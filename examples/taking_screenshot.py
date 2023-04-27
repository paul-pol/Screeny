from screeny.src.screeny import Screeny

import cv2


sc = Screeny()
img = sc.take_screenshot()

cv2.imshow("Testshot", img)
cv2.waitKey(0)

