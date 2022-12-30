from pathlib import Path
import dataclasses
import jinja2


PATH_TO_STATIC_DATA: Path = (Path(__file__).parent / 'static' / 'project_templates').resolve()


def render_string(string: str, **kwargs):
    return jinja2.Template(string).render(**kwargs)


def convert_dataclass_to_dict(dataclass) -> dict:
    assert dataclasses.is_dataclass(dataclass)

    return dataclasses.asdict(dataclass)
