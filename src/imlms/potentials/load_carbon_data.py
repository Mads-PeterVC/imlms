from importlib.resources import files
from ase.io import read, write
import torch
import numpy as np
from ase import Atoms
from scipy.spatial.distance import cdist

def load_data(n, max_examples=None):
    path = files('imlms.potentials.data.carbon') / f'n_carbon_{n}_reduced.traj'

    if max_examples is None:
        atoms = read(path, index=':')
    else:
        atoms = read(path, index=f'0:{max_examples}')
    positions = np.array([a.positions for a in atoms])
    energies = np.array([a.get_potential_energy() for a in atoms])

    return positions, energies

def get_carbon_cluster_data(n, train=True, max_examples=None):
    assert n in [5, 6, 7, 8, 9, 10, 11, 12], 'Invalid cluster size'
    positions, energies = load_data(n, max_examples=max_examples)

    return torch.tensor(positions).float(), torch.tensor(energies).float()

def to_atoms(X):
    atoms = Atoms(f'C{X.shape[0]}', positions=X, cell=np.eye(3)*10)
    atoms.center()
    return atoms

def get_invariances_examples():

    X, E = get_carbon_cluster_data(6)

    sort_index = np.argsort(E)
    return to_atoms(X[sort_index[0]]), to_atoms(X[sort_index[1]])

def identity_atoms(atoms):
    return atoms

def translate_atoms(atoms):
    atoms = atoms.copy()
    atoms.positions += np.array([2, 0, 0])
    return atoms

def rotate_atoms(atoms):
    atoms = atoms.copy()
    atoms.rotate(90, 'z', center='COM')
    return atoms

def permute_atoms(atoms):
    atoms = atoms.copy()
    perm = np.array(np.arange(len(atoms)))-1
    atoms.positions = atoms.positions[perm]
    return atoms

transforms = {
    'identity': identity_atoms,
    'translate': translate_atoms,
    'rotate': rotate_atoms,
    'permute': permute_atoms
}

def get_atomic_dataset(n, threshold=2.5):

    X, _ = load_data(n)

    y = []
    for x in X:        
        D = cdist(x, x) + np.eye(len(x))*100
        D = np.count_nonzero(D < threshold, axis=1)
        y.append(D)
    
    return X, np.array(y)





if __name__ == '__main__':

    X, E = get_carbon_cluster_data(5)

    print(X.shape, E.shape)