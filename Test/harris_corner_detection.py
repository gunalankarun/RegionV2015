import cv2
import numpy as np

filename = 'calibri_font.jpg'
img = cv2.imread(filename)
print img
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,1,0.04) #(img, blockSize, ksize, k)
#larger k is, the less tolerance given
#k must be odd and no larger than 31, think k looks for a min size 

#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[255,255,0] #[b,g,r] for feature markers

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
