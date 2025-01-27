import cv2  
import mediapipe as mp  
import pyautogui  
import time  

def count_fingers(lst):
    cnt = 0  # Initialize finger count

    # Calculate a threshold based on the vertical position of specific landmarks
    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    # Check if the index finger is raised (landmark 5 is the tip, landmark 8 is the base)
    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1

    # Check if the middle finger is raised (landmark 9 is the tip, landmark 12 is the base)
    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1

    # Check if the ring finger is raised (landmark 13 is the tip, landmark 16 is the base)
    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1

    # Check if the pinky finger is raised (landmark 17 is the tip, landmark 20 is the base)
    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1

    # Check if the thumb is extended (landmark 5 is tip, landmark 4 is base)
    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 1

    return cnt  # Return the total count of raised fingers


cap = cv2.VideoCapture(0)

# Initialize MediaPipe drawing utilities and hands module
drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=1)  # Create a Hands object to detect one hand at a time

start_init = False  # Flag to indicate whether counting has started
prev = -1  # Variable to store previous finger count

while True:
    end_time = time.time()  # Get current time for timing control
    _, frm = cap.read()  # Capture frame from webcam
    frm = cv2.flip(frm, 1)  # Flip the frame horizontally for a mirror effect

    # Process the frame to detect hands and landmarks
    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

    if res.multi_hand_landmarks:  # Check if any hands are detected
        hand_keyPoints = res.multi_hand_landmarks[0]  # Get landmarks for the first detected hand

        cnt = count_fingers(hand_keyPoints)  # Count raised fingers 

        # Check if the current finger count is different from the previous count
        if not(prev == cnt):
            if not(start_init):  
                start_time = time.time()  # Start timing when a new count is detected
                start_init = True

            elif (end_time - start_time) > 0.2:  
                # Only act after a delay of more than 0.2 seconds to avoid rapid triggering
                if (cnt == 1):
                    pyautogui.press("right")  

                elif (cnt == 2):
                    pyautogui.press("left")    
                
                elif (cnt == 3):
                    pyautogui.press("up")     
                
                elif (cnt == 4):
                    pyautogui.press("down")    
                
                elif (cnt == 5):
                    pyautogui.press("space")    

                prev = cnt   # Update previous count to current count
                start_init = False   # Reset start initialization flag

        
        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    cv2.imshow("window", frm)  

    if cv2.waitKey(1) & 0xFF == 27:  
        cv2.destroyAllWindows()   
        cap.release()  
        break   