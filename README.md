==== Code Quality Exercise ====

Install setup:
Visual Studio Code
Install VSCode plugins pylint and pylance
Install conda with python 3.9
Setup an environment named 'vector'
Activate your environment
Install mypy, pytest, pylint, and isort with pip


Task:
Define a Vector class that can be instantiated with a list of numeric values.

It should support the following functions:
- random access of elements
- iterable
- printable

And mathematical operations:
- addition (of vectors)
- subtraction (of vectors)
- multiplication (by vector or scalar)
- division (by vector or scalar)
- dot product (with the @ operator)
- raising to power
- concatenation (of vectors)

In subsequent iterations the class should be:
- Commented with proper docstrings
- Use type hints
- Throw meaningful exceptions to prevent misuse
- Have pytest unit tests in the 'test' folder


Final step:
When you are finished, run the following commands on your final vector module and
tests: isort, pylint, and mypy. Resolve all remaining issues, make sure pytest
runs fine, and all tests pass without errors.

You are allowed to disable 'invalid-name' in pylint and also add other reasonable disables,
but the number of disabled checks should be kept at a minimum and pylint should give your
modules a 10/10 rating.

During development you can use calculate.py to see if your code works.