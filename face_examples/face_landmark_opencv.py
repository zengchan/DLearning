# coding=utf-8
import sys
import os
import dlib
import glob
import cv2
'''
# 初始化dlib人脸检测器
detector = dlib.get_frontal_face_detector()

# 初始化显示窗口
win = dlib.image_window()
# opencv加载视频文件
cap = cv2.VideoCapture('/home/zchan/dlib-19.15/python_examples/test.mp4')
#cap = cv2.VideoCapture(0)
while cap.isOpened():

    ret, cv_img = cap.read()
    if cv_img is None:
        break
    img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    dets = detector(img, 0)

    print("Number of faces detected: {}".format(len(dets)))
    for i, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            i, d.left(), d.top(), d.right(), d.bottom()))

    win.clear_overlay()
    win.set_image(img)
    win.add_overlay(dets)

cap.release()
'''

'''
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('/home/zchan/dlib-19.15/python_examples/test.mp4')

# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    cv2.imshow('Frame',frame)

    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

  # Break the loop
  else: 
    break

# When everything done, release the video capture object
cap.release()

# Closes all the frames
#cv2.destroyAllWindows()
'''

predictor_path='./shape_predictor_68_face_landmarks.dat'
# 初始化dlib人脸检测器
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)
# 初始化显示窗口
win = dlib.image_window()
# opencv加载视频文件
cap = cv2.VideoCapture('/home/zchan/dlib-19.15/python_examples/test.mp4')
#cap = cv2.VideoCapture(0)
while cap.isOpened():

    ret, cv_img = cap.read()
    if cv_img is None:
        break
    img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    dets = detector(img, 1)
    win.clear_overlay()
    win.set_image(img)
    for k, d in enumerate(dets):
        print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            k, d.left(), d.top(), d.right(), d.bottom()))
        # Get the landmarks/parts for the face in box d.
        shape = predictor(img, d)
        print("Part 0: {}, Part 1: {} ...".format(shape.part(0),
                                                  shape.part(1)))
        # Draw the face landmarks on the screen.
        #win.clear_overlay()
        #win.add_overlay(img)
        win.add_overlay(shape)
        win.add_overlay(dets)
cap.release()



