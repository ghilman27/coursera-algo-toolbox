# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def sort_by_left_end(segments):
    return sorted(segments)


def optimal_points(segments):
    segments = sort_by_left_end(segments)
    points = []
    if len(segments) == 1:
        return segments[0].end

    point_start = segments[0].start
    point_end = segments[0].end
    for s in segments[1:]:
        if s.start > point_start and s.start > point_end:
            points.append(point_end)
            point_start = s.start
            point_end = s.end
        if s.start > point_start and s.start <= point_end:
            point_start = s.start
        if s.end < point_end:
            point_end = s.end
    points.append(point_end)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

