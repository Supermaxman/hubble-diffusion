---
license: openrail++
language: 
  - en
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
widget:
- text: "Hubble snaps images of the birthplace of stars within a cluster: The dust and gas expand within the cluster due to the powerful influence of baby stars. With these new images comes improved detail and a clearer view for astronomers to study how early stars are born and change over time."
  example_title: Baby Stars
- text: "Hubble captures the death of a star: Old stars, nearing the end of their life, collapse under the weight of their own gravity and the outer layers explode as a 'supernova'. In this image Hubble captures the moments after collapse, where the star has exploded and left an empty void in its place, where a new black hole has emerged."
  example_title: Old Stars
- text: "Hubble image of galaxies colliding: The distorted spirals of two distant galaxies colliding are captured here in a new image from the NASA/ESA Hubble Space Telescope. The typically symmetric spirals common in spiral galaxies appear significantly warped, as the shape of both galaxies is torn apart by their gravitational pulls."
  example_title: Galaxies Collide
- text: "Pink-tinted plumes in the Large Magellanic Cloud: The aggressively pink plumes seen in this image are extremely uncommon, with purple-tinted currents and nebulous strands reaching out into the surrounding space."
  example_title: Pink Plumes
- text: "The stellar plasma of Wolf 359: The red dwarf star Wolf 359 from the constellation Leo is captured in extreme detail in a new image from the NASA/ESA Hubble Space Telescope. Wolf 359, classified as a M6 red dwarf, has certain peculiar qualities indicated by an unusual ejection of plasma. The Hubble telescope was able to capture one such event"
  example_title: Wolf 359
thumbnail: ""
inference: true
datasets:
- Supermaxman/esa-hubble
---

# Hubble Diffusion v2: Stable Diffusion v2.1 fine tuned on ESA Hubble Deep Space Images & Captions

Put in a detailed text prompt and generate high-quality Hubble Deep Space Images! Now with Stable Diffusion 2.1!

## 512x512 Diffusion Examples

Generated with the `StableDiffusionPipeline` with a normal Google Colab GPU with 15 GB of VRAM.
Images are arranged in a `3x3` grid from using a `batch_size` of `9`.
Details and code is provided in the [Usage](#usage) section.
Each of the following `3x3` examples took just over a minute to generate:

 > Hubble captures the death of a star: Old stars, nearing the end of their life, collapse under the
 > weight of their own gravity and the outer layers explode as a 'supernova'. In this image Hubble
 > captures the moments after collapse, where the star has exploded and left an empty void in its
 > place, where a new black hole has emerged.
>![old.png](https://github.com/Supermaxman/hubble-diffusion/blob/04da8c799098d27c59610b92c15a00fbfa21a1ea/examples/hubble-diffusion-2/old.png?raw=true)

 > Pink-tinted plumes in the Large Magellanic Cloud:
 > The aggressively pink plumes seen in this image are extremely uncommon,
 > with purple-tinted currents and nebulous strands reaching out into the surrounding space.
 >![pink.png](https://github.com/Supermaxman/hubble-diffusion/blob/04da8c799098d27c59610b92c15a00fbfa21a1ea/examples/hubble-diffusion-2/pink.png?raw=true)

 > Hubble snaps images of the birthplace of stars within a cluster:
 > The dust and gas expand within the cluster due to the powerful influence of baby stars.
 > With these new images comes improved detail and a clearer view for astronomers to
 > study how early stars are born and change over time.
>![baby.png](https://github.com/Supermaxman/hubble-diffusion/blob/04da8c799098d27c59610b92c15a00fbfa21a1ea/examples/hubble-diffusion-2/baby.png?raw=true)

 > Hubble image of galaxies colliding: The distorted spirals of two distant galaxies colliding are
 > captured here in a new image from the NASA/ESA Hubble Space Telescope. The typically symmetric
 > spirals common in spiral galaxies appear significantly warped, as the shape of both galaxies is torn
 > apart by their gravitational pulls.
>![collide.png](https://github.com/Supermaxman/hubble-diffusion/blob/04da8c799098d27c59610b92c15a00fbfa21a1ea/examples/hubble-diffusion-2/collide.png?raw=true)

 > The stellar plasma of Wolf 359: The red dwarf star Wolf 359 from the constellation Leo is captured in extreme detail in a new image from the NASA/ESA Hubble Space Telescope.
 > Wolf 359, classified as a M6 red dwarf, has certain peculiar qualities indicated by an unusual ejection of plasma. The Hubble telescope was able to capture one such event
>![wolf359.png](https://github.com/Supermaxman/hubble-diffusion/blob/04da8c799098d27c59610b92c15a00fbfa21a1ea/examples/hubble-diffusion-2/wolf359.png?raw=true)

More examples can be found in the [GitHub repository](https://github.com/Supermaxman/hubble-diffusion).

## 2560x1536 MultiDiffusion Examples

Yes, you heard that right! With the `StableDiffusionPanoramaPipeline` from [MultiDiffusion](https://multidiffusion.github.io/) and `enable_xformers_memory_efficient_attention` from [xformers](https://huggingface.co/docs/diffusers/optimization/fp16#memory-efficient-attention) you can actually generate 1440p images on a normal Google Colab GPU with 15 GB of VRAM!
Details and code is provided in the [Usage](#usage) section.
Each of the following examples took just over an hour to generate, but are absolutely worth it:

> Aqua-tinted plumes in the Large Magellanic Cloud:
> The deep aqua plumes seen in this image are extremely uncommon, with purple-tinted currents and nebulous strands reaching out into the surrounding space.
>![aqua-2560-1536-128.png](https://github.com/Supermaxman/hubble-diffusion/blob/04da8c799098d27c59610b92c15a00fbfa21a1ea/examples/hubble-diffusion-2/aqua-2560-1536-128.png?raw=true)

> A slow and deadly dance:
Most solar systems only contain a single star, while rarely binary star systems can contain two stars closely orbiting each other.
> With this new image, Hubble captures an extremely rare trinary star system, where three stars orbit each other in a daring yet dangerous dance.
>![trinary-2560-1536-257.png](https://github.com/Supermaxman/hubble-diffusion/blob/04da8c799098d27c59610b92c15a00fbfa21a1ea/examples/hubble-diffusion-2/trinary-2560-1536-257.png?raw=true)

## Model Details

- **Developed by:** Maxwell Weinzierl
- **Model type:** Diffusion-based text-to-image generation model
- **Language(s):** English
- **License:** [CreativeML Open RAIL++-M License](https://huggingface.co/stabilityai/stable-diffusion-2/blob/main/LICENSE-MODEL)
- **Model Description:** This is a model that can be used to generate and modify images based on text prompts. It is a [Latent Diffusion Model](https://arxiv.org/abs/2112.10752) that uses a fixed, pretrained text encoder ([OpenCLIP-ViT/H](https://github.com/mlfoundations/open_clip)), with initial weights from [stabilityai/stable-diffusion-2-1-base](https://huggingface.co/stabilityai/stable-diffusion-2-1-base). It was fine-tuned on [Supermaxman/esa-hubble](https://huggingface.co/datasets/Supermaxman/esa-hubble).
- **Resources for more information:** [GitHub Repository](https://github.com/Stability-AI/).
- **Cite as:**

```bibtex
@misc{weinzierl2023sdhubble2,
  author = {Weinzierl, Maxwell A.},
  title = {Hubble Diffusion v2: Stable Diffusion v2.1 fine tuned on ESA Hubble Deep Space Images & Captions},
  year={2023},
  howpublished= {\url{https://huggingface.co/Supermaxman/hubble-diffusion-2}}
} 
```

Also, be sure to check out the prior version [Hubble Diffusion v1](https://huggingface.co/Supermaxman/hubble-diffusion-1)!

## Examples

We recommend using [🤗's Diffusers library](https://github.com/huggingface/diffusers) to run Hubble Diffusion.

### Usage

#### 512x512 Generation

```bash
pip install transformers diffusers accelerate
```

```python
import torch
from diffusers import StableDiffusionPipeline

model_id = "Supermaxman/hubble-diffusion-2"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")
# saves GPU memory for small inference cost
pipe.enable_attention_slicing()

prompt = "Hubble snaps images of the birthplace of stars within a cluster: The dust and gas expand within the cluster due to the powerful influence of baby stars. With these new images comes improved detail and a clearer view for astronomers to study how early stars are born and change over time."
image = pipe(prompt).images[0]
image
```

>![example.png](https://github.com/Supermaxman/hubble-diffusion/blob/04da8c799098d27c59610b92c15a00fbfa21a1ea/examples/hubble-diffusion-2/example.png?raw=true)

#### 2560x1536 MultiDiffusion Generation

```bash
pip install transformers diffusers accelerate xformers
```

```python
import torch
from diffusers import StableDiffusionPanoramaPipeline, DDIMScheduler

model_id = 'Supermaxman/hubble-diffusion-2'
scheduler = DDIMScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPanoramaPipeline.from_pretrained(
     model_id, scheduler=scheduler, torch_dtype=torch.float16
)
# saves significant GPU memory and can be faster for inference
pipe.enable_xformers_memory_efficient_attention()
pipe = pipe.to("cuda")

prompt = "A slow and deadly dance: Most solar systems only contain a single star, while rarely binary star systems can contain two stars closely orbiting each other. With this new image, Hubble captures an extremely rare trinary star system, where three stars orbit each other in a daring yet dangerous dance."
image = pipe(prompt).images[0]
image
```

>![trinary-2560-1536-258.png](https://github.com/Supermaxman/hubble-diffusion/blob/e76b22c805eea07e376f23ad12bb9ddecfd47cca/examples/hubble-diffusion-2/trinary-2560-1536-258.png?raw=true)

## Model description

Trained on [ESA Hubble Deep Space Images & Captions](https://huggingface.co/datasets/Supermaxman/esa-hubble) using [Google Colab Pro](https://colab.research.google.com/signup) with a single A100 GPU for around 33,000 steps (about 12 hours, at a cost of about $20).
More details can be found at the [GitHub repo](https://github.com/Supermaxman/hubble-diffusion).

## Links

- [Captioned Hubble Deep Space Scans dataset](https://huggingface.co/datasets/Supermaxman/esa-hubble)
- [Model weights in Diffusers format](https://huggingface.co/Supermaxman/hubble-diffusion-2)
- [Training code](https://github.com/Supermaxman/hubble-diffusion)
- [Hubble Diffusion v1](https://huggingface.co/Supermaxman/hubble-diffusion-1)

Trained by [Maxwell Weinzierl](https://personal.utdallas.edu/~maxwell.weinzierl/) ([@Supermaxman1](https://twitter.com/Supermaxman1)).

## Citation

```bibtex
@misc{weinzierl2023sdhubble2,
  author = {Weinzierl, Maxwell A.},
  title = {Hubble Diffusion v2: Stable Diffusion v2.1 fine tuned on ESA Hubble Deep Space Images & Captions},
  year={2023},
  howpublished= {\url{https://huggingface.co/Supermaxman/hubble-diffusion-2}}
} 
```
