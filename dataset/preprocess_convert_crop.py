from pathlib import Path
import os
import json
from tqdm.rich import tqdm
from PIL import Image
import PIL

PIL.Image.MAX_IMAGE_PIXELS = 1e20


def crop_half_width(im):
    w, h = im.size
    crop_w = w // 2
    for i in range(2):
        box = (i * crop_w, 0, (i + 1) * crop_w, h)
        yield i * crop_w, im.crop(box)


def crop_half_height(im):
    w, h = im.size
    crop_h = h // 2
    for i in range(2):
        box = (0, i * crop_h, w, (i + 1) * crop_h)
        yield i * crop_h, im.crop(box)


def recursive_split_iterator(
    image: Image, max_size: int, crop_w: int = 0, crop_h: int = 0, cropped=False
):
    w, h = image.size
    if w > max_size:
        print(f"Splitting {w}x{h} image into two halves, width-wise")
        for piece_crop_w, piece in crop_half_width(image):
            cw, ch = piece.size
            print(f"Half width: {cw}x{ch}")
            yield from recursive_split_iterator(
                piece, max_size, crop_w + piece_crop_w, crop_h, cropped=True
            )
    elif h > max_size:
        print(f"Splitting {w}x{h} image into two halves, height-wise")
        for piece_crop_h, piece in crop_half_height(image):
            cw, ch = piece.size
            print(f"Half height: {cw}x{ch}")
            yield from recursive_split_iterator(
                piece, max_size, crop_w, crop_h + piece_crop_h, cropped=True
            )
    else:
        yield crop_w, crop_h, image, cropped


if __name__ == "__main__":
    image_folder = "D:/Data/nasa/images"
    output_image_folder = "D:/Data/nasa/processed"
    max_size = 12_000

    os.makedirs(output_image_folder, exist_ok=True)
    metadata = {}
    with open(os.path.join(image_folder, "metadata.jsonl"), "r") as f:
        for line in f:
            meta = json.loads(line)
            meta["crop_w"] = 0
            meta["crop_h"] = 0
            metadata[meta["file_name"]] = meta

    with open(os.path.join(output_image_folder, "metadata.jsonl"), "w") as f:
        for file in tqdm(list(Path(image_folder).glob("*.tif"))):
            meta = metadata[file.name]
            image = Image.open(file)
            image = image.convert("RGB")
            image.thumbnail(image.size)
            for crop_w, crop_h, piece, cropped in recursive_split_iterator(
                image, max_size
            ):
                meta = meta.copy()
                if cropped:
                    output_file_name = file.stem + f"_{crop_w}_{crop_h}.png"
                else:
                    output_file_name = file.stem + ".png"
                meta["file_name"] = output_file_name
                meta["crop_w"] = crop_w
                meta["crop_h"] = crop_h
                meta["cropped"] = cropped
                w, h = piece.size
                meta["width"] = w
                meta["height"] = h
                # 24 bits per pixel, 3 channels, one byte per channel
                meta["file_size"] = w * h * 3
                output_file_path = os.path.join(output_image_folder, output_file_name)
                piece.save(output_file_path, "PNG")
                f.write(json.dumps(meta) + "\n")
