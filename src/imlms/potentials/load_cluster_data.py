import numpy as np
from scipy.spatial.distance import pdist
from importlib.resources import path
import torch

def load_cluster_data():

    with path('imlms.potentials.data', 'rattle_data.npz') as p:

        data = np.load(p)
        positions = data['positions']
        energies = data['energies']

    return positions, energies

def get_cluster_data(train=True):
    positions, energies = load_cluster_data()
    distances = np.array([pdist(p) for p in positions])

    # Convert to tensors
    positions = torch.tensor(positions).float()
    distances = torch.tensor(distances).float()
    energies = torch.tensor(energies).float()

    if train: 
        indices = torch.arange(0, 300)
    else:
        indices = torch.arange(300, 1000)        

    return positions[indices], distances[indices], energies[indices]








