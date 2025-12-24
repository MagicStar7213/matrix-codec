# MATH UTILS
![Python](https://img.shields.io/badge/-Python-yellow?style=flat-square&labelColor=blue&logo=python&logoColor=white)

This is a set of tools that allow to check or utilise individual math-related operations. It mainly covers "medium" 12th grade topics such as matrices or geometry (inluding vector theory) but it is planned to include other aspects in the future.

## Usage
The program is divided into modules that cover each topic. Currently, [**Matrices**](mathutils/matrices/README.md) and [**Geometry**](mathutils/geometry/README.md) modules are included. When the main program is run, you will be prompted to choose from several options, and so on until reaching a specific utility. Specifics to each module are specified both in the program and in the module's README.

## Development
Math Utils uses SymPy as backend processor, so **Python>=3.9** and `sympy>=1.14` is needed. It might also work with previous versions but it has not been tested.

To build it, install the `build` package with `pip install --upgrade build`, enter the repository folder and run `python -m build .` to generate a source dist and wheel.