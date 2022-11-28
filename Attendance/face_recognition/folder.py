import os
# import argparse
def create(p):
    path = 'C://Users/admin/Desktop/cutomfaces/dataset'
    os.chdir(path)
    Newfolder = p
    os.makedirs(Newfolder)

   
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-c", "--cascade", required=True,
# 	help = "path to where the face cascade resides")
# ap.add_argument("-o", "--output", required=True,
# 	help="path to output directory")
# args = vars(ap.parse_args())

# ENCODE_FACES.PY
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--dataset", required=True,
# 	help="path to input directory of faces + images")
# ap.add_argument("-e", "--encodings", required=True,
# 	help="path to serialized db of facial encodings")
# ap.add_argument("-d", "--detection-method", type=str, default="cnn",
# 	help="face detection model to use: either `hog` or `cnn`")
# args = vars(ap.parse_args())



#facerecognition
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
# ap.add_argument("-e", "--encodings", required=True,
# 	help="path to serialized db of facial encodings")
# ap.add_argument("-o", "--output", type=str,
# 	help="path to output video")
# ap.add_argument("-y", "--display", type=int, default=1,
# 	help="whether or not to display output frame to screen")
# ap.add_argument("-d", "--detection-method", type=str, default="cnn",
# 	help="face detection model to use: either `hog` or `cnn`")
args = vars(ap.parse_args())