import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')

#photo[10:150, 200:280] = 181, 176, 38

#cv2.rectangle(photo, (10, 0), (100, 100), (119, 201, 105), thickness=cv2.FILLED)

#cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (119, 201, 105), thickness=3)

#cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 100, (181, 176, 38), thickness=cv2.FILLED)
#Привет)))))))))

cv2.putText(photo, "Shelk", (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (181, 176, 38), 2)
cv2.imshow('Photo', photo)
cv2.waitKey(0)
