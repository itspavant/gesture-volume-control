import cv2
import time
import math
import numpy as np
import pyttsx3
import HandTrackingModule as htm
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Text-to-Speech Engine
engine = pyttsx3.init()

# Camera setup
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
camera_on = True  # Toggle flag for camera on/off

# Hand detection
detector = htm.handDetector(detectionCon=0.7)

# Audio control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

# Initial volume display values
vol = 0
volBar = 400
volPer = 0
prev_lengths = []

try:
    while True:
        if camera_on:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)

            if len(lmList) != 0:
                # Thumb tip = 4, Index tip = 8
                x1, y1 = lmList[4][1], lmList[4][2]
                x2, y2 = lmList[8][1], lmList[8][2]
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

                cv2.circle(img, (x1, y1), 7, (0, 255, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 7, (0, 255, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.circle(img, (cx, cy), 7, (0, 255, 0), cv2.FILLED)

                length = math.hypot(x2 - x1, y2 - y1)

                # Smooth volume
                prev_lengths.append(length)
                if len(prev_lengths) > 5:
                    prev_lengths.pop(0)
                smooth_length = sum(prev_lengths) / len(prev_lengths)

                vol = np.interp(smooth_length, [20, 110], [minVol, maxVol])
                volBar = np.interp(smooth_length, [20, 110], [400, 150])
                volPer = np.interp(smooth_length, [20, 110], [0, 100])
                volume.SetMasterVolumeLevel(vol, None)

                if smooth_length < 20:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)

                # Mute/unmute
                x_pinky, y_pinky = lmList[20][1], lmList[20][2]
                pinky_dist = math.hypot(x_pinky - x1, y_pinky - y1)

                if pinky_dist < 40:
                    volume.SetMute(1, None)
                    engine.say("Muted")
                    engine.runAndWait()
                    cv2.putText(img, "MUTED", (460, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)
                else:
                    volume.SetMute(0, None)
                    engine.say("Unmuted")
                    engine.runAndWait()

                cv2.putText(img, f"Len: {int(length)}", (400, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 255), 2)

            # Draw volume bar
            cv2.rectangle(img, (50, 150), (85, 400), (0, 255, 0), 2)
            cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f"{int(volPer)} %", (40, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

            # FPS
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

            # Show result
            cv2.imshow("Img", img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):  # Quit
            break
        elif key == ord("p"):  # Pause or resume camera
            camera_on = not camera_on
            print("Camera On" if camera_on else "Camera Off")

except KeyboardInterrupt:
    print("Interrupted by user.")

finally:
    cap.release()
    cv2.destroyAllWindows()
