coords = {
    (0,0): [(0, 0), (100, 100)],
    (1,0): [(100, 100), (200, 200)]
}


punt = [109, 190]

for key in coords:
    if coords[key][0][0] <= punt[0] <= coords[key][1][0] and coords[key][0][1] <= punt[1] <= coords[key][1][1]:
        print(f"Punt is in gebied: {key}")
