# Spylizard - your sparselizard python bindings

Build instructions:

1. sudo apt-get install pybind11-dev (should become available in /usr/include/pybind11)
1. sudo apt-get install python3.10-dev (if your system does not already have it)
1. Clone sparselizard and sparselizard-users in the same folder
1. Build sparselizard with cmake as usual
1. Build sparselizard-users/api/python with cmake as usual
1. pip install .

To update the stubs: (only works if spylizard is already installed with pip)
1. cd into api/python
1. pip install pybind11-stubgen
1. pybind11-stubgen --no-setup-py --root-module-suffix stubs -o package spylizard
1. pip install -I .

---

Interactive python test run in the terminal:

```bash
ipython3
> from spylizard import *
> printversion()
> expr = array3x1(1,2,3)
> expr.print()
```
