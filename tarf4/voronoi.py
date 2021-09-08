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


def voronoi(points, shape=(600, 600)):
    depthmap = np.ones(shape, np.float)*1e308
    colormap = np.zeros(shape, np.int)

    def hypot(X, Y):
        return (X-x)**2 + (Y-y)**2

    for i in range(len(points)):
        x = points[i].x
        y = points[i].y
        paraboloid = np.fromfunction(hypot, shape)
        colormap = np.where(paraboloid < depthmap, i+1, colormap)
        depthmap = np.where(paraboloid <
                            depthmap, paraboloid, depthmap)

    for p in points:
        x = p.x
        y = p.y
        colormap[x-1:x+2, y-1:y+2] = 0

    return colormap


def draw_map(colormap):
    shape = colormap.shape

    # Colors
    palette = np.array([
        0x000000FF,
        0xFF0000FF,
        0x00FF00FF,
        0xFFFF00FF,
        0x0000FFFF,
        0xFF00FFFF,
        0x00FFFFFF,
        0xFFFFFFFF,
        0xFFDDDCCA,
    ])

    colormap = np.transpose(colormap)
    pixels = np.empty(colormap.shape+(4,), np.int8)

    pixels[:, :, 3] = palette[colormap] & 0xFF
    pixels[:, :, 2] = (palette[colormap] >> 8) & 0xFF
    pixels[:, :, 1] = (palette[colormap] >> 16) & 0xFF
    pixels[:, :, 0] = (palette[colormap] >> 24) & 0xFF

    image = Image.frombytes("RGBA", shape, pixels)
    image.save('voronoi.png')


if __name__ == '__main__':
    # draw_map(voronoi(([100,300], [200,500], [300,200], [400,500], [500,300], [200,300])))
    draw_map(voronoi((Point(100, 300, 0), Point(200, 500, 0), Point(
        300, 200, 0), Point(400, 500, 0), Point(500, 300, 0), Point(200, 300, 0))))
#     draw_map(voronoi(([100,100],[356,301],[400,65],[324,145],
# [200,399])))
