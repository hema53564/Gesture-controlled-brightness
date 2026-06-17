import cv2
import numpy as np
import mediapipe as mp
import screen_brightness_control as sbc
from math import hypot

# Initialize video capture and Mediapipe hands
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

# Set OpenCV window to full-screen
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)  # Allow resizing
cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)  # Full-screen mode

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture frame. Exiting...")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    lmlist = []

    if results.multi_hand_landmarks:
        for handlandmark in results.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmlist.append([id, cx, cy])
            mpDraw.draw_landmarks(img, handlandmark, mpHands.HAND_CONNECTIONS)

    if len(lmlist) > 8:  # Ensure there are enough landmarks
        x1, y1 = lmlist[4][1], lmlist[4][2]  # Thumb tip
        x2, y2 = lmlist[8][1], lmlist[8][2]  # Index finger tip
        cv2.circle(img, (x1, y1), 15, (255, 255, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 255, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # Calculate distance and brightness
        length = hypot(x2 - x1, y2 - y1)
        brightness = max(0, min(int(np.interp(length, [50, 300], [0, 100])), 100))
        sbc.set_brightness(brightness)

        # Display brightness on screen
        cv2.putText(img, f'Brightness: {brightness}%', (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Image", img)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
