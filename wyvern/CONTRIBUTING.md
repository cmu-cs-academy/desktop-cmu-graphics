# Contributing

## Prerequisites

- [Rust](https://rustup.rs/)
- [uv](https://docs.astral.sh/uv/)

## Setup

Build and install the package in development mode:

```
uv run maturin develop
```

## Running

```
uv run python test.py
```

After making changes to the Rust code, re-run `uv run maturin develop` before running again.
