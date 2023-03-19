from cgitb import enable

import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils   # type: ignore
mp_drawing_styles = mp.solutions.drawing_styles  # type: ignore
mp_pose = mp.solutions.pose  # type: ignore

# For webcam input:
cap = cv2.VideoCapture("Datasets/Fall Sequences/fall-01-cam0.mp4")

#Fall Detection Variables
fall = False
fall_count = 0
fall_threshold = 10

# Fall Detection
with mp_pose.Pose(
    min_detection_confidence=0.1,
    min_tracking_confidence=0.1) as pose:
  
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      break

    #convert the BGR image to RGB.
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #flip image
    image = cv2.flip(image, 1)
    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = pose.process(image)

    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

    # Fall Detection
    if results.pose_landmarks is not None:
        if results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y > 0.9:
            print(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y)
            print("Fall Detected")
        
    cv2.imshow('MediaPipe Pose', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break