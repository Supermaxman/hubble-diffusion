import PIL
from PIL import Image

PIL.Image.MAX_IMAGE_PIXELS = 1e20

from datasets import load_dataset


if __name__ == "__main__":
    image_folder = "D:/Data/nasa/processed"
    num_shards = 200
    ds = load_dataset("imagefolder", data_dir=image_folder, split="train")
    # work-around for massive images
    # ds.push_to_hub("esa-hubble", num_shards=len(ds))
    ds.push_to_hub("esa-hubble", num_shards=num_shards)
