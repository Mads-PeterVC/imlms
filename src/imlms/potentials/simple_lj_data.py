import numpy as np
import torch
from ase.calculators.lj import LennardJones
from ase import Atoms

def get_positions(r):
    return np.array([[0, 0, 0], [0, 0, r]])

def get_energy(r, sigma=1, epsilon=1):
    atoms = Atoms('2He', positions=get_positions(r))
    calc = LennardJones(sigma=sigma, epsilon=epsilon, rc=10.0)
    atoms.calc = calc
    return atoms.get_potential_energy()

def get_simple_lj_dataset(n_samples=25, print_values=False):

    sigma = np.random.uniform(1.0, 2, 1)[0]
    epsilon = np.random.uniform(1.0, 2, 1)[0]

    if print_values:
        print(f"{sigma = }")
        print(f"{epsilon = }")

    r0 = 2**(1/6) * sigma
    R = np.random.uniform(0.8*r0, 1.2*r0, n_samples)
    y = torch.tensor([get_energy(r, sigma, epsilon) for r in R]).float()
    R = torch.tensor(R).float().view(-1, 1)

    return R, y



