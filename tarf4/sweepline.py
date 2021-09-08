import os
import math
import time
from typing import List

import numpy as np
import matplotlib.pyplot as plt

from shapely.geometry import Polygon

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
        if math.isclose(self.x,p.x) and math.isclose(self.y,p.y) and math.isclose(self.z, p.z):
            return True
        return False
            
        
class Edge:
    def __init__(self, p1, p2, visits=0):
        if p1.point_is_close(p2):
            raise Exception("Edge must have two different points. Points given: {} and {}.".format(p1, p2))
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

        self.spoly = Polygon([[p1.x,p1.y,p1.z],[p2.x,p2.y,p2.z],[p3.x,p3.y,p3.z]])
    def __str__(self):
        return "{} {} {}".format(str(self.p1), str(self.p2), str(self.p3))

    def __eq__(self, other):
        if self.p1.point_is_close(other.p1) or self.p1.point_is_close(other.p2) or self.p1.point_is_close(other.p3):
            if self.p2.point_is_close(other.p1) or self.p2.point_is_close(other.p2) or self.p2.point_is_close(other.p3):
                if self.p3.point_is_close(other.p1) or self.p3.point_is_close(other.p2) or self.p3.point_is_close(other.p3):
                    return True
        return False

def plotSegment(segments: List[Point], threeD=False) -> None:
        if threeD:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

        for segment in segments:
            segx = [p.x for p in segment]
            segy = [p.y for p in segment]
            if threeD:
                segz = [p.z for p in segment]
                ax.plot(segx, segy, segz)
            else:
                plt.plot(segx, segy)
        plt.show()


def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)


def sort_points_per_x(points):
    xs = []
    for p in points:
        xs.append(p.x)
    indexes = np.argsort(xs)
    points = np.array(points)
    points = points[indexes]
    return points.tolist()


def check_edge_intersection(edge, segments):
    if len(segments) < 1:
        return False
    for seg in segments:
        A = seg.p1
        B = seg.p2
        C = edge.p1
        D = edge.p2
        if intersect(A,B,C,D):
            return True
        else:
            return False


def sweep_line(points):
    points = sort_points_per_x(points)
    segments = []
    for i in range(len(points)-1):
        for j in range(i):
            new_edge = Edge(points[i], points[j])
            if not check_edge_intersection(new_edge, segments):
                segments.append(new_edge)
    
    return segments
            
    
if __name__ == '__main__':
    points = [Point(1, 3, 0), Point(2, 5, 0), Point(3, 2, 0), Point(4, 5, 0), Point(5, 3, 0)]
    segments = sweep_line(points)
    for seg in segments:
        print(seg)