import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text(encoding="UTF-8")

setup(
    name="clictune_bypass",
    version="0.0.1",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/florentclarret/clictune-bypass",
    project_urls={
        "Changelog": "https://github.com/FlorentClarret/clictune-bypass/blob/main/CHANGELOG.md"
    },
    author="Florent Clarret",
    author_email="florent.clarret@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "clictune_bypass": ["py.typed"],
    },
    install_requires=[
        "beautifulsoup4==4.11.1",
        "requests==2.28.1",
    ],
)
