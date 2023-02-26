import os
import math
from pathlib import Path
import json
from tqdm.rich import tqdm


if __name__ == "__main__":
    metadata_path = "D:/Data/nasa/processed/metadata.jsonl"
    file_sizes = []
    heights = []
    widths = []
    examples = ["opo9941a", ""]
    with open(metadata_path, "r") as f:
        for line in f:
            data = json.loads(line)
            file_sizes.append(data["file_size"])
            heights.append(data["height"])
            widths.append(data["width"])
    print(f"Total number of images: {len(file_sizes)}")
    print(f"Total size of dataset: {sum(file_sizes) / 1e9:.0f} GB")
    print(f"Average image size: {sum(file_sizes) / len(file_sizes) / 1e6:.0f} MB")
    print(f"Average image height: {sum(heights) / len(heights):.0f} px")
    print(f"Average image width: {sum(widths) / len(widths):.0f} px")
    print(f"Max image size: {max(file_sizes) / 1e6:.0f} MB")
