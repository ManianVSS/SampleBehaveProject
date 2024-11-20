import os

from behave import given
from behave.step_registry import registry

from utils import importutil

if __name__ == '__main__':

    step_definition_module_python_files = importutil.get_python_files("features/steps")

    # Scan for each python module if it has step definitions, add them to step definition mapping
    for py_file in step_definition_module_python_files:
        module_name = os.path.split(py_file)[-1].strip(".py")
        imported_step_def_module = importutil.dynamic_import(module_name, py_file)

    steps = []
    steps.extend(registry.steps['given'])
    steps.extend(registry.steps['when'])
    steps.extend(registry.steps['then'])
    steps.extend(registry.steps['step'])

    for step in steps:
        print(step.pattern)
