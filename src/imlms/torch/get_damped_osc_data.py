import torch

def get_damped_osc_dataset(n=35):
    A = 2
    gamma = torch.pi / 10
    omega = torch.pi / 3

    t = torch.linspace(0, 10, n)

    x = A * torch.exp(-gamma * t) * torch.cos(omega * t) + torch.randn(t.size()) * 0.1

    return t, x