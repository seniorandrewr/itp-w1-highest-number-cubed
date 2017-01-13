"""This is the entry point of the program."""


def highest_number_cubed(limit):
    x = 0
    z = 0
    while x < limit:
        z = x ** 3
        x += 1
        if z > limit:
            return x - 2