# Spylizard - your sparselizard python bindings

Build instructions:

1. sudo apt-get install pybind11 (should become available in /usr/include/pybind11)
1. sudo apt-get install python3.10-dev
1. Clone sparselizard and sparselizard-users in the same folder
1. Build sparselizard with cmake as usual
1. Build sparselizard-users/api/python with cmake as usual
1. pip install .

To update the stubs: (could be added to cmake later)
1. cd into api/python
1. pip install pybind11-stubgen
1. pybind11-stubgen --no-setup-py --root-module-suffix stubs -o package spylizard

---

Interactive python test run in the terminal:

```bash
ipython3
> from spylizard import *
> printversion()
> expr = array3x1(1,2,3)
> expr.print()
```
