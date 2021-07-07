import math


def somavetorial(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]+y[i])
    return z


def multescalar(lamb: int, x: list) -> list:
    z = []
    for i in range(len(x)):
        z.append(lamb*x[i])
    return z


def prodescalar(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]*y[i])
    return z


def norma(x):
    z = 0
    for i in range(len(x)):
        z += x[i]**2
    return math.sqrt(z)


print(somavetorial([0, 2, 3], [1, 2, 0]))
print(multescalar(2, [1, 1]))
print(prodescalar([1, 2, 3], [3, 2, 1]))
print(norma([1, 2]))
