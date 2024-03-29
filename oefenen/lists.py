import numpy as np

# 2d array to list
arr_2 = np.array([[0, 0], [2, 0], [1, 0], [4, 1], [4, 0],
                  [0, 1], [1, 1], [2, 1], [3, 1], [3, 0],
                  [0, 2], [1, 2], [2, 2], [3, 2], [4, 2]])
list_2 = arr_2.tolist()
print(list_2)
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

leuk = [[237, 311], [239, 271], [241, 232], [243, 193], [245, 154], [247, 116], [249, 78], [277, 312], [279, 272], [281, 232], [283, 193], [284, 155], [286, 116], [287, 78], [318, 314], [320, 273], [321, 233], [322, 194], [324, 155], [325, 117], [326, 78], [358, 314], [360, 274], [361, 234], [362, 195], [363, 156], [364, 117], [366, 78], [400, 315], [401, 275], [402, 195], [402, 235], [403, 156], [404, 117], [405, 78], [441, 316], [442, 235], [442, 275], [443, 195], [444, 156], [445, 116], [446, 78], [484, 235], [484, 276], [484, 317], [485, 155], [485, 195], [486, 77], [486, 116], [527, 155], [527, 195], [527, 236], [527, 277], [527, 318], [528, 76], [528, 115], [570, 75], [570, 115], [570, 155], [570, 195], [570, 236], [570, 277], [570, 319]]

oneliner_corners = [[round(x/10)*10 for x in c] for c in leuk]
sortedlist2 = sorted(oneliner_corners , key=lambda k: [k[0], k[1]])
print(f'List: {sortedlist2}')