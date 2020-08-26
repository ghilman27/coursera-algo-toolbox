# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    starts.sort()
    ends.sort()
    sorted_points = sorted([(point, index) for index, point in enumerate(points)])

    start_idx = 0
    end_idx = 0
    n_segments = len(starts)
    n_segments_active = 0

    for point, point_idx in sorted_points:
        # scan by opening a segment, 
        # if a segment's starting point <= our point value
        # it means that segment is active
        # so add that to n_segments_active
        while start_idx < n_segments and starts[start_idx] <= point:
            start_idx += 1
            n_segments_active += 1
            
        # now there are n segments active
        # but we can't assure if these n segments still active
        # (reach our point before its closing point)
        # so if we found the segment's closing point that is smaller
        # than our point value, it means that particular segment 
        # is closed before reaching our point
        # it also means, that segment not contains our point
        # so subtract that segment from n_segment_active
        while end_idx < n_segments and ends[end_idx] < point:
            end_idx += 1
            n_segments_active -= 1
        
        # now we know how many segments active within our point's reach
        # (n_segment_active), that is the number of segment that contains
        # our point. So append that to cnt
        cnt[point_idx] = n_segments_active

    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
