![ci](https://github.com/QMSS-G5072-2026/weather_huang_sabrina/actions/workflows/ci-cd.yml/badge.svg)

# weather_srh2206

This is for hw07 and I'll be using three functions from last week's weather exercise and turn it into a python package.

## Installation

```bash
$ uv add weather_srh2206
```

or, without uv, `pip install weather_srh2206`.

## Development

```bash
$ uv sync                       # create .venv and install the package with its dev and docs groups
$ uv run pytest                 # run the tests
$ uv run make html -C docs      # build the documentation
$ uv build                      # build the sdist and wheel into dist/
```

## Usage

```python
import weather_srh2206

weather_srh2206.celsius_to_fahrenheit(100)  # 212.0
weather_srh2206.summarize_temperatures([10.0, 20.0, float("nan")])
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`weather_srh2206` was created by Sabrina Huang. It is licensed under the terms of the MIT license.

## Credits

`weather_srh2206` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `qmss-pkgs-cookiecutter` [template](https://github.com/QMSS-G5072-2026/qmss-pkgs-cookiecutter), a uv-based fork of [`py-pkgs-cookiecutter`](https://github.com/py-pkgs/py-pkgs-cookiecutter).
