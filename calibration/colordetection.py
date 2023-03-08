import numpy as np
import cv2 as cv
import argparse
import json

ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", help = "path to the image")
# args = vars(ap.parse_args())
# load the image


#make readable coordinates
#convert the multiple whitespace to single white space
# coord=' '.join(np.split())

#replace whitespace with comma
# coord=coord.replace(" ",",")

#make a list of it
# lists = json.loads(coord)

# print(lists[0])



# define the list of boundaries
# boundaries = [
# 	([17, 15, 100], [50, 56, 200]),
# 	([86, 31, 4], [220, 88, 50]),
# 	([25, 146, 190], [62, 174, 250]),
# 	([103, 86, 65], [145, 133, 128])
# ]
#
# # loop over the boundaries
# for (lower, upper) in boundaries:
# 	# create NumPy arrays from the boundaries
# 	lower = np.array(lower, dtype = "uint8")
# 	upper = np.array(upper, dtype = "uint8")
# 	# find the colors within the specified boundaries and apply
# 	# the mask
# 	mask = cv.inRange(image, lower, upper)
# 	output = cv.bitwise_and(image, image, mask = mask)
# 	print(np.hstack([image, output]))
# 	# show the images
# 	cv.imshow("images", np.hstack([image, output]))
# 	cv.waitKey(1000)

def color_detection(file_location):
    image = cv.imread(file_location)

    lower_red = np.array([0,5,193])  # BGR-code of your lowest red
    upper_red = np.array([27,87,247])   # BGR-code of your highest red
    mask = cv.inRange(image, lower_red, upper_red)
    #get all non zero values
    coords=cv.findNonZero(mask)
    output = cv.bitwise_and(image, image, mask = mask)


    coords = coords.tolist()
    newCoords = []
    for c in coords:
        newCoords.append(c[0])

    center = [sum(c)/len(c) for c in zip(*newCoords)]
    cv.circle(output, (int(center[0]), int(center[1])), 3, [0, 255, 0], 3)

    # show the images
    cv.imshow("images", np.hstack([image, output]))

    if cv.waitKey(0) & 0xff == 27:
        cv.destryAllWindows()
