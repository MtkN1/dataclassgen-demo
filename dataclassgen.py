from __future__ import annotations

__all__ = [
    "generate_attrs",
    "generate_dataclass",
    "generate_pydantic_dataclass",
    "protocol_model",
]

from collections.abc import Callable
from typing import TYPE_CHECKING, dataclass_transform

if TYPE_CHECKING:
    from collections.abc import Callable


@dataclass_transform()
def protocol_model[T](cls: type[T]) -> type[T]:
    raise NotImplementedError


def generate_dataclass[**P, R](protocol: Callable[P, R], /) -> Callable[P, R]:
    raise NotImplementedError


def generate_pydantic_dataclass[**P, R](protocol: Callable[P, R], /) -> Callable[P, R]:
    raise NotImplementedError


def generate_attrs[**P, R](protocol: Callable[P, R], /) -> Callable[P, R]:
    raise NotImplementedError
