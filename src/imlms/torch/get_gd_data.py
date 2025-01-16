import torch

def get_example_data(n=25):
    x = torch.linspace(-1, 1, n).view(-1, 1)
    y = 2 * x + torch.randn(x.size()) * 0.33
    return x, y