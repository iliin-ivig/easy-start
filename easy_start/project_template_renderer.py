from case_transform import transform, CaseStyle

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

        self.jinja_env.filters['camelcase'] = lambda s: transform(s, to_style=CaseStyle.CAMEL_CASE)
        self.jinja_env.filters['snakecase'] = lambda s: transform(s, to_style=CaseStyle.SNAKE_CASE)
        self.jinja_env.filters['kebabcase'] = lambda s: transform(s, to_style=CaseStyle.KEBAB_CASE)
        self.jinja_env.filters['uppercamelcase'] = lambda s: transform(s, to_style=CaseStyle.UPPER_CAMEL_CASE)
        self.jinja_env.filters['uppersnakecase'] = lambda s: transform(s, to_style=CaseStyle.UPPER_SNAKE_CASE)
        self.jinja_env.filters['upperkebabcase'] = lambda s: transform(s, to_style=CaseStyle.UPPER_KEBAB_CASE)

    def list_templates(self) -> list[str]:
        return self.jinja_env.list_templates()

    def render(self, templates: str | list[str], **settings):
        templates = [templates] if isinstance(templates, str) else templates

        for template in templates:
            filepath = self.destination / self.jinja_env.from_string(template).render(**settings)
            filecontent = self.jinja_env.get_template(template).render(**settings)

            filepath.parent.mkdir(exist_ok=True, parents=True)
            filepath.write_text(filecontent)
