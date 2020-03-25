import random


def ReturnRandom(matrix_size):
    a = random.randint(0, matrix_size - 1)
    b = random.randint(0, matrix_size - 1)
    if a != b:
        return [a, b]


# print(ReturnRandom(16))
# (ReturnRandom(15)
