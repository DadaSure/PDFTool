import cv2
import numpy as np
import os


def batchEdgeDetectionProcessing(inputDir):
    #Manual Input
    if inputDir == '0':
        inputDir = input("Please input the directory for processing (parent of the folders to be processed): ")
    #inputDir = 'C:/Users/slrla/OneDrive/Documents/Shuo/SplitingTest221011/Naming'

    outputDir = inputDir + '/' + 'edge_detection_output'
    #C:/Users/slrla/OneDrive/Documents/Shuo/SplitingCharDocuments
    if not (os.path.exists(inputDir)):
        print("ERROR: Input path does not exist (pay attention to the path format)")
        exit() 
    os.chdir(inputDir)
    
    failedCount = 0
    imageCount = 0

    for parent, dirnames, filenames in os.walk(inputDir):
        for filename in filenames:
            if 'edge_detection_output' in parent or 'cutting_char_output' in parent:
                break
            pic_path = os.path.join(parent, filename)
            print(pic_path)
            if(pic_path.endswith('.png')):
                imageCount+=1
                singleImageProcessingResult = singleImageEdgeDetection(pic_path, True)
                if (type(singleImageProcessingResult) == type(0)):
                    #fail
                    if(singleImageProcessingResult==0):
                        failedCount+=1
                else:
                    #success
                    savePNG(fileName=filename, image=singleImageProcessingResult, outputDir=outputDir)

def singleImageEdgeDetection(imgPath, debugOption: bool):
    fileNameWithExtension = str(os.path.basename(imgPath))
    if not fileNameWithExtension.endswith('.png'):
        return (0,0)
    fileName = fileNameWithExtension.split('.')[0]

    #read input image
    image = cv2.imread(imgPath)

    #save a ratio for the last step transform
    ratio = 900 / image.shape[0]
    img = resizeImg(image)
    print('shape =', img.shape)

    #do canny edge detection
    canny_img = getCanny(img)
    if debugOption:
        showImg("canny", canny_img)


    #find the largest contour
    imgContour = img.copy()
    max_contour, max_area = findMaxContour(canny_img)
    cv2.drawContours(imgContour, max_contour, -1, (0, 0, 255), 3)
    if debugOption:
        showImg("maxcontour", imgContour)

    #find the boxes of the largest contour
    imgBox = img.copy()
    boxes = getBoxPoint(max_contour)
    for box in boxes:
        cv2.circle(imgBox, tuple(box), 5, (0, 0, 255), 2)
    print(boxes)
    if debugOption:
        showImg("box", imgBox)

    #transform the contour box into a rect
    boxes = adaPoint(boxes, ratio)
    boxes = orderPoints(boxes)
    # 透视变化
    warped = warpImage(image, boxes)
    if debugOption:
        showImg("transform", warped)
    
    if debugOption:
        cv2.destroyAllWindows()

    return warped


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


# 求出面积最大的轮廓
def findMaxContour(image):
    # 寻找边缘
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # 计算面积
    max_area = 0.0
    max_contour = []
    for contour in contours:
        currentArea = cv2.contourArea(contour)
        if currentArea > max_area:
            max_area = currentArea
            max_contour = contour
    return max_contour, max_area


# 多边形拟合凸包的四个顶点
def getBoxPoint(contour):
    # 多边形拟合凸包
    hull = cv2.convexHull(contour)
    epsilon = 0.02 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(hull, epsilon, True)
    approx = approx.reshape((len(approx), 2))
    return approx


# 适配原四边形点集
def adaPoint(box, pro):
    box_pro = box
    if pro != 1.0:
        box_pro = box/pro
    box_pro = np.trunc(box_pro)
    return box_pro
 
 
# 四边形顶点排序，[top-left, top-right, bottom-right, bottom-left]
def orderPoints(pts):
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect
 
 
# 计算长宽
def pointDistance(a, b):
    return int(np.sqrt(np.sum(np.square(a - b))))
 
 
# 透视变换
def warpImage(image, box):
    w, h = pointDistance(box[0], box[1]), \
           pointDistance(box[1], box[2])
    dst_rect = np.array([[0, 0],
                         [w - 1, 0],
                         [w - 1, h - 1],
                         [0, h - 1]], dtype='float32')
    M = cv2.getPerspectiveTransform(box, dst_rect)
    warped = cv2.warpPerspective(image, M, (w, h))
    return warped

def savePNG(fileName, image, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    os.chdir(outputDir)
    cv2.imwrite(fileName, image)

def showImg(windowName, image):
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    # cv2.imshow(windowName, resize(image, (int(image.shape[0]*0.8), int(image.shape[1]*0.8))))
    cv2.imshow(windowName, image)
    cv2.waitKey(0)


if __name__=="__main__":
    batchEdgeDetectionProcessing('0')

'''
path = r'/Users/shuo/Documents/PyProjects/PDFTest/edge_detection/edge.png'
outpath_canny = r'/Users/shuo/Documents/PyProjects/PDFTest/edge_detection/edge_canny.png'
outpath_maxcontour = r'/Users/shuo/Documents/PyProjects/PDFTest/edge_detection/edge_contour.png'
outpath_box = r'/Users/shuo/Documents/PyProjects/PDFTest/edge_detection/edge_box.png'
outpath_transform = r'/Users/shuo/Documents/PyProjects/PDFTest/edge_detection/edge_transform.png'
'''
