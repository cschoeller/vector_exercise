## Clean Coding Exercise

This repository contains a coding exercise with a focus on code style and best practices. These are skills rarely taught at university and typically not part of leetcode-like challenges. While this exercise uses Python, many of the ideas transfer to other programming languages.

### Install setup
Use Visual Studio Code (VS) and install the `pylint` and `pylance` plugins for support during the exercise. Also install `conda` for managing a virtual environment. Then run the following commands to install and use the environment:

```
conda create --name vector python=3.9 -y
conda activate vector
pip install -r requirements.txt
```

To enable the plugins for working with your environment press `F1`, type "Select Interpreter" and choose your `vector` environment.

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
- have appropriate unit tests in the 'test' folder

### Final step
When you are finished, run the following commands on your final vector and test modules:
`isort`, `pylint`, and `mypy`. Resolve all remaining issues, make sure `pytest` runs fine,
and all tests pass without errors. You can also run `black` on your files to automatically
resolve formatting errors.

You are allowed to disable 'invalid-name' in `pylint` and also add other reasonable disables,
but the number of disabled checks should be kept at a minimum and `pylint` should give your
modules a 10/10 rating.

During development you can run `usage_examples.py` to see if your code works.
