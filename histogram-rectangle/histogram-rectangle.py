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
