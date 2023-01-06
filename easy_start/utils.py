from pathlib import Path
from case_transform import transform, CaseStyle
import dataclasses
import argparse
import types


PATH_TO_STATIC_DATA: Path = (Path(__file__).parent / 'static' / 'project_templates').resolve()


def convert_dataclass_to_dict(dataclass) -> dict:
    assert dataclasses.is_dataclass(dataclass)

    return dataclasses.asdict(dataclass)


def is_trivial_class(cls) -> bool:
    return type(cls) == type


def is_missing(field: dataclasses.Field) -> bool:
    return isinstance(field, dataclasses._MISSING_TYPE)


def add_arguments_from_dataclass(parser: argparse.ArgumentParser, dataclass):
    assert dataclasses.is_dataclass(dataclass) and is_trivial_class(dataclass)

    for field_name, field in dataclass.__dataclass_fields__.items():
        kwargs = {}

        if not is_missing(field.default):
            kwargs['default'] = field.default

        kwargs['required'] = 'default' not in kwargs

        if not is_missing(field.type):
            if is_trivial_class(field.type):
                kwargs['type'] = field.type
            elif isinstance(field.type, types.GenericAlias) and field.type.__origin__ in [list, tuple]:
                kwargs['nargs'] = '+'
                value_type, = field.type.__args__
                if is_trivial_class(value_type):
                    kwargs['type'] = value_type

        parser.add_argument(
            '--' + transform(field_name, from_style=CaseStyle.SNAKE_CASE, to_style=CaseStyle.KEBAB_CASE),
            dest=field_name,
            **kwargs
        )


def create_dataclass_from_argument_parser(
    dataclass,
    parsed_arguments: argparse.Namespace,
    skip_unexpected_arguments=True,
    skip_none=True
):
    assert dataclasses.is_dataclass(dataclass) and is_trivial_class(dataclass)

    dataclass_arguments = {
        key: value
        for key, value in parsed_arguments.__dict__.items()
        if all([
            not skip_unexpected_arguments or key in key in dataclass.__annotations__,
            not skip_none or value is not None,
        ])
    }

    return dataclass(**dataclass_arguments)
