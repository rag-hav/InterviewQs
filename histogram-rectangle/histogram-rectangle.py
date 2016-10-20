# given a histogram
# find the largest area rectangle in the histogram
# https://www.youtube.com/watch?v=VNbkzsnllsU

# test histograms
a = [1, 3, 5, 3, 0, 2, 6, 6, 1, 0, 3, 6]
    # answer should be area 12
b = [1, 3, 5, 3, 2, 2, 3, 3, 1, 0, 3, 6]
    # answer should be area 14

def rectangle(histogram):
    positions = []
    values = []
    best = 0
    for pos, val in enumerate(histogram):
        if len(positions) == 0 and len(values) == 0:
            positions.append(pos)
            values.append(val)
        elif val > values[-1]:
            positions.append(pos)
            values.append(val)
        elif val == values[-1]:
            pass
        else:
            size = values.pop() * (pos - positions[-1])
            if size > best:
                best = size
            while values and val < values[-1]:
                positions.pop()
                size = values.pop() * (pos - positions[-1])
                if size > best:
                    best = size
            if values and val == values[-1]:
                positions.pop()
            elif values and val > values[-1]:
                values.append(val)
            else:
                positions = []

    l = len(histogram)
    for pos, val in zip(positions, values):
        size = val * (l - pos)
        if size > best:
            best = size
    return best


"""
NOTES
process for a

positions push 0
values push 1
[0], [1], 0

positions push 1
values push 3

[0, 1], [1, 3], 0
positions push 2
values push 5
[0, 1, 2], [1, 3, 5], 0

while 3 is less than values[-1]:
    evaluate size:
        value[-1] * curr-pos[-1] = 5*1 = 5
        if > best, store in best. best = 5
    values pop !!
    [0, 1, 2], [1, 3]
    if value[-1] is 3:
        positions pop
        [0, 1], [1, 3]
    else:
        values push 3
[0, 1], [1, 3], 5

0 is less than 3 and 1:
    size_3 = 3 * (4 - 1) = 9. best = 9



a = [1, 3, 5, 3, 0, 2, 6, 6, 1, 0, 3, 6]
"""
