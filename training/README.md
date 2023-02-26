
# Hubble Diffusion

## Training Hubble Diffusion v1

Training requires a premium A100 GPU along with high memory mode from Google colab.
Initial training utilized the `train_text_to_image_streaming.py` script, as it was believed
that the `Supermaxman/esa-hubble` dataset would be too big to download to disk.
After monitoring GPU usage, it was found that only 10%-20% of the GPU was being utilized with the streaming approach, and therefore significant speed gains could be achieved if the dataset could first be downloaded and then used for training.
The dataset ended up barely fitting on the 160 GB storage space on Google colab, but it was able to be downloaded and GPU utilization went up to 60%-70% with the `train_text_to_image.py` script.

The following command was used to train the model:

```bash
accelerate launch train_text_to_image.py \
--pretrained_model_name_or_path="CompVis/stable-diffusion-v1-4" \
--dataset_name="Supermaxman/esa-hubble" \
--seed=0 \
--use_ema \
--resolution=512 \
--num_workers=12 \
--random_flip \
--train_batch_size=1 \
--gradient_accumulation_steps=4 \
--mixed_precision="fp16" \
--num_train_epochs=50 \
--checkpointing_steps=1000 \
--learning_rate=1e-05 \
--resume_from_checkpoint="latest" \
--checkpoints_total_limit=3 \
--report_to="wandb" \
--project_name="esa-hubble" \
--output_dir="/content/gdrive/MyDrive/Models/hubble/esa-hubble-v1"
```

## Training Hubble Diffusion v2

Training requires a premium A100 GPU along with high memory mode from Google colab.
Training utilized the `train_text_to_image.py` script along with the `Supermaxman/esa-hubble` dataset.
The dataset barely fit on the 160 GB storage space on Google colab, but it was downloaded and GPU utilization was 60%-70%.

The following command was used to train the model:

```bash
accelerate launch train_text_to_image.py \
--pretrained_model_name_or_path="stabilityai/stable-diffusion-2-1-base" \
--dataset_name="Supermaxman/esa-hubble" \
--seed=0 \
--use_ema \
--resolution=512 \
--num_workers=12 \
--random_flip \
--train_batch_size=1 \
--gradient_accumulation_steps=4 \
--mixed_precision="fp16" \
--num_train_epochs=50 \
--checkpointing_steps=1000 \
--learning_rate=1e-05 \
--resume_from_checkpoint="latest" \
--checkpoints_total_limit=3 \
--report_to="wandb" \
--project_name="esa-hubble" \
--output_dir="/content/gdrive/MyDrive/Models/hubble/esa-hubble-v2"
```
