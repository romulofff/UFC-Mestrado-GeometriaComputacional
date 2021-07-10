import math


class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Gcrf():

    def somavetorial(self, x, y):
        z = []
        for i in range(len(x)):
            z.append(x[i]+y[i])
        return z

    def subtrvetorial(self, x, y):
        z = []
        for i in range(len(x)):
            z.append(x[i]-y[i])
        return z

    def multescalar(self, lamb: int, x: list) -> list:
        z = []
        for i in range(len(x)):
            z.append(lamb*x[i])
        return z

    def prodescalar(self, x, y):
        z = []
        for i in range(len(x)):
            z.append(x[i]*y[i])
        return sum(z)

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
        # print("PSEUDOS", self.pseudoAnguloOrientado(
            # x), self.pseudoAnguloOrientado(y))
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

        r1 = self.prodvetorial(ab, ac)*self.prodvetorial(ab, ad)
        # r1 = self.prodvetorial(ab, ac)*self.prodvetorial(ab, ad) < 0
        r2 = self.prodvetorial(cd, ca)*self.prodvetorial(cd, cb)
        # r2 = self.prodvetorial(cd, ca)*self.prodvetorial(cd, cb) < 0
        return (r1, r2), r1 < 0 and r2 < 0

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
            x -- The x coordinates of point.
            y -- The y coordinates of point.
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


    def rotationIndex(self, p: Point, poly: list):
        j = len(poly)-1
        rotIndex = 0
        for i in range(len(poly)):
            ppi = self.subtrvetorial(p, poly[j])
            ppi1 = self.subtrvetorial(p, poly[i])
            print("ppi:", ppi, "pppi1", ppi1)
            rotIndex += self.pseudoAngulo2(ppi, ppi1)
            print("rotIndex",rotIndex)
            j = i
        # print(rotIndex)

        rotIndex *= 1/(2*math.pi)
        print(rotIndex)
        if rotIndex == 0:
            return False
        if abs(rotIndex) == 1:
            return True
        return rotIndex




if __name__ == '__main__':

    gc = Gcrf()

    print(gc.somavetorial([0, 2, 3], [1, 2, 0]))
    print(gc.multescalar(2, [1, 1]))
    print(gc.prodescalar([1, 2, 3], [3, 2, 1]))
    print(gc.norma([1, 2]))
    print(gc.distancia([3, 3], [0, 0]))
    print(gc.angulo([2, -4, -1], [0, 5, 2]))
    print(gc.anguloOrientado([0, 1]))
    print(gc.anguloOrientado([0, -1]))
    print(gc.pseudoAnguloCosseno([2, -4, -1], [0, 5, 2]))
    print(gc.pseudoAnguloCosseno([1, 0], [0, 1], False))
    print(gc.pseudoAnguloOrientado([10, 5]))
    print(gc.prodvetorial([1, 0, 0], [0, 1, 0]))
    print(gc.prodvetorial([1, 0], [0, 1]))

    print(gc.prodescalar([1, 2], [2, 1]))
    print(gc.pseudoAngulo2([1, 0], [0, 1]))

    print("Se positivo a está a esquerda de b:",
          gc.pseudoAngulo2([1, 1], [1, -1]))
    print("Se positivo a está a esquerda de b:",
          gc.pseudoAngulo2([1, -1], [1, 1]))

    print("Interseção dos segmentos de retas: ",
          gc.intersect((0, 0), (2, 2), (0, 1), (2, 1)))
    print("Interseção dos segmentos de retas: ",
          gc.intersect((0, 0), (2, 2), (0, 1), (2, 1)))
    print("Interseção dos segmentos de retas: ",
          gc.intersect((0, 0), (2, 2), (0, 6), (9, -3)))
    print("Interseção dos segmentos de retas: ",
          gc.intersect((0, -2), (6, 4), (0, 6), (9, -3)))

    print(gc.antiHorario([(0, 0), (0, 1), (2, 0)]))
    print(gc.antiHorario([(0, 0), (2, 0), (0, 1)]))
    print(gc.area((0, 1), (2, 0)))
    print(gc.area((0, 1, 3), (2, 0, 4)))

    print("PIP:", gc.pip(Point(0, 0), [
          Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)]))
    print("PIP:", gc.pip(Point(2, 2), [
          Point(-1, 1), Point(1, 1), Point(1, -1), Point(-1, -1)]))
    print("PIP:", gc.rotationIndex((0, 0), [
          (-2, 2), (2, 2), (2, -2), (-2, -2)]))
    # print("PIP:", gc.rotationIndex((2, 2), [
    #       (-1, 1), (1, 1), (1, -1), (-1, -1)]))
