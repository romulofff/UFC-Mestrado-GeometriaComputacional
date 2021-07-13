import math
from typing import List

import matplotlib.pyplot as plt
import numpy as np


class Point():
    """Data structure of a point."""

    def __init__(self, x, y, z=0) -> None:
        """Point object

        Args:
            x (float): x coordinate of point
            y (float): y coordinate of point
        """
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        if self.z == 0:
            return 2
        else:
            return 3

    def __call__(self) -> tuple:
        return (self.x, self.y)

    def __str__(self) -> str:
        return str((self.x, self.y))

    def to_numpy(self):
        return np.array([self.x, self.y])


class Gcrf():

    def genPoly(self, n):
        xn = np.random.random(n)
        yn = np.random.random(n)
        z = zip(xn, yn)
        z = [Point(x, y) for x, y in z]
        z = np.array(z)
        angles = [self.anguloOrientado(i) for i in z]
        indexes = np.argsort(angles)
        z = z[indexes]
        z = z.tolist()

        return z

    def somavetorial(self, a, b):
        if isinstance(a, Point):
            return Point(a.x+b.x, a.y+b.y, a.z+b.z)
        z = []
        for i in range(len(a)):
            z.append(a[i]+b[i])
        return z

    def subtrvetorial(self, a, b):
        if isinstance(a, Point):
            return Point(a.x-b.x, a.y-b.y, a.z-b.z)
        z = []
        for i in range(len(a)):
            z.append(a[i]-b[i])
        return z

    def multescalar(self, lamb: int, x: list) -> list:
        # if isinstance(a, Point):
        #     return Point(a.x*lamb, a.y*lamb, a.z*lamb)
        z = []
        for i in range(len(x)):
            z.append(lamb*x[i])
        return z

    def prodescalar(self, a, b):
        res = []
        for i in range(len(a)):
            res.append(a[i]*b[i])
        return sum(res)

    def norma(self, x):
        z = 0
        for i in range(len(x)):
            z += x[i]**2
        return math.sqrt(z)

    def distancia(self, x, y):
        """Returns the distance between vectors x and y.

        Args:
            x (list): list containing points from vector x.
            y (list): list containing points from vector y.

        Returns:
            [float]: [the distance between vectors x and y]
        """
        z = []
        for i in range(len(x)):
            z.append(x[i]-y[i])
        return self.norma(z)

    def angulo(self, x, y, degrees=False):
        """Returns the angle between vectors x and y.

        Args:
            x (list): list containing points from vector x.
            y (list): list containing points from vector y.
            degrees (bool): if the result should be in degrees or radians, defaults to False.
        Returns:
            float: the angle between the two vectors
        """

        if not degrees:
            return math.acos(self.prodescalar(x, y)/(self.norma(x)*self.norma(y)))
        return math.acos(self.prodescalar(x, y)/(self.norma(x)*self.norma(y)))*(180/math.pi)

    def anguloOrientado(self, x, degrees=False):
        if isinstance(x, Point):
            x = x()
        mult = 1
        if x[1] < 0:
            mult = -1
        if not degrees:
            return mult*math.acos(x[0]/self.norma(x))
        return mult*math.acos(x[0]/self.norma(x))*(180/math.pi)

    def pseudoAnguloCosseno(self, x, y, degrees=False):
        if not degrees:
            return 1-(self.prodescalar(x, y)/(self.norma(x)*self.norma(y)))
        return (1-(self.prodescalar(x, y)/(self.norma(x)*self.norma(y))))*(180/math.pi)

    def pseudoAnguloOrientado(self, x):
        if isinstance(x, Point):
            x = x()
        if x[1] >= 0:
            if x[0] >= 0:
                if x[0] >= x[1]:
                    return x[1]/x[0]
                return 2-(x[0]/x[1])
            if -x[0] <= x[1]:
                return 2+(-x[0]/x[1])
            return 4-(x[1]/-x[0])
        if x[0] < 0:
            if -x[0] >= -x[1]:
                return 4+(-x[1]/-x[0])
            return 6-(-x[0]/-x[1])
        if x[0] <= -x[1]:
            return 6+(x[0]/-x[1])
        return 8-(-x[1]/x[0])

    def pseudoAngulo2(self, x, y):
        return self.pseudoAnguloOrientado(x)-self.pseudoAnguloOrientado(y)

    def prodvetorial(self, x, y):
        if len(x) == 2:
            return x[0]*y[1]-x[1]*y[0]
        return [x[1]*y[2]-x[2]*y[2], x[2]*y[0]-x[0]*y[2], x[0]*y[1]-x[1]*y[0]]

    def intersect(self, a, b, c, d):
        ab = self.subtrvetorial(b, a)
        ac = self.subtrvetorial(c, a)
        ad = self.subtrvetorial(d, a)
        ca = self.subtrvetorial(a, c)
        cb = self.subtrvetorial(b, c)
        cd = self.subtrvetorial(d, c)

        # r1 = self.prodvetorial(ab, ac)*self.prodvetorial(ab, ad)
        r1 = self.prodvetorial(ab, ac)*self.prodvetorial(ab, ad) < 0
        # r2 = self.prodvetorial(cd, ca)*self.prodvetorial(cd, cb)
        r2 = self.prodvetorial(cd, ca)*self.prodvetorial(cd, cb) < 0
        # return (r1, r2), r1 < 0 and r2 < 0
        return r1 and r2

    def area(self, x, y):
        if len(x) == 2:
            return abs(self.prodvetorial(x, y))
        return self.norma(self.prodvetorial(x, y))

    def antiHorario(self, listaDePontos):
        res = 0
        for i in range(len(listaDePontos)-1):
            res += self.prodvetorial(listaDePontos[i], listaDePontos[i+1])
        res += self.prodvetorial(listaDePontos[0], listaDePontos[-1])
        return 0.5*res > 0

    def slope(self, p1: Point, p2: Point):
        return (p2.y - p1.y) / (p2.x - p1.x)

    def pip(self, p: Point, poly) -> bool:
        """ Determine if the point is in the polygon.

        Args:
            p -- a object of type Point(x, y)
            poly -- a list of tuples [(x, y), (x, y), ...]

        Returns:
            True if the point is in the path or is a corner or on the boundary"""

        num = len(poly)
        j = num - 1
        result = False
        for i in range(len(poly)):
            if (p.x == poly[i].x) and (p.y == poly[i].y):
                return True
            if ((poly[i].y > p.y) != (poly[j].y > p.y)):
                slope = self.slope(p, poly[i])
                if slope == 0:
                    return True
                if (slope < 0) != (poly[j].y < poly[i].y):
                    result = not result
            j = i
        return result

    def starPolygon(self, points, jumps):
        i = 0
        starredPolygon = []
        while i < jumps:
            for j in range(i, len(points), jumps):
                # print("Ponto adicionado j:",points[j]())
                starredPolygon.append(points[j])
            # print("Ponto adicionado i:",points[i]())
            starredPolygon.append(points[i])
            i += 1
        return starredPolygon

    def centeroidnp(self, points):
        length = len(points)
        tipoPoints = type(points[0])

        if tipoPoints == tuple:
            arr = np.array(points)
        elif tipoPoints == Point:
            arr = np.array([p.to_numpy() for p in points])

        sum_x = np.sum(arr[:, 0])
        sum_y = np.sum(arr[:, 1])
        return sum_x/length, sum_y/length

    def plotPolygon(self, points, annotate=False):
        """Plot polygon from list of points

        Args:
            points (Point): list of Point objects indicating the polygon vertices
        """

        points.append(points[0])
        if type(points[0]) == Point:
            points = [p() for p in points]
        x, y = zip(*points)
        plt.grid(0.5)
        plt.plot(x, y, '-o')
        if annotate:
            plt.text(x[0], y[0], "p1")
            plt.text(x[1], y[1], "p2")
            plt.text(x[2], y[2], "p3")
        plt.show()

    def plotSegment(self, segments: List[Point]) -> None:
        for segment in segments:
            segx = [p.x for p in segment]
            segy = [p.y for p in segment]
            plt.plot(segx, segy)
        plt.show()

    def rotationIndex(self, p: Point, poly: list):
        # NOT WORKING
        j = len(poly)-1
        rotIndex = 0
        for i in range(len(poly)):
            ppi = self.subtrvetorial(p, poly[j])
            ppi1 = self.subtrvetorial(p, poly[i])
            rotIndex += self.pseudoAngulo2(ppi, ppi1)
            j = i
        rotIndex *= 1/(2*math.pi)
        if rotIndex == 0:
            return False
        if abs(rotIndex) == 1:
            return True
        return rotIndex


if __name__ == '__main__':

    gc = Gcrf()

    # poly = gc.genPoly(9)
    # gc.plotPolygon(poly)
    print("Operações entre vetores:")
    a = [0, 2, 3]
    b = [1, 2, 0]
    print("Soma entre os vetores {} e {}: ".format(a, b), gc.somavetorial(a, b))
    print("Subtração entre os vetores {} e {}: ".format(
        a, b), gc.subtrvetorial(a, b))
    a = [15, 25]
    b = 2
    print("Multiplicando o vetor {} pelo escalar {}: ".format(
        a, b), gc.multescalar(b, a))
    a = [1, 2, 3]
    b = [3, 2, 1]
    print("Produto escalar entre {} e {}:".format(a, b), gc.prodescalar(a, b))
    a = [1, 2]
    print("Norma do vetor {}:".format(a), gc.norma([1, 2]))
    a = [3, 3]
    b = [0, 0]
    print("Distância de {} para {}: ".format(
        a, b), gc.distancia([3, 3], [0, 0]))
    a = [2, -4, -1]
    b = [0, 5, 2]
    print("Ângulo entre os vetores {} e {} em radianos:".format(
        a, b), gc.angulo(a, b))
    print("Ângulo entre os vetores {} e {} em graus:".format(
        a, b), gc.angulo(a, b, True))
    print(gc.anguloOrientado([0, 1]))
    print(gc.anguloOrientado([0, -1]))
    print(gc.pseudoAnguloCosseno([2, -4, -1], [0, 5, 2]))
    print(gc.pseudoAnguloCosseno([1, 0], [0, 1], False))
    print(gc.pseudoAnguloOrientado([10, 5]))
    a = [1, 0, 0]
    b = [0, 1, 0]
    print("Produto vetorial entre {} e {}:".format(a, b), gc.prodvetorial(a, b))
    a = [10, 0, 5]
    b = [0, 5, 0]
    print("Produto vetorial entre {} e {}:".format(a, b), gc.prodvetorial(a, b))
    a = [1, 0]
    b = [0, 1]
    print("Produto vetorial entre {} e {}:".format(a, b), gc.prodvetorial(a, b))
    a = [10, 0]
    b = [0, 5]
    print("Produto vetorial entre {} e {}:".format(a, b), gc.prodvetorial(a, b))

    # print(gc.prodescalar([1, 2], [2, 1]))
    # print(gc.pseudoAngulo2([1, 0], [0, 1]))

    a = (1, 1)
    b = (1, -1)
    print("Se o pseudo-ângulo for positivo {} está à esquerda de {}:".format(a, b),
          gc.pseudoAngulo2(a, b))
    print("Se o pseudo-ângulo for positivo {} está à esquerda de {}:".format(a, b),
          gc.pseudoAngulo2(b, a))

    print("Interseção dos segmentos de retas: ",
          gc.intersect((0, 0), (2, 2), (0, 1), (2, 1)))
    gc.plotSegment([[Point(0, 0), Point(2, 2)], [Point(0, 1), Point(2, 1)]])

    print("Interseção dos segmentos de retas: ",
          gc.intersect((0, 0), (2, 2), (0, 6), (9, -3)))
    gc.plotSegment([[Point(0, 0), Point(2, 2)], [Point(0, 6), Point(9, -3)]])

    print("Interseção dos segmentos de retas: ",
          gc.intersect((0, -2), (6, 4), (0, 6), (9, -3)))
    gc.plotSegment([[Point(0, -2), Point(6, 4)], [Point(0, 6), Point(9, -3)]])

    print("O polígono {} é Anti-horário:".format(
        [(0, 0), (0, 1), (2, 0)]), gc.antiHorario([(0, 0), (0, 1), (2, 0)]))
    gc.plotPolygon([(0, 0), (0, 1), (2, 0)], True)
    print("O polígono {} é Anti-horário:".format(
        [(0, 0), (2, 0), (0, 1)]), gc.antiHorario([(0, 0), (2, 0), (0, 1)]))
    gc.plotPolygon([(0, 0), (2, 0), (0, 1)], True)

    a = (0, 1)
    b = (2, 0)
    print("Área no R2, se > 0, o ângulo é orientado de {} para {}:".format(
        a, b), gc.area(a, b))

    a = (0, 1, 3)
    b = (2, 0, 4)
    print("Área no R3, se > 0, o ângulo é orientado de {} para {}:".format(
        a, b), gc.area(a, b))

    pip = gc.pip(Point(0, 0), [Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])
    print("Point in Polygon:", pip)
    if pip:
        plt.scatter(0, 0, c='g')
    else: 
        plt.scatter(0, 0, c='r')
    gc.plotPolygon([Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])


    pip = gc.pip(Point(2, 2), [Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])
    print("Point in Polygon:", pip)
    if pip:
        plt.scatter(2, 2, c='g')
    else: 
        plt.scatter(2, 2, c='r')
    gc.plotPolygon([Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])

    a = np.random.random(1) 
    b = np.random.random(1)
    poly = gc.genPoly(6)
    pip = gc.pip(Point(a, b), poly)
    print("Point in Polygon:", pip)
    if pip:
        plt.scatter(a, b, c='g')
    else: 
        plt.scatter(a, b, c='r')
    gc.plotPolygon(poly)


    ################################################################################
    # Ponto no polígono usando índice de rotação não está funcionando.

    # print("Point in Polygon - Rotation Index:", gc.rotationIndex(Point(0, 0), [
    #       Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)]))
    # plt.scatter(0, 0, c='g')
    # gc.plotPolygon([Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])

    # print("Point in Polygon - Rotation Index:", gc.rotationIndex(Point(2, 2), [
    #       Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)]))
    # plt.scatter(2, 2, c='g')
    # gc.plotPolygon([Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)])
    ################################################################################


    poly = [Point(-1, 1), Point(1, 1), Point(3, 1),
            Point(4, 2), Point(2.5, 3), Point(1.5, 3.5),
            Point(1.5, 5), Point(-1.5, 5), Point(-0.8, 3.5), Point(-2, 2)]

    starredPoly = gc.starPolygon(poly, 2)

    cx, cy = gc.centeroidnp(starredPoly)
    print("Centroid:", (cx, cy))
    print("Centroid in polygon:", gc.pip(Point(cx, cy), starredPoly))
    plt.grid(0.5)
    plt.scatter(cx, cy, c='g')
    gc.plotPolygon(starredPoly)

    starredPoly = gc.starPolygon(poly, 4)

    cx, cy = gc.centeroidnp(starredPoly)
    print("Centroid:", (cx, cy))
    print("Centroid in polygon:", gc.pip(Point(cx, cy), starredPoly))
    plt.grid(0.5)
    plt.scatter(cx, cy, c='g')
    gc.plotPolygon(starredPoly)

    starredPoly = gc.starPolygon(gc.genPoly(10), 4)

    cx, cy = gc.centeroidnp(starredPoly)
    print("Centroid:", (cx, cy))
    print("Centroid in polygon:", gc.pip(Point(cx, cy), starredPoly))
    plt.grid(0.5)
    plt.scatter(cx, cy, c='g')
    gc.plotPolygon(starredPoly)
