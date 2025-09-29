from __future__ import annotations

__all__ = [
    "generate_attrs",
    "generate_dataclass",
    "generate_pydantic_dataclass",
    "protocol_model",
]

import dataclasses
from typing import TYPE_CHECKING, dataclass_transform, get_type_hints

import attrs
import pydantic.dataclasses

if TYPE_CHECKING:
    from collections.abc import Callable


@dataclass_transform()
def protocol_model[T](cls: type[T]) -> type[T]:
    return cls


def _strip_protocol_to_class[**P, R](protocol: Callable[P, R], /) -> type[object]:
    annotations = get_type_hints(protocol)
    namespace = {"__annotations__": annotations}
    return type(f"{protocol.__name__}", (), namespace)


def _cast_to_callable[**P, R](
    _typ: Callable[P, R], val: type[object], /
) -> Callable[P, R]:
    return val  # type: ignore


def generate_dataclass[**P, R](protocol: Callable[P, R], /) -> Callable[P, R]:
    cls = _strip_protocol_to_class(protocol)
    generated_class = dataclasses.dataclass(cls)
    return _cast_to_callable(protocol, generated_class)


def generate_pydantic_dataclass[**P, R](protocol: Callable[P, R], /) -> Callable[P, R]:
    cls = _strip_protocol_to_class(protocol)
    generated_class = pydantic.dataclasses.dataclass(cls)
    return _cast_to_callable(protocol, generated_class)


def generate_attrs[**P, R](protocol: Callable[P, R], /) -> Callable[P, R]:
    cls = _strip_protocol_to_class(protocol)
    generated_class = attrs.define(cls)
    return _cast_to_callable(protocol, generated_class)
