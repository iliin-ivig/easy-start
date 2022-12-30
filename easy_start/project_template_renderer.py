from easy_start.utils import render_string

from pathlib import Path
import jinja2


class ProjectTemplateRenderer:
    def __init__(self, path_to_project_template: Path, path_to_project: Path):
        assert path_to_project_template.exists()

        self.destination = path_to_project
        self.jinja_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(path_to_project_template),
            trim_blocks=True,
            lstrip_blocks=True,
        )

    def list_templates(self) -> list[str]:
        return self.jinja_env.list_templates()

    def render(self, templates: str | list[str], **settings):
        templates = [templates] if isinstance(templates, str) else templates

        for template in templates:
            filepath = self.destination / render_string(template, **settings)
            filecontent = self.jinja_env.get_template(template).render(**settings)

            filepath.parent.mkdir(exist_ok=True, parents=True)
            filepath.write_text(filecontent)
