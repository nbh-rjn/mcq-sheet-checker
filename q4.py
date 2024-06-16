import cv2
import numpy as np

# read img and do the usual converting so we can process further
image = cv2.imread('bubble.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

kernel = np.ones((10, 13), np.uint8)
filled_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)

q=1
opt = ['A', 'B', 'C', 'D']

for i in range(filled_image.shape[0]):
    for j in range(100, filled_image.shape[1]):
        if ((i+75)%125==0) and ((j+75)%125==0):
            if filled_image[i, j]== 0:
                print(q, end=" ")
                q+=1
                ans = ((j)//125) -1
                print(opt[ans])



cv2.waitKey(0)
cv2.destroyAllWindows()
