import numpy as np

# 2d array to list
arr_2 = np.array([[0, 0], [2, 0], [1, 0], [4, 1], [4, 0], [0, 1], [1, 1], [2, 1], [3, 1], [3, 0]])
list_2 = arr_2.tolist()
sortedlist = sorted(list_2 , key=lambda k: [k[1], k[0]])

print(f'List: {sortedlist}')

# Creating an empty dictionary
dicts = {}
keys = range(len(sortedlist))
values = sortedlist
for y in range(2):
        for i in range(5):
                dicts[(i, y)] = values[y*5 + i]

print(dicts)