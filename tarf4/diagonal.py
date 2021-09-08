import math
import os
import time
from typing import List

import numpy as np
from PIL import Image


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.adj_edges = []

    def __call__(self) -> tuple:
        return (self.x, self.y, self.z)

    def __str__(self) -> str:
        return str((self.x, self.y, self.z))

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def add_adj_edge(self, edge):
        self.adj_edges.append(edge)

    def point_is_close(self, p):
        if math.isclose(self.x, p.x) and math.isclose(self.y, p.y) and math.isclose(self.z, p.z):
            return True
        return False


class Edge:
    def __init__(self, p1, p2, visits=0):
        if p1.point_is_close(p2):
            raise Exception(
                "Edge must have two different points. Points given: {} and {}.".format(p1, p2))
        self.p1 = p1
        self.p2 = p2
        self.visits = visits
        p1.add_adj_edge(self)
        p2.add_adj_edge(self)

    def __str__(self):
        return "{} {}".format(str(self.p1), str(self.p2))

    def __eq__(self, other):
        if self.p1 == other.p1 or self.p1 == other.p2:
            if self.p2 == other.p1 or self.p2 == other.p2:
                return True
        return False


class Face():
    def __init__(self, p1, p2, p3):
        # super().__init__(self)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        self.e1 = Edge(p1, p2)
        self.e2 = Edge(p2, p3)
        self.e3 = Edge(p3, p1)

    def __str__(self):
        return "{} {} {}".format(str(self.p1), str(self.p2), str(self.p3))

    def __eq__(self, other):
        if self.p1.point_is_close(other.p1) or self.p1.point_is_close(other.p2) or self.p1.point_is_close(other.p3):
            if self.p2.point_is_close(other.p1) or self.p2.point_is_close(other.p2) or self.p2.point_is_close(other.p3):
                if self.p3.point_is_close(other.p1) or self.p3.point_is_close(other.p2) or self.p3.point_is_close(other.p3):
                    return True
        return False


def diag_in_hull(diag, hull):
    return True

def add_edge_to_hull(edge, hull):
    pass

def diagonal_triangulation(hull):
    first_point = hull[0]

    for i in range(len(hull)-1):
        diag = Edge(hull[1], hull[i])
        if diag_in_hull(diag, hull):
            hull = add_edge_to_hull(diag, hull)
            # ITERATE RECURSIVELY ON DOMAIN
