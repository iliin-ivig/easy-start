# Installation
From cloned repo:
```sh
pip3 install path/to/cloned/repo
```

From cloud-based git repository:
```sh
pip3 install git+ssh://git@https://github.com/iliin-ivig/easy-start
```

# Usage examples

## Python Package

```python
from easy_start import start_project, PythonPackageSettings
from pathlib import Path

settings = PythonPackageSettings(
    package_name='easy_start',
    full_package_name='ivig-easy-start',
    description='This package helps initialize a project using a parameterized template.',
    url='https://github.com/iliin-ivig/easy-start',
    requirements=[
        'Jinja2~=3.1.2',
    ],
    scripts=[
        'ivig-easy-start',
    ],
    include_static_data=True,
)

start_project(
    destination=Path('./path/to/new_python_project'),
    settings=settings,
)
```

## C++ project with executables

```python
from easy_start import start_project, CppExecutableSettings
from pathlib import Path

settings = CppExecutableSettings(
    project_name='BestProjectEver',
    project_short_name='bpe',
    description='description',
    url='https://github.com/author/BestProjectEver',
    requirements=['fmt/9.1.0', 'nlohmann_json/3.11.2'],
    executables=['run', 'server'],
    source_folder='src',
    bin_folder='bin',
)

start_project(
    destination=Path('./path/to/new_cpp_project'),
    settings=settings,
)
```
