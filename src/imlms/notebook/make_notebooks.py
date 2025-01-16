from pathlib import Path
import nbformat
from .notebook_utils import create_student_notebook, create_solution_notebook

def make_notebooks(path):
    """
    Make regular and solution notebooks given a master notebook.
    """

    if not isinstance(path, Path):
        path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f'{path} does not exist.')
    
    if '_master' not in path.stem:
        raise ValueError('Only master notebooks are supported.')
    
    # Cereate regular notebook
    master = nbformat.read(str(path), as_version=4)
    student_notebook = create_student_notebook(master.copy())
    student_path = (path.parent / path.stem.replace('_master', '')).with_suffix(path.suffix)
    nbformat.write(student_notebook, str(student_path))

    # # Create solution notebook
    master = nbformat.read(str(path), as_version=4)
    solution_notebook = create_solution_notebook(master.copy())
    solution_path = (path.parent / path.stem.replace('_master', '_solution')).with_suffix(path.suffix)
    nbformat.write(solution_notebook, str(solution_path))



