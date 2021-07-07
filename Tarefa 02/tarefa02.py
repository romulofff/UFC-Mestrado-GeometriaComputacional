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
    return sum(z)


def norma(x):
    z = 0
    for i in range(len(x)):
        z += x[i]**2
    return math.sqrt(z)


def distancia(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]-y[i])
    return norma(z)


def angulo(x, y):
    return math.acos(prodescalar(x, y)/(norma(x)*norma(y)))*(180/math.pi)


print(somavetorial([0, 2, 3], [1, 2, 0]))
print(multescalar(2, [1, 1]))
print(prodescalar([1, 2, 3], [3, 2, 1]))
print(norma([1, 2]))
print(distancia([3, 3], [0, 0]))
print(angulo([2, -4, -1], [0, 5, 2]))
