# Installation
From cloned repo:
```sh
pip3 install path/to/cloned/repo
```

From cloud-based git repository:
```sh
pip3 install git+ssh://git@https://github.com/iliin-ivig/easy-start
```

# Scripts
This package provides the following scripts:

    - `ivig-easy-start`

# Usage
1. CLI:
```sh
ivig-easy-start python-package \
    --package-name easy_start \
    --full-package-name ivig-easy-start \
    --description 'This package helps initialize a project using a parameterized template.' \
    --url 'https://github.com/iliin-ivig/easy-start' \
    --requirements 'Jinja2~=3.1.2' \
    --scripts 'ivig-easy-start' \
    --include-static-data true
```

2. package:
```python
from easy_start.project_templates.python_package import PythonPackageSettings, start_python_package
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

start_python_package(destination=Path('../easy-start'), settings=settings)
```
