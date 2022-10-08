# Clictune bypass


| |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --- |----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CI/CD | [![CI - Test](https://github.com/FlorentClarret/clictune-bypass/actions/workflows/tox.yml/badge.svg)](https://github.com/FlorentClarret/clictune-bypass/actions/workflows/tox.yml)                                                                                                                                                                                                                                                                                                                       |
| Package | [![PyPI - Version](https://img.shields.io/pypi/v/clictune-bypass.svg?logo=pypi&label=PyPI&logoColor=gold)](https://pypi.org/project/clictune-bypass/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/clictune-bypass.svg?logo=python&label=Python&logoColor=gold)](https://pypi.org/project/clictune-bypass/) |
| Meta | [![code style - black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![types - mypy](https://img.shields.io/badge/types-mypy-blue.svg)](https://github.com/python/mypy) [![imports - isort](https://img.shields.io/badge/imports-isort-ef8336.svg)](https://github.com/pycqa/isort) [![License - MIT](https://img.shields.io/badge/license-MIT-9400d3.svg)](https://spdx.org/licenses/)                                                                    |

</div>

clictune-bypass is a very simple open-source Python library to get links protected by [clictune](https://www.clictune.com/).
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
