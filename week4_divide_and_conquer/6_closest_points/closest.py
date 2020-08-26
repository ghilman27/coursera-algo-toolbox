#Uses python3
import sys
import math
from collections import namedtuple
# from test import test

"""
THIS IS A VERY COMPLICATED PROBLEM
best explanation so far: https://www.youtube.com/watch?v=0W_m46Q4qMc&t=340s
"""


MAX_INPUT = 10000
ISENG = 0

sys.setrecursionlimit(MAX_INPUT)
Point = namedtuple('Point', 'x y')


def distance_2d(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)


def brute_min_distance(points, n):
    min_dist = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            dist = distance_2d(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist


# Strip is defined as a region between
# [mid_point.x - D] and [mid_point.x + D]
# where D is the minimum distance on left and right partition
# left partition | right partition
#           |    |    |
#              D    D
# we want to find the minimum inter partition distance
# and compare it with D --> min(D, interpartitiondistance)
def find_strip(points, mid_point, d, n):
    strip = []
    for point in points:
        if abs(point.x - mid_point.x) < d:
            strip.append(point)
    return strip


# -KEY POINT-
# because for every point in this iteration, we only compare 
# to max another 7 points (see the theorem proof!)
# the time complexity of this loop is not O(n^2)
# we don't have to specify which point is from the left or from the right
# because, if p1 and p2 are from the same partition
# their distance will be equal or more than d
# so it will not be picked as min_dist
def compute_min_dist_strip(points, mid_point, d, n):
    strip = find_strip(points, mid_point, d, n)
    min_dist = d
    strip.sort(key=lambda point: point.y)
    for p1_idx in range(len(strip)):
        p2_idx = p1_idx + 1
        while p2_idx < len(strip) and (strip[p2_idx].y - strip[p1_idx].y) < d:
            min_dist = min(min_dist, distance_2d(strip[p1_idx], strip[p2_idx]))
            p2_idx += 1
    return min_dist


def min_dist(points, n):
    if n <= 3:
        return brute_min_distance(points, n)
    
    mid = n // 2
    left_dist = min_dist(points[:mid], mid)
    right_dist = min_dist(points[mid:], n-mid)

    min_dist_both = min(left_dist, right_dist)
    min_dist_strip = compute_min_dist_strip(points, points[mid], min_dist_both, n)

    return min(min_dist_both, min_dist_strip)


def minimum_distance(points, n):
    if n<=1:
        return "Need minimum of two points"
    return min_dist(sorted(points), n)


if __name__ == '__main__':
    # test(minimum_distance, brute_min_distance)
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list(map(lambda d: Point(d[0], d[1]), zip(x, y)))
    print("{0:.9f}".format(minimum_distance(points, n)))
