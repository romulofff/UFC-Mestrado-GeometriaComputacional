import math
from typing import List

import matplotlib.pyplot as plt
import numpy as np

from gcrf import Gcrf, Point


if __name__ == '__main__':

    gc = Gcrf()

    # # poly = gc.genPoly(9)
    # # gc.plotPolygon(poly)
    # print("Operações entre vetores:")
    # a = [0, 2, 3]
    # b = [1, 2, 0]
    # print("Soma entre os vetores {} e {}: ".format(a, b), gc.somavetorial(a, b))
    # print("Subtração entre os vetores {} e {}: ".format(
    #     a, b), gc.subtrvetorial(a, b))
    # a = [15, 25]
    # b = 2
    # print("Multiplicando o vetor {} pelo escalar {}: ".format(
    #     a, b), gc.multescalar(b, a))
    # a = [1, 2, 3]
    # b = [3, 2, 1]
    # print("Produto escalar entre {} e {}:".format(a, b), gc.prodescalar(a, b))
    # a = [1, 2]
    # print("Norma do vetor {}:".format(a), gc.norma([1, 2]))
    # a = [3, 3]
    # b = [0, 0]
    # print("Distância de {} para {}: ".format(
    #     a, b), gc.distancia([3, 3], [0, 0]))
    # a = [2, -4, -1]
    # b = [0, 5, 2]
    # print("Ângulo entre os vetores {} e {} em radianos:".format(
    #     a, b), gc.angulo(a, b))
    # print("Ângulo entre os vetores {} e {} em graus:".format(
    #     a, b), gc.angulo(a, b, True))
    # print(gc.anguloOrientado([0, 1]))
    # print(gc.anguloOrientado([0, -1]))
    # print(gc.pseudoAnguloCosseno([2, -4, -1], [0, 5, 2]))
    # print(gc.pseudoAnguloCosseno([1, 0], [0, 1], False))
    # print(gc.pseudoAnguloOrientado([10, 5]))
    # a = [1, 0, 0]
    # b = [0, 1, 0]
    # print("Produto vetorial entre {} e {}:".format(a, b), gc.prodvetorial(a, b))
    # a = [10, 0, 5]
    # b = [0, 5, 0]
    # print("Produto vetorial entre {} e {}:".format(a, b), gc.prodvetorial(a, b))
    # a = [1, 0]
    # b = [0, 1]
    # print("Produto vetorial entre {} e {}:".format(a, b), gc.prodvetorial(a, b))
    # a = [10, 0]
    # b = [0, 5]
    # print("Produto vetorial entre {} e {}:".format(a, b), gc.prodvetorial(a, b))

    # # print(gc.prodescalar([1, 2], [2, 1]))
    # # print(gc.pseudoAngulo2([1, 0], [0, 1]))

    # a = (1, 1)
    # b = (1, -1)
    # print("Se o pseudo-ângulo for positivo {} está à esquerda de {}:".format(b, a),
    #       gc.pseudoAngulo2(a, b))
    # print("Se o pseudo-ângulo for positivo {} está à esquerda de {}:".format(a, b),
    #       gc.pseudoAngulo2(b, a))

    # print("Interseção dos segmentos de retas: ",
    #       gc.intersect((0, 0), (2, 2), (0, 1), (2, 1)))
    # gc.plotSegment([[Point(0, 0), Point(2, 2)], [Point(0, 1), Point(2, 1)]])

    # print("Interseção dos segmentos de retas: ",
    #       gc.intersect((0, 0), (2, 2), (0, 6), (9, -3)))
    # gc.plotSegment([[Point(0, 0), Point(2, 2)], [Point(0, 6), Point(9, -3)]])

    # print("Interseção dos segmentos de retas: ",
    #       gc.intersect((0, -2), (6, 4), (0, 6), (9, -3)))
    # gc.plotSegment([[Point(0, -2), Point(6, 4)], [Point(0, 6), Point(9, -3)]])

    # print("O polígono {} é Anti-horário:".format(
    #     [(0, 0), (0, 1), (2, 0)]), gc.antiHorario([(0, 0), (0, 1), (2, 0)]))
    # gc.plotPolygon([(0, 0), (0, 1), (2, 0)], True)
    # print("O polígono {} é Anti-horário:".format(
    #     [(0, 0), (2, 0), (0, 1)]), gc.antiHorario([(0, 0), (2, 0), (0, 1)]))
    # gc.plotPolygon([(0, 0), (2, 0), (0, 1)], True)

    # a = (0, 1)
    # b = (2, 0)
    # print("Área no R2, se > 0, o ângulo é orientado de {} para {}:".format(
    #     a, b), gc.area(a, b))

    # a = (0, 1, 3)
    # b = (2, 0, 4)
    # print("Área no R3, se > 0, o ângulo é orientado de {} para {}:".format(
    #     a, b), gc.area(a, b))

    # pip = gc.pip(Point(0, 0), [Point(-1, 1),
    #              Point(1, 1), Point(1, -1), Point(-1, -1)])
    # print("Point in Polygon:", pip)
    # if pip:
    #     plt.scatter(0, 0, c='g')
    # else:
    #     plt.scatter(0, 0, c='r')
    # gc.plotPolygon([Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])

    # pip = gc.pip(Point(2, 2), [Point(-1, 1),
    #              Point(1, 1), Point(1, -1), Point(-1, -1)])
    # print("Point in Polygon:", pip)
    # if pip:
    #     plt.scatter(2, 2, c='g')
    # else:
    #     plt.scatter(2, 2, c='r')
    # gc.plotPolygon([Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])

    # a = np.random.random(1)
    # b = np.random.random(1)
    # poly = gc.genPoly(6)
    # pip = gc.pip(Point(a, b), poly)
    # print("Point in Polygon:", pip)
    # if pip:
    #     plt.scatter(a, b, c='g')
    # else:
    #     plt.scatter(a, b, c='r')
    # gc.plotPolygon(poly)

    # ################################################################################
    # # Ponto no polígono usando índice de rotação não está funcionando.

    # # print("Point in Polygon - Rotation Index:", gc.rotationIndex(Point(0, 0), [
    # #       Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)]))
    # # plt.scatter(0, 0, c='g')
    # # gc.plotPolygon([Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])

    # # print("Point in Polygon - Rotation Index:", gc.rotationIndex(Point(2, 2), [
    # #       Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)]))
    # # plt.scatter(2, 2, c='g')
    # # gc.plotPolygon([Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])
    # ################################################################################

    # poly = [Point(-1, 1), Point(1, 1), Point(3, 1),
    #         Point(4, 2), Point(2.5, 3), Point(1.5, 3.5),
    #         Point(1.5, 5), Point(-1.5, 5), Point(-0.8, 3.5), Point(-2, 2)]

    # starredPoly = gc.starPolygon(poly, 2)

    # cx, cy = gc.centeroidnp(starredPoly)
    # print("Centroid:", (cx, cy))
    # print("Centroid in polygon:", gc.pip(Point(cx, cy), starredPoly))
    # plt.grid(0.5)
    # plt.scatter(cx, cy, c='g')
    # gc.plotPolygon(starredPoly)

    # starredPoly = gc.starPolygon(poly, 4)

    # cx, cy = gc.centeroidnp(starredPoly)
    # print("Centroid:", (cx, cy))
    # print("Centroid in polygon:", gc.pip(Point(cx, cy), starredPoly))
    # plt.grid(0.5)
    # plt.scatter(cx, cy, c='g')
    # gc.plotPolygon(starredPoly)

    # starredPoly = gc.starPolygon(gc.genPoly(10), 4)

    # cx, cy = gc.centeroidnp(starredPoly)
    # print("Centroid:", (cx, cy))
    # print("Centroid in polygon:", gc.pip(Point(cx, cy), starredPoly))
    # plt.grid(0.5)
    # plt.scatter(cx, cy, c='g')
    # gc.plotPolygon(starredPoly)


    from randomPoly import to_convex_contour
    gc.plotPolygon(to_convex_contour(10))
    # print(to_convex_contour(10))

