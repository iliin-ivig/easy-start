from easy_start import ProjectTemplateRenderer
from easy_start.utils import PATH_TO_STATIC_DATA, convert_dataclass_to_dict

from pathlib import Path
import dataclasses


@dataclasses.dataclass(kw_only=True)
class PythonPackageSettings:
    package_name: str
    full_package_name: str | None = None
    description: str = 'short package description'
    url: str = 'https://github.com/...'
    requirements: list[str] = dataclasses.field(default_factory=list)
    scripts: list[str] = dataclasses.field(default_factory=list)
    include_static_data: bool = True

    def __post_init__(self):
        if self.full_package_name is None:
            self.full_package_name = self.package_name


def start_python_package(destination: Path, settings: PythonPackageSettings):
    renderer = ProjectTemplateRenderer(
        path_to_project=destination,
        path_to_project_template=(PATH_TO_STATIC_DATA / 'python_package'),
    )

    settings_dict = convert_dataclass_to_dict(settings)

    renderer.render(
        [
            'setup.cfg',
            'README.md',
            'pyproject.toml',
            '.gitignore',
            '{{package_name}}/__init__.py',
        ]
        +
        [
            'MANIFEST.in',
            '{{package_name}}/static/README.md',
        ] if settings.include_static_data else [],
        **settings_dict,
    )
