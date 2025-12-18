import torch

# 1D Tensor (Vector)
vector = torch.tensor([1.0, 2.0, 3.0])

# 2D Tensor (Matrix) filled with zeros
matrix = torch.zeros((2, 3))

# 3D Tensor (Random values) - common for image data
random_data = torch.rand((3, 64, 64))

print(f"Dimensions: {random_data.ndim}")
print(f"Shape: {random_data.shape}")
print(f"Data Type: {random_data.dtype}")

'''if torch.cuda.is_available():
    random_data = random_data.to("cuda")
    print("Tensor moved to GPU!")'''