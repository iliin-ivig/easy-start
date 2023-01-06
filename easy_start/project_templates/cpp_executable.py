from easy_start.project_template_renderer import ProjectTemplateRenderer
from easy_start.utils import PATH_TO_PROJECT_TEMPLATES, convert_dataclass_to_dict

from pathlib import Path
import dataclasses


@dataclasses.dataclass(kw_only=True)
class CppExecutableSettings:
    project_name: str
    project_short_name: str | None = None
    description: str = 'short package description'
    url: str = 'https://github.com/...'
    requirements: list[str] = dataclasses.field(default_factory=list)
    executables: list[str] = dataclasses.field(default_factory=lambda: ['run'])
    source_folder: str = 'src'
    bin_folder: str = 'bin'

    def __post_init__(self):
        if self.project_short_name is None:
            self.project_short_name = self.project_name


def start_cpp_executable(destination: Path, settings: CppExecutableSettings):
    renderer = ProjectTemplateRenderer(
        path_to_project=destination,
        path_to_project_template=(PATH_TO_PROJECT_TEMPLATES / 'cpp_executable'),
    )

    settings_dict = convert_dataclass_to_dict(settings)

    renderer.render(
        [
            '.gitignore',
            'README.md',
            'CMakeLists.txt',
            'CMakePresets.json',
            'conanfile.txt',
            '{{source_folder}}/{{project_short_name}}/utils/print.cpp',
            '{{source_folder}}/{{project_short_name}}/utils/print.h',
            '{{source_folder}}/{{project_short_name}}/utils/print.hpp',
        ]
        ,
        **settings_dict,
    )

    for executable in settings.executables:
        renderer.render(
            '{{source_folder}}/{{project_short_name}}/Main{{executable | uppercamelcase}}.cpp',
            executable=executable,
            **settings_dict,
        )

    return renderer
