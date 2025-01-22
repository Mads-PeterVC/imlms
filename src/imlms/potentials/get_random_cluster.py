from ase import Atoms 
import numpy as np
from agox.generators import RandomGenerator
from agox.environments import Environment
from agox.utils.plot import plot_atoms, plot_cell
import matplotlib.pyplot as plt

def get_random_cluster():
    cell_size = 8
    edge_size = 2
    a = cell_size - edge_size
    conf_cell = np.array([[a, 0, 0], [0, a, 0], [0, 0, 0]])
    conf_corner = np.array([edge_size/2, edge_size/2, cell_size/2])

    environment = Environment(template=Atoms('', cell=np.eye(3)*cell_size), 
                            symbols="He10",
                            confinement_corner=conf_corner,
                            confinement_cell=conf_cell, 
                            print_report=False)

    generator = RandomGenerator(**environment.get_confinement())

    atoms = generator.get_candidates(sampler=None, environment=environment)[0]
    atoms.center()
    return atoms
