"""
given a matrix that is sorted row-wise and column-wise
return the number of negative numbers
"""

import numpy as np
array = np.array([[-3, -2, -1, 1],
                  [-2, 2, 3, 4],
                  [4, 5, 7, 8]])

#try 1:
#O(n*m)
def negs1(array):
    limit = len(array[0])
    count = 0
    for row in array:
        for index, elem in enumerate(row[0:limit]):
            if elem < 0:
                count += 1
            else:
                limit = index
                break
    return count

#try 2:
#O(n+m)
def negs2(array):
    step = array.shape[1]
    count = 0
    for row in array:
        for i in reversed(range(step)):
            if row[i] < 0:
                step = i + 1
                count += step
                break
        else:
            break
    return count
