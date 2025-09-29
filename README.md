# dataclassgen-demo

This workspace experiments with whether it is feasible to generate concrete data models from abstract data models in Python.

Abstract data models are declared using `typing.Protocol` and describe the required attributes and their types without being instantiable.

Concrete data models behave like the standard library `dataclasses.dataclass`: they are instantiable and expose the same attribute type annotations.

The `dataclassgen.generate_*` family of functions produces concrete data models from an abstract model.
The goal is to support generating models compatible with the standard `dataclasses`, as well as external libraries such as `pydantic.dataclasses` and `attrs`.

APIs provided by this module are intended to be fully type safe.

## Use case

Without this module, you must define both an abstract model and concrete implementations manually:

```python
import dataclasses
import pydantic
from typing import Protocol


class User(Protocol):
    name: str


@dataclasses.dataclass
class UserDataClass:
    name: str


@pydantic.dataclasses.dataclass
class UserPydantic:
    name: str


def process_user(user: User) -> None:
    pass


user_dataclass = UserDataClass(name="Alice")
user_pydantic = UserPydantic(name="Bob")

process_user(user_dataclass)
process_user(user_pydantic)
```

With this module, you define the abstract model once and generate concrete models programmatically:

```python
import dataclassgen
from typing import Protocol


@dataclassgen.protocol_model
class User(Protocol):
    name: str


UserDataClass = dataclassgen.generate_dataclass(User)
UserPydantic = dataclassgen.generate_pydantic_dataclass(User)


def process_user(user: User) -> None:
    pass


user_dataclass = UserDataClass(name="Alice")
user_pydantic = UserPydantic(name="Bob")

process_user(user_dataclass)
process_user(user_pydantic)
```
