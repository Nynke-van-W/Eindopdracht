import calibration.colordetection as cd
import cv2 as cv
import numpy as np

#cd.color_detection("./calibration/bloemen.jpeg")

coords = {
    (0,0): [(0, 0), (100, 100)],
    (1,0): [(100, 100), (200, 200)]
}
punt = [109, 190]

for key in coords:
    if coords[key][0][0] <= punt[0] <= coords[key][1][0] and coords[key][0][1] <= punt[1] <= coords[key][1][1]:
        print(f"Punt is in gebied: {key}")

vid = cv.VideoCapture(0)
newCoords = []
while (True):
    ret, frame = vid.read()
    # cv.imshow('frame', frame)

    upper_red = np.array([77,108,219])  # BGR-code of your lowest red
    lower_red = np.array([53,77,182])   # BGR-code of your highest red
    mask = cv.inRange(frame, lower_red, upper_red)
    # get all non zero values
    coords = cv.findNonZero(mask)
    output = cv.bitwise_and(frame, frame, mask=mask)

    if coords is not None:
        coords = coords.tolist()
        for c in coords:
            newCoords.append(c[0])

        center = [sum(c) / len(c) for c in zip(*newCoords)]
        cv.circle(output, (int(center[0]), int(center[1])), 3, [0, 255, 0], 3)
        print(center)
    # show the images
    cv.imshow("images", np.hstack([frame, output]))
    cv.waitKey(1000)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break