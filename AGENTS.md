This is an experimental workspace.

You need to meet the requirements of [README.md](README.md).

Available tools:

- Python interpreter path: `.venv/bin/python` (Python 3.13)
  - site-packages path (external modules): `.venv/lib/python3.13/site-packages`
- Module name: `dataclassgen`
- Test command: `.venv/bin/pytest test_dataclassgen.py`
- Type check command: `NPM_CONFIG_CACHE=.cache/npm npx -y pyright dataclassgen.py test_dataclassgen.py`
- Typing docs path: `docs/typing.rst`

Rules:

- Always run testing and type checking after editing code.
- DO NOT use `typing.Any` for return types of public APIs.
  - In the internal implementation, `typing.Any` and `typing.cast` can be used.
- If there are clear defects in the test code, you can fix them.
