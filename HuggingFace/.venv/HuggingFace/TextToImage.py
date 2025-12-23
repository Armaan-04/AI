from diffusers import StableDiffusionPipeline
import torch

#Load the Stable Diffusion Model
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id , torch_dtype=torch.float16)

#Move the model to GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

#Define your text prompt
prompt = "Flying cars soar over a futuristic cityscape at sunset."

#Generate the image
with torch.autocast("cuda"): #Using autocast for mixed precision (faster on GPU)
    image = pipe(prompt).images[0]
# The pipeline shows a progress bar by default in the terminal


#Save the image
image.save("Generate_image.png")
print("Image saved as generated_image.png")

