import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from tarefa02.gcrf import Gcrf, Point

gc = Gcrf()


# def jarvis(points):
#     if len(points) < 3:
#         return []

#     points = sorted(points)

#     convex_hull = [points[0]]

#     current = None
#     while True:
#         current = points[0]
#         for point in points[1:]:
#             if current == convex_hull[-1] or \
#                 between(convex_hull[-1], current, point) or \
#                     gc.antiHorario([convex_hull[-1], current, point]):
#                 current = point

#         if current == convex_hull[0]:
#             break

#         convex_hull.append(current)

#     return convex_hull
points = []
with open("sample_poly.bin", 'r') as f:
    for line in f.readlines():
        l = eval(line)
        print(l)
        points.append(Point(l[0], l[1], l[2]))
print(points[0])
gc.plotSegment(points, True)
