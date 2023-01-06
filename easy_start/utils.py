from pathlib import Path
from case_transform import transform, CaseStyle
import dataclasses
import argparse
import types


PATH_TO_PROJECT_TEMPLATES: Path = (Path(__file__).parent / 'static' / 'project_templates').resolve()


def convert_dataclass_to_dict(dataclass) -> dict:
    assert dataclasses.is_dataclass(dataclass)

    return dataclasses.asdict(dataclass)
