import numpy as np
import cv2
import pyautogui

resolution = (1920, 1080)

codec = cv2.VideoWriter.fourcc(*"XVID")

filename = "recording.avi"

fps = 60.0

out = cv2.VideoWriter(filename, codec, fps, resolution) 

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    out.write(frame)
    
    cv2.imshow('Live', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
out.release()
cv2.destroyAllWindows()
    