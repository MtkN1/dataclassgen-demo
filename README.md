# dataclassgen-demo

これは Python で抽象データモデルから具象データモデルを生成することが実現可能かを実験するワークスペースです。

**抽象データモデル**

抽象データモデルは `typing.Protocol` を使用して定義されます。

抽象データモデルはインスタンス化できませんが、属性の型アノテーションを持ちます。

**具象データモデル**

具象データモデルは標準ライブラリの `dataclasses.dataclass` のように振る舞います。

つまりインスタンス化可能であり、属性の型アノテーションを持ちます。

`dataclassgen.generate_*` 関数らを使用して、抽象データモデルから具象データモデルを生成します。

生成できる具象データモデルは標準の `dataclasses`, また外部ライブラリである `pydantic.dataclasses` や `attrs` のモデルをサポートすることを目指します。

このモジュールの API は完全に型安全である必要があります。

## ユースケース

このモジュールがない場合、抽象データモデルと具象データモデルを手動で定義する必要があります:

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

このモジュールを使用すると、抽象データモデルを定義し、具象データモデルを生成することができます:

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
