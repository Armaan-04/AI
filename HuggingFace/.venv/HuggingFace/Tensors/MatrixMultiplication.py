import torch

# A 2x3 matrix (2 rows, 3 columns)
tensor_A = torch.tensor([[1, 2, 3],
                         [4, 5, 6]])

# A 3x2 matrix (3 rows, 2 columns)
tensor_B = torch.tensor([[7, 8],
                         [9, 10],
                         [11, 12]])

# Multiply them
result = torch.matmul(tensor_A, tensor_B)
print(result)
