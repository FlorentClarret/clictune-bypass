# Clictune bypass
|         |                                                                                                                                                                                                       |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CI/CD   | [![CI - Test][tox-badge]][tox-workflow] [![pre-commit.ci status][pre-commit-badge]][pre-commit-result]                                                                                                |
| Package | [![PyPI - Version][pypi-badge]][pypi-website] [![PyPI - Python Version][pypi-version]][pypi-website]                                                                                                  |
| Meta    | [![code style - black][black-badge]][black-website] [![types - mypy][mypy-badge]][mypy-website] [![imports - isort][isort-badge]][isort-website] [![License - MIT][license-badge]][license-website]   |
| Misc    | [![Mergify Status][mergify-badge]][mergify-website]                                                                                                                                                   |

clictune-bypass is a very simple open-source Python library to get links protected by [clictune][clictune-website].
## Install

``` shell
pip install clictune-bypass
```

## Usage

```python
from clictune_bypass import get_url

link = get_url("https://www.mylink1.biz/bypass")

print(link)
```

# Contributing guide

Glad you want to help! To do so, you can read our [Contributing guide](CONTRIBUTING.md).

[clictune-website]: https://www.clictune.com/
[black-website]: https://github.com/psf/black
[black-badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[tox-badge]: https://github.com/FlorentClarret/clictune-bypass/actions/workflows/tox.yml/badge.svg
[tox-workflow]: https://github.com/FlorentClarret/clictune-bypass/actions/workflows/tox.yml
[pre-commit-badge]: https://results.pre-commit.ci/badge/github/FlorentClarret/clictune-bypass/main.svg
[pre-commit-result]: https://results.pre-commit.ci/latest/github/FlorentClarret/clictune-bypass/main
[pypi-badge]: https://img.shields.io/pypi/v/clictune-bypass.svg?logo=pypi&label=PyPI&logoColor=gold
[pypi-website]: https://pypi.org/project/clictune-bypass/
[pypi-version]: https://img.shields.io/pypi/pyversions/clictune-bypass.svg?logo=python&label=Python&logoColor=gold
[mypy-badge]: https://img.shields.io/badge/types-mypy-blue.svg
[mypy-website]: https://github.com/python/mypy
[isort-badge]: https://img.shields.io/badge/imports-isort-ef8336.svg
[isort-website]: https://github.com/pycqa/isort
[license-badge]: https://img.shields.io/badge/license-MIT-9400d3.svg
[license-website]: https://spdx.org/licenses/
[mergify-badge]: https://img.shields.io/endpoint.svg?url=https://api.mergify.com/v1/badges/FlorentClarret/clictune-bypass&style=flat
[mergify-website]: https://mergify.com