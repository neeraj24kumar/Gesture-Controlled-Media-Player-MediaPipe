# Gesture-Controlled-Media-Player-MediaPipe
Developed an interface that allows users to control media playback through hand gestures using MediaPipe's hand-tracking capabilities.

The objective of this project is to develop a gesture-controlled media player that allows users to manage media playback through intuitive hand gestures, thereby enhancing the user experience by eliminating the need for traditional input devices such as keyboards and mice. By leveraging computer vision techniques with the MediaPipe library for hand tracking and PyAutoGUI for simulating keyboard actions, the system aims to provide a seamless and interactive interface for media control. Ultimately, this project seeks to demonstrate the potential of gesture recognition technology in creating more accessible and user-friendly applications.

# System Components and Technologies Used: 
- Webcam: A webcam is used to capture the live video feed of the user's hand gestures.  
- Gesture Recognition Algorithm: The system employs a gesture recognition algorithm to analyze the video frames and identify specific hand gestures.  
- Media Player: The media player is responsible for playing, pausing, stopping, and adjusting the volume of media content.  
- Gesture Mapping: The system maps recognized gestures to corresponding media player commands.  
- MediaPipe: A cross-platform framework for building multimodal applied machine learning pipelines 
- PyAutoGUI: A Python module that enables programmatically controlling the mouse and keyboard.

# Project Flow:  
- A fundamental library for scientific computing with Python, used for numerical operations.  
- The project begins by setting up the development environment and installing the required libraries.  
- A Program is coded with the necessary user interface elements, such as gesture patterns.
- The Mediapipe library is used to access the webcam and perform hand gesture recognition. 
- The hand landmarks are extracted using the Mediapipe library, and the relevant gestures are recognized based on the position of the fingers.  
- Once a gesture is recognized, appropriate actions are triggered using PyAutoGUI to control media playback.  
- The NumPy library is utilized for efficient numerical operations and data manipulation if required.  
- The application is tested extensively on different media playback platforms (e.g. Youtube) to ensure proper functionality and usability.

 ![image](https://github.com/user-attachments/assets/4f519fdc-3e9d-45a3-9a4b-86201cb7c35a)
Figure 1: Process Flow

# A. Fingers Recognition 
- The function `count_fingers(lst)` receives a list of hand landmarks detected by the MediaPipe library, where each landmark corresponds to a specific point on the hand.
- A counter variable `cnt` is initialized to zero. This will keep track of how many fingers are raised.
- The variable `thresh` is calculated using the y-coordinates of specific landmarks (the wrist and the middle finger). This threshold helps determine if a finger is considered raised based on its position relative to other landmarks.
- The function checks the positions of various landmarks to see if fingers are extended. For each finger (thumb, index, middle, ring), it compares the y-coordinates of the fingertip (tip landmark) and the corresponding base landmark.
- If the difference in their y-coordinates exceeds the threshold (`thresh`), it indicates that the finger is raised, and the counter `cnt` is incremented.
- Additionally, for the thumb, there is an x-coordinate check. If the x-coordinate difference between the thumb tip and base exceeds a certain value (6), it counts as a raised finger.
- After evaluating all relevant landmarks, the function returns the total count of raised fingers (`cnt`).


# B. Hand Landmarks defined by MediaPipe 
Using these hand landmarks, we can define various gestures and link them to their corresponding intended functionalities to control the media player. Coordinates on the screen and the landmarks on the hand are mapped together to generate the desired output. 
In the segmentation image of fingers, the labeling algorithm is applied to mark the regions of the fingers. In the result of the labeling method, the detected regions in which the number of pixels is too small are regarded as noisy regions and discarded. Only the regions of enough sizes are regarded as fingers and remain.

![image](https://github.com/user-attachments/assets/89ea61b2-0470-4b80-9553-0b732a174760)
Figure 2:Hand landmarks - by Mediapipe

With the help of the palm mask, fingers, and the palm can be segmented easily. The part of the hand that is covered by the palm mask is the palm, while the other parts of the hand are the fingers. Based on the count the features of the media are controlled 
e.g.: 
a) If the count of the finger is 1 the media will be forward. 
b) If the count of the finger is 2 the media will be Rewind. 
 
Similarly, the logic for controlling volume and playback is based on counting the number of fingers raised:
- When three fingers are raised (cnt == 3), the code simulates pressing the "up" arrow key using pyautogui.press("up"), which typically increases the volume.
- When four fingers are raised (cnt == 4), it simulates pressing the "down" arrow key with pyautogui.press("down"), which usually decreases the volume.
- When five fingers are raised (cnt == 5), it simulates pressing the space bar using pyautogui.press("space"), which toggles play and pause in most media players.
- When one finger is raised (cnt == 1), it simulates pressing the right arrow key using pyautogui.press("right"), typically used to skip to the next track or fast forward.
- When two fingers are raised (cnt == 2), it simulates pressing the left arrow key with pyautogui.press("left"), which usually goes back to the previous track or rewinds.


# C. Contours defined by MediaPipe
Contours are defined as the line joining all the points along the boundary of an image that has the same intensity. Contours come in handy in shape analysis, finding the size of the object of interest, and object detection.

![image](https://github.com/user-attachments/assets/b190aa20-05a3-49ea-a873-11d18c3b0b39)
![image](https://github.com/user-attachments/assets/ab4f28a3-edf5-4fc3-b35b-1264baf5f6dc)

Figure 3:Contours - by Mediapipe

The project introduces a novel means of media player control via hand gestures, aligning with users' real-world interactions. This intuitive approach offers a seamless and interruption-free experience, eliminating the need for extra devices. Moreover, it expands interaction possibilities by allowing diverse forms of engagement, rather than confining users to a single input point. The process begins with capturing an image, which is subsequently converted into RGB format. The code then proceeds to verify the presence of multiple hands within the image. An empty list serves as a repository for elements representing the detected hand's characteristics. These elements encompass the number of points comprising the hand, derived through the utilization of media pipe technology. 

Note: - Open youtube in split screen and leave the cursor in that video when the code is executed

# A. Play/Pause 
The system has succeeded in getting a hand gesture to pause and detect the action to be performed, so the corresponding video play action is active.
![image](https://github.com/user-attachments/assets/db94c088-96c7-4764-989c-2f4c9b6ccc0c)
Figure 4: Hand Gesture for play / pause


### B. Forward 
The system has succeeded in detecting the hand gesture and detecting the action to be performed, so the corresponding video transfer action (forward seeking) is active.
![image](https://github.com/user-attachments/assets/ab60446d-cab6-46eb-baf1-e2cbb6730eee)
Figure 5:Hand Gesture for forward


C. Rewind 
The system has succeeded in detecting the hand gesture and detecting the action to be performed, so the corresponding video transfer action (backward seeking) is active.

 
Figure 6:Hand Gesture for rewind



D. Volume up 
The system has succeeded in detecting the Volume Up hand touch and detecting the action to be performed, so the corresponding action to increase the video volume is effective

 
Figure 7:Hand Gesture for volume up


E. Volume Down 
The system has succeeded in detecting the Volume Down hand touch and detecting the action to be performed, so the corresponding action to decrease the video volume is effective.

 
Figure 8:Hand Gesture for volume down



Results: -
A. Hand Gesture Recognition 
The system successfully recognized and classified a variety of hand gestures performed by users. These gestures included play, pause, volume up, volume down, and forward/Rewind gestures. But in certain lighting conditions the algorithm is not able to recognize hand landmarks.
 
B. Media Player Control 
The system effectively translated the recognized hand gestures into corresponding commands for the media player. Users were able to control media playback operations, such as play, pause, stop, and adjust volume, by performing predefined gestures.

C. Real-time Interaction 
The system achieved real-time performance, providing instantaneous feedback and responsiveness to the user's hand gestures. Media playback operations closely followed the recognized gestures without noticeable delays but with sometime the gestures were not recognized properly.
