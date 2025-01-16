import nbformat

def get_solution_cells(notebook):
    solution_cells = [False for cell in notebook.cells]
    for i, cell in enumerate(notebook.cells):
        if '!solution' in cell.source.lower():
            solution_cells[i] = True

    return solution_cells

def get_exercise_cells(notebook):
    exercise_cells = [False for cell in notebook.cells]
    for i, cell in enumerate(notebook.cells):
        if '#!exercise' in cell.source.lower():
            exercise_cells[i] = True

    return exercise_cells

def create_student_notebook(master_notebook):
    student_notebook = nbformat.v4.new_notebook()
    solution_cells = get_solution_cells(master_notebook)

    for cell, solution in zip(master_notebook.cells, solution_cells):
        if not solution:
            student_notebook.cells.append(cell)

    strip_tags(student_notebook)
    remove_output(student_notebook)

    return student_notebook

def create_solution_notebook(master_notebook):
    solution_notebook = nbformat.v4.new_notebook()
    exercise_cells = get_exercise_cells(master_notebook)

    for cell, exercise in zip(master_notebook.cells, exercise_cells):            
        if not exercise:
            solution_notebook.cells.append(cell)

    strip_tags(solution_notebook)

    return solution_notebook

def strip_tags(notebook):
    for cell in notebook.cells:
        if '#!' in cell.source:
            lines = cell.source.split('\n')
            new_lines = [line for line in lines if '#!' not in line]
            cell.source = '\n'.join(new_lines)

def remove_output(notebook):
    for cell in notebook.cells:
        cell.outputs = []
        cell.execution_count = None
    

if __name__ == '__main__':

    path = '/Users/au616397/Repositories/imlms/lessons/lesson_1/numpy_exercises_master.ipynb'

    master = nbformat.read(path, as_version=4)
    student_notebook = create_student_notebook(master.copy())
    nbformat.write(student_notebook, 'student.ipynb')


    master = nbformat.read(path, as_version=4)
    solution_notebook = create_solution_notebook(master.copy())
    nbformat.write(solution_notebook, 'solution.ipynb')