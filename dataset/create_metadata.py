import os
import math
from pathlib import Path
import json
from tqdm.rich import tqdm
import PIL
from PIL import Image

PIL.Image.MAX_IMAGE_PIXELS = 1e20


def convert_file_size_to_int(size) -> int:
    """
    Converts a size expressed as a string with digits an unit (like `"50MB"`) to an integer (in bytes).

    Args:
        size (`int` or `str`): The size to convert. Will be directly returned if an `int`.

    Example:

    ```py
    >>> convert_file_size_to_int("1MiB")
    1048576
    ```
    """
    if isinstance(size, int):
        return size
    if size.upper().endswith("PIB"):
        return int(size[:-3]) * (2**50)
    if size.upper().endswith("TIB"):
        return int(size[:-3]) * (2**40)
    if size.upper().endswith("GIB"):
        return int(size[:-3]) * (2**30)
    if size.upper().endswith("MIB"):
        return int(size[:-3]) * (2**20)
    if size.upper().endswith("KIB"):
        return int(size[:-3]) * (2**10)
    if size.upper().endswith("PB"):
        int_size = int(size[:-2]) * (10**15)
        return int_size // 8 if size.endswith("b") else int_size
    if size.upper().endswith("TB"):
        int_size = int(size[:-2]) * (10**12)
        return int_size // 8 if size.endswith("b") else int_size
    if size.upper().endswith("GB"):
        int_size = int(size[:-2]) * (10**9)
        return int_size // 8 if size.endswith("b") else int_size
    if size.upper().endswith("MB"):
        int_size = int(size[:-2]) * (10**6)
        return int_size // 8 if size.endswith("b") else int_size
    if size.upper().endswith("KB"):
        int_size = int(size[:-2]) * (10**3)
        return int_size // 8 if size.endswith("b") else int_size
    raise ValueError(
        f"`size={size}` is not in a valid format. Use an integer followed by the unit, e.g., '5GB'."
    )


def strip_quotes(s):
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    return s


if __name__ == "__main__":
    image_folder = "D:/Data/nasa/images"
    meta_folder = "D:/Data/nasa/meta"
    missing_folder = "D:/Data/nasa/images_missing_meta"
    output_file_path = "D:/Data/nasa/images/metadata.jsonl"
    num_shards = 300
    metadata = []
    for file in tqdm(list(Path(image_folder).glob("*.tif"))):
        file_name = file.name.replace(".tif", ".json")
        meta_file = os.path.join(meta_folder, file_name)
        if not os.path.exists(os.path.join(image_folder, meta_file)):
            print(f"Missing image: {file.name}")
            os.rename(
                os.path.join(image_folder, file.name),
                os.path.join(missing_folder, file.name),
            )
            continue
        with open(meta_file, "r") as f:
            raw_data = json.load(f)
        data = {
            "file_name": file.name,
            "text": (
                strip_quotes(raw_data["title"])
                + ": "
                + strip_quotes(raw_data["description"])
            ),
        }
        for key, value in raw_data.items():
            if key != "meta":
                data[key] = value
        meta = raw_data["meta"]
        for key, value in meta.items():
            data[key] = value
        im = Image.open(file)
        w, h = im.size
        data["width"] = w
        data["height"] = h
        # 24 bits per pixel, 3 channels, one byte per channel
        data["file_size"] = w * h * 3
        metadata.append(data)

    # sort entries by file size such that the largest images are first
    metadata.sort(key=lambda x: x["file_size"], reverse=True)

    # compute the total size of the dataset
    dataset_nbytes = sum(entry["file_size"] for entry in metadata)

    num_images_per_shard = int(math.ceil(len(metadata) / num_shards))

    # create the shards
    shards = {
        i: {
            "size": 0,
            "entries": [],
        }
        for i in range(num_shards)
    }
    shards_with_space = set(range(num_shards))

    # fill the shards such that each shard has nearly the same number of images and the same total size
    for entry in metadata:
        # of the shards that have space, pick the one with the smallest size
        shard = min(shards_with_space, key=lambda x: shards[x]["size"])

        shards[shard]["size"] += entry["file_size"]
        shards[shard]["entries"].append(entry)
        if len(shards[shard]["entries"]) >= num_images_per_shard:
            shards_with_space.remove(shard)

    max_actual_shard_size = max(shard["size"] for shard in shards.values())
    min_actual_shard_size = min(shard["size"] for shard in shards.values())
    average_actual_shard_size = sum(shard["size"] for shard in shards.values()) / len(
        shards
    )
    min_actual_shard_count = min(len(shard["entries"]) for shard in shards.values())
    max_actual_shard_count = max(len(shard["entries"]) for shard in shards.values())

    print(
        f'Max file size: {max(entry["file_size"] for entry in metadata) / 1e6:.0f} MBs'
    )

    print(f"Min shard size: {min_actual_shard_size / 1e6:.0f} MBs")

    print(f"Max shard size: {max_actual_shard_size / 1e6:.0f} MBs")

    print(f"Avg shard size: {average_actual_shard_size / 1e6:.0f} MBs")

    print(
        f"Min shard count: {min_actual_shard_count} of {num_images_per_shard} images per shard"
    )

    print(
        f"Max shard count: {max_actual_shard_count} of {num_images_per_shard} images per shard"
    )
    # recreate the metadata list with the shards
    sharded_metadata = []
    for shard in shards.values():
        sharded_metadata.extend(shard["entries"])

    assert len(sharded_metadata) == len(
        metadata
    ), f"The number of entries changed after sharding from {len(metadata)} to {len(sharded_metadata)}"

    with open(output_file_path, "w") as fo:
        for data in sharded_metadata:
            fo.write(json.dumps(data) + "\n")
