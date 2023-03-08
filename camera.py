import cv2 as cv
import numpy as np

# img = cv.imread(image)
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#
#
# # Find the chess board corners
# ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)
# # If found, add object points, image points (after refining them)
# if ret == True:
#     objpoints.append(objp)
#     corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
#     imgpoints.append(corners)
#
#     # Draw and display the corners
#     cv.drawChessboardCorners(img, chessboardSize, corners2, ret)
#     cv.imshow('img', img)
#     cv.waitKey(1000)

vid = cv.VideoCapture(0)
chessboardSize = (9,7)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
newCoords = []
newCorners = []

while (True):
    ret, frame = vid.read()
    ret, hoeken = vid.read()
    # cv.imshow('frame', frame)

    gray = cv.cvtColor(hoeken, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)
    # If found, add object points, image points (after refining them)

    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)
        corners = corners.tolist()
        for c in corners:
            newCorners.append(c[0])

        print(newCorners)
        # Draw and display the corners
        cv.drawChessboardCorners(hoeken, chessboardSize, corners2, ret)
        cv.imshow('img', hoeken)


    #colordetection
    upper_red = np.array([77, 108, 219])  # BGR-code of your lowest red
    lower_red = np.array([53, 77, 182])  # BGR-code of your highest red
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