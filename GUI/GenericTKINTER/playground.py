def add(*args):
    totes = 0
    for n in args:
        totes += n
        print(totes)
    return totes

print(add(1, 2, 5))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs.get("multiply")
    print(n)




calculate(2, add=3, multiply=5)

