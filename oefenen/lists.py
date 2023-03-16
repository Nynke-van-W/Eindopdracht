import numpy as np

# 2d array to list
arr_2 = np.array([[0, 0], [2, 0], [1, 0], [4, 1], [4, 0],
                  [0, 1], [1, 1], [2, 1], [3, 1], [3, 0],
                  [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]])
list_2 = arr_2.tolist()
sortedlist = sorted(list_2 , key=lambda k: [k[1], k[0]])
print(f'List: {sortedlist}')

# Creating an empty dictionary
dicts = {}
keys = range(len(sortedlist))
values = sortedlist

for y in range(3):
        for i in range(5):
                if i < 4 and y < 2:
                        point = values[(y * 5 + i)]
                        point2 = values[(y*5 + i +6)]
                        dicts[(i, y)] = point, point2

print(dicts)

