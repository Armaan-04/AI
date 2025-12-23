from optimum.intel.openvino import OVStableDiffusionPipeline
import os


# 1. Configuration
# We use v1-5 as it is more robust and public than v1-4 or 2-1
model_id = "runwayml/stable-diffusion-v1-5"
save_directory = "sd_v15_openvino_model"

# 2. Check if we already converted the model locally
if not os.path.exists(save_directory):
    print(f"First time setup: Exporting {model_id} to OpenVINO format...")
    # export=True downloads the standard model and converts it for your Intel GPU
    pipe = OVStableDiffusionPipeline.from_pretrained(model_id, export=True)

    # Save it so we don't have to wait 10+ minutes next time
    pipe.save_pretrained(save_directory)
    print(f"Model saved to {save_directory}")
else:
    print("Loading optimized model from local storage...")
    pipe = OVStableDiffusionPipeline.from_pretrained(save_directory, compile=False)

# 3. Target your Intel Iris Xe (GPU)
# This will be much faster than your CPU
pipe.to("GPU")
pipe.compile()

# 4. Generate the image
prompt = "Flying cars soar over a futuristic cityscape at sunset."

print("Generating image on Intel Iris Xe... (approx 1-2 mins)")
# 20 steps is perfect for a quick, high-quality result
image = pipe(prompt, num_inference_steps=20).images[0]

# 5. Save the final image
image.save("Generate_image_accelerated.png")
print("Success! Image saved as Generate_image_accelerated.png")