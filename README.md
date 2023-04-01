## Clean Coding Exercise

### Install setup
Use Visual Studio Code (VS) and install the pylint and pylance plugins for support during the exercise. Also install `conda` for managing a virtual environment. Then run the following commands to install and use the environment:

```
conda create --name vector python=3.9 -y
conda activate vector
pip install -r requirements.txt
```

### Task
Define a `Vector` class that can be instantiated with a list of numeric values.

It should support the following functions:
- random access of elements
- iterable
- printable

And mathematical operations:
- addition (of vectors)
- subtraction (of vectors)
- multiplication (with vector or scalar)
- division (by vector or scalar)
- dot product (with the @ operator)
- raising to power
- concatenation (of vectors)

In subsequent iterations the class should be:
- commented with proper docstrings
- use type hints
- throw meaningful exceptions to prevent misuse
- have appropriate pytest unit tests in the 'test' folder

### Final step
When you are finished, run the following commands on your final vector and test modules:
`isort`, `pylint`, and `mypy`. Resolve all remaining issues, make sure `pytest` runs fine,
and all tests pass without errors. You can also run `black` on your files to automatically
resolve formatting errors.

You are allowed to disable 'invalid-name' in `pylint` and also add other reasonable disables,
but the number of disabled checks should be kept at a minimum and `pylint` should give your
modules a 10/10 rating.

During development you can run `usage_examples.py` to see if your code works.
