# Introduction

This is a typed Python project starter template. It showcases:

- How to set up linting + typechecking on CI and pre-commits
- How to use `mypy` with the strictest settings available as of this writing
- How to use the `Ok | Err` ADTs with pattern matching

  Note: you can do away with the `assert_never`s once exhaustive pattern matching is implemented on `mypy`.

# Setup

```
pip install poetry
poetry shell
poetry install
```

# Running

```
poetry run main
```
