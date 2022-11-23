import cv2
import numpy as np
 
 
# 固定尺寸
def resizeImg(image, height=900):
    h, w = image.shape[:2]
    pro = height / h
    size = (int(w * pro), int(height))
    img = cv2.resize(image, size)
    return img
 
 
# 边缘检测
def getCanny(image):
    # 高斯模糊
    binary = cv2.GaussianBlur(image, (3, 3), 2, 2)
    # 边缘检测
    binary = cv2.Canny(binary, 60, 240, apertureSize=3)
    # 膨胀操作，尽量使边缘闭合
    kernel = np.ones((3, 3), np.uint8)
    binary = cv2.dilate(binary, kernel, iterations=1)
    return binary
 
path = r'/Users/shuo/Documents/PyProjects/PDFTest/edge_detection/edge.png'
outpath = r'/Users/shuo/Documents/PyProjects/PDFTest/edge_detection/edge_canny.png'
img = cv2.imread(path)
img = resizeImg(img)
print('shape =', img.shape)
binary_img = getCanny(img)
cv2.imwrite(outpath, binary_img)
 
# output:    shape = (900, 420, 3)