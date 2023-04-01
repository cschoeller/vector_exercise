"""Simple examples for using the vector class."""

from vector import Vector


def main():
    """Example calculations."""
    # pylint: disable=invalid-name

    x = Vector([1.2, 3.0, 0.5])
    y = Vector([5.8, 2.1, -0.5])

    print(x[0])
    print(list(x))

    # explicit iteration
    try:
        it = iter(x)
        while True:
            v = next(it)
            print(v)
    except StopIteration:
        print("End of iteration")

    z_add = x + y
    print(z_add)

    z_sub = x - y
    print(z_sub)

    z_mul = x * y
    print(z_mul)

    z_div = x / y
    print(z_div)

    z_pow = x**3
    print(z_pow)

    z_cat = x.cat(y)
    print(z_cat)

    z_chain = (x + y) ** 2 + x
    print(z_chain)

    z = x @ y
    print(z)

    print(x * 5)
    print(x / 5.0)


if __name__ == "__main__":
    main()
