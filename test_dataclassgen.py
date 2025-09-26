from __future__ import annotations

from dataclasses import is_dataclass
from typing import Protocol

import attrs
from pydantic.dataclasses import is_pydantic_dataclass

from dataclassgen import (
    generate_attrs,
    generate_dataclass,
    generate_pydantic_dataclass,
    protocol_model,
)


@protocol_model
class UserProtocol(Protocol):
    name: str
    age: int


def process_user(user: UserProtocol) -> UserProtocol:
    return user


def test_generate_dataclass() -> None:
    User = generate_dataclass(UserProtocol)
    user = User(name="Alice", age=30)

    process_user(user)

    assert (user.name, user.age) == ("Alice", 30)
    assert is_dataclass(User)


def test_generate_pydantic_dataclass() -> None:
    User = generate_pydantic_dataclass(UserProtocol)
    user = User(name="Alice", age=30)

    process_user(user)

    assert (user.name, user.age) == ("Alice", 30)
    # > "FunctionType" is not assignable to "type[Any]"
    # assert is_pydantic_dataclass(User)
    assert is_pydantic_dataclass(type(user))


def test_generate_attrs() -> None:
    User = generate_attrs(UserProtocol)
    user = User(name="Alice", age=30)

    process_user(user)

    assert (user.name, user.age) == ("Alice", 30)
    # > "FunctionType" is not assignable to "type"
    # assert attrs.has(User)
    assert attrs.has(type(user))
