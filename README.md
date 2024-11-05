# Multi-Provider Strategy for App Configuration in Python

This repository for showcases a custom, extensible configuration module using the provider pattern in python.

This solution is perfect for scenarios where config data comes from multiple sources. It could be tempting to write utility classes to read data from these sources and call them directly in your business logic. However, this brings the major disadvantage of having our business logic littered with file readers. It's also not extensible.

With the approach in this repository, all of the configuration logic is abstracted away, making it easy to extend without making any changes to your main application code.

## Basic Usage

1. If not already installed, install [Poetry](https://python-poetry.org/docs/).
2. Run `poetry install` to install dependencies.
3. Run the command `poetry run python -m src.app` to test the module.
4. You should see "Alan Turing" in your console!
