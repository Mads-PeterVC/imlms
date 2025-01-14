from ase.calculators.calculator import Calculator, all_changes

def get_calculator_from_class(cls):
    class CalculatorWrapper(Calculator):        
        implemented_properties = ['energy', 'forces']
        def __init__(self, **kwargs):
            super().__init__()
            self.calculator = cls(**kwargs)
        def calculate(self, atoms=None, properties=['energy'], system_changes=all_changes):
            Calculator.calculate(self, atoms, properties, system_changes)
            energy, forces = self.calculator.calculate(atoms)
            self.results['energy'] = energy
            self.results['forces'] = forces
    return CalculatorWrapper

