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

vid = cv.VideoCapture(1)
chessboardSize = (9,7)

criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((chessboardSize[0] * chessboardSize[1], 3), np.float32)
objp[:,:2] = np.mgrid[0:chessboardSize[0],0:chessboardSize[1]].T.reshape(-1,2)
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
while (True):
    ret, frame = vid.read()
    cv.imshow('frame', frame)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, corners = cv.findChessboardCorners(gray, chessboardSize, None)
    # If found, add object points, image points (after refining them)

    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)
        print(objpoints)
        # Draw and display the corners
        cv.drawChessboardCorners(frame, chessboardSize, corners2, ret)
        cv.imshow('img', frame)
        cv.waitKey(1000)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break