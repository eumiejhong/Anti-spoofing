#Usage
# python gather_examples.py --input videos/--.mov --output training/--.mov


# import the necessary package from imutils.video import VideoStream
import imutils
import numpy as np
import argparse
import cv2
import os
import os.path

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", type=str, required=True,
	help="path to input video")
ap.add_argument("-o", "--output", type=str, required=True,
	help="path to output directory of cropped faces")
args = vars(ap.parse_args())


vs = cv2.VideoCapture(args["input"])
currentframe = 0

while(True):
    #reading from frame
    ret, frame = vs.read()

    if ret:
        name = "output" + str(currentframe) + '.png'
        print ('Creating...' + name)

        fileName = os.path.join(args["output"], name)
        cv2.imwrite(fileName, frame)
        currentframe += 1
    else:
        break

#cleanup
vs.release()
cv2.destroyAllWindows()
