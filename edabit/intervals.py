def count_overlapping(intervals, point):
    tup = (min(x)<=point<=max(x) for x in intervals)
    print(tup)
    print(sum(tup))

count_overlapping([[1,2],[2,3],[3,4],[2,4]], 2)