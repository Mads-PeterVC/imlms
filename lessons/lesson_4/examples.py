import torch

class NonlinearRegression(torch.nn.Module):
    def __init__(self):
        super(NonlinearRegression, self).__init__()
        self.linear_1 = torch.nn.Linear(3, 4)
        self.linear_2 = torch.nn.Linear(4, 2)

    def forward(self, x):            
        x = self.linear_1(x)
        x = torch.relu(x)
        x = self.linear_2(x)
        return x