import numpy as np
import torch

def plot_parity(ax, true, pred, label=None):

    if isinstance(true, torch.Tensor):
        true = true.detach().cpu().numpy()
    
    if isinstance(pred, torch.Tensor):
        pred = pred.detach().cpu().numpy()

    mse = np.mean((true.flatten() - pred.flatten())**2)

    if label is None:
        label = ''        
    ax.scatter(true, pred, label=label+' MSE: {:.3f}'.format(mse))

    ax.set_xlabel('True Energy')
    ax.set_ylabel('Predicted Energy')
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    lim = (min(xlim[0], ylim[0]), max(xlim[1], ylim[1]))
    ax.plot(lim, lim, 'k--')
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.legend()

