from easy_start.project_templates.python_package import PythonPackageSettings, start_python_package
from easy_start.project_templates.cpp_executable import CppExecutableSettings, start_cpp_executable

from pathlib import Path


def start_project(
    destination: Path,
    settings: PythonPackageSettings | CppExecutableSettings,
):
    match settings:
        case PythonPackageSettings():
            start_python_package(destination, settings)

        case CppExecutableSettings():
            start_cpp_executable(destination, settings)

        case _:
            raise ValueError(f'Unavailable settings {settings}')
