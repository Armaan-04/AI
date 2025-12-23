from diffusers import StableDiffusionPipeline
import torch

#Load the model
pipe = StableDiffusionPipeline.from_pretained("runwayml/stable-diffusion-v1.5" , torch.device("cpu") )
#pipe = pipe.to("cuda")

prompt = "A futuristic cityscape at night with flying cars."
frames= []
for i in range(10): #generate 10 frames
    frame = pipe(prompt).frames[0]
    frames.append(frame)

import cv2
import numpy as np

#save frames into a video
for i , frame in enumerate(frames):
    cv2.imwrite(f"frame{i}.png", np.array(frame))

#Stitch frames into a video
frame_rate = 5
frame_size = frames[0].size
out = cv2.VideoWriter("output_video.mp4" , cv2.VideoWriter_fourcc(*"mp4v"), frame_rate, frame_size)

for i in range(len(frames)):
    frame = cv2.imread(f"frame{i}.png")
    out.write(frame)

out.release()