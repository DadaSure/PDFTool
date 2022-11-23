from enum import Enum
from unittest import result
import cv2
from cv2 import COLOR_RGB2GRAY
from matplotlib.pyplot import show
import numpy as np
from cv2 import resize
from matplotlib import image
import os
import math


#Params
gaussianBlurKernelSize=15#must be an Odd
canny_thrs1=100
canny_thrs2=200
approxStepLength=0.05
openCalcKernelSize=5
edgeDectectionLineAngleRestriction = 2
dilateKernelSize = 3

class imageShowMode(Enum):
    dontShow = 0
    showFinalResult = 1
    showEachStep = 2

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
                singleImageProcessingResult = singleImageProcessing(inputPath=pic_path, showMode=imageShowMode.showEachStep)
                # resultType = type(singleImageProcessingResult)
                # print(resultType)
                if (type(singleImageProcessingResult) == type(0)):
                    #fail
                    if(singleImageProcessingResult==0):
                        failedCount+=1
                else:
                    #success
                    savePNG(fileName=filename, image=singleImageProcessingResult, outputDir=outputDir, )

                
    sucessCount = imageCount - failedCount

    #save the text box as PNG
    #savePNG()


    #print("Edge Dectection Processing Finished! Total: %s image(s) Success:%s image(s) Fail: %s images(s) Accuracy: %s" % (imageCount, sucessCount, failedCount, sucessCount/imageCount))




def singleImageProcessing(inputPath, showMode):
    # Read the original image
    img = cv2.imread(inputPath)
    img_original = img.copy()
    # Display original image
    # cv2.imshow('Original', img)
    # cv2.waitKey(0)
    if showMode == imageShowMode.showEachStep:
        showImg('Original', img)

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (gaussianBlurKernelSize,gaussianBlurKernelSize), 0)
    if showMode == imageShowMode.showEachStep:
        showImg("blur", img_blur)

    img_blur = increaseContrast(img_blur)
    #showImg("Increase Contrast",img_blur)
    if showMode == imageShowMode.showEachStep:
        showImg("increase contrast", img_blur)

    #open calculation, remove thin lines to find the textbox better
    if openCalcKernelSize != 0:
        img_blur= cv2.morphologyEx(img_blur, cv2.MORPH_OPEN, np.ones((openCalcKernelSize,openCalcKernelSize),np.uint8))
    #showImg("Open Calculation",img_blur)

    
    
    # Canny Edge Detection
    edged = cv2.Canny(image=img_blur, threshold1=canny_thrs1, threshold2=canny_thrs2, apertureSize=3) # Canny Edge Detection
    # Display Canny Edge Detection Image
    if showMode == imageShowMode.showEachStep:
        showImg('Canny Edge Detection', edged)
    

    if dilateKernelSize != 0:
        edged = cv2.dilate(img_blur, np.ones((openCalcKernelSize,openCalcKernelSize),np.uint8), iterations=1)
    if showMode == imageShowMode.showEachStep:
        showImg('dilate', edged)

    #Contour Dectection
    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[0]#if don't select [0] it will error
    #Get the largest top 5 contours
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    for c in cnts:
        #Calculate approximate
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, approxStepLength*peri, True)
        
        cv2.drawContours(img, [approx], -1, (0,255,0), 2)
        if showMode == imageShowMode.showEachStep:
            showImg('Approx', img)

        #if we can find the approx is a rectangle, then that's the text box we want to find
        if len(approx) == 4:
                screenCnt = approx
                break
    
    if not 'screenCnt' in locals():
        print("Recognition for %s failed, cannot find a rectangle text box" % inputPath)
        cv2.destroyAllWindows()
        return 0

    #Show Contours
    cv2.drawContours(img, [screenCnt], -1, (0,255,0), 2)
    if showMode == imageShowMode.showEachStep:
        showImg('Outline', img)
    
    #check if lines are near horizontal or vertical
    #if the offset is too much, means the rectangle dectection result may wrong
    rect=order_points(screenCnt.reshape(4, 2))
    (tl, tr, br, bl) = rect
    angle_topLine = calculate_k(tl,tr)
    angle_bottomLine = calculate_k(bl, br)
    angle_leftLine = calculate_k(bl, tl)
    angle_rightLine = calculate_k(br, tr)
    if abs(angle_bottomLine)>edgeDectectionLineAngleRestriction or abs(angle_topLine)>edgeDectectionLineAngleRestriction or abs(angle_leftLine)<(90-edgeDectectionLineAngleRestriction) or abs(angle_rightLine)<(90-edgeDectectionLineAngleRestriction):
        print("Recognition for %s failed, edge dectection result may be wrong" % inputPath)
        cv2.destroyAllWindows()
        return 0   

    #perspective transform
    #screenCnt should be [[x1,y1],[x2,y2],[x3,y3],[x4,y4]], means the corners of the text box
    #warped = four_point_transform(img, screenCnt.reshape(4, 2) * resize_ratio)
    warped = four_point_transform(img_original, screenCnt.reshape(4, 2))
             
    if(warped.shape[0] / img_original.shape[0] <0.45 or warped.shape[1] / img_original.shape[1] < 0.8):
        print("Recognition for %s failed, transformed image unusable" % inputPath)
        cv2.destroyAllWindows()
        return 0

    if showMode != imageShowMode.dontShow:
        showImg('Transformed', warped)

    # print(warped.shape[0]/img_original.shape[0])
    # print(warped.shape[1]/img_original.shape[1])

    #resize the transformed text box to the same width, eg 1653
    #currently doesnt work, 20221011
    transformedTargetWidth = 1653
    transformedResizeRatio = warped.shape[1]/transformedTargetWidth
    transformedHeight = int(warped.shape[0]/transformedResizeRatio)
    transformedResized = cv2.resize(warped,(transformedHeight, transformedTargetWidth))

    cv2.destroyAllWindows()

    return warped





def savePNG(fileName, image, outputDir):
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    os.chdir(outputDir)
    cv2.imwrite(fileName, image)

def increaseContrast(image):
    dstImg = cv2.equalizeHist(image)
    return dstImg

def showImg(windowName, image):
    cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
    cv2.imshow(windowName, resize(image, (int(image.shape[0]*0.8), int(image.shape[1]*0.8))))
    cv2.waitKey(0)

def order_points(pts):
    #4 points
    rect = np.zeros((4,2), dtype="float32")

    #0 upper left, 1 upper right, 2 lower right, 3 lower left
    #0,2
    s = pts.sum(axis=1)
    rect[0]=pts[np.argmin(s)]
    rect[2]=pts[np.argmax(s)]

    #1,3
    diff = np.diff(pts, axis=1)
    rect[1]=pts[np.argmin(diff)]
    rect[3]=pts[np.argmax(diff)]

    return rect

def four_point_transform(image, pts):
    #get input points
    rect=order_points(pts)
    (tl, tr, br, bl) = rect


    #calculate max width and height
    widthA = np.sqrt(((br[0]-bl[0])**2)+((br[1]-bl[1])**2))
    widthB = np.sqrt(((tr[0]-tl[0])**2)+((tr[1]-tl[1])**2))
    maxWidth = max(int(widthA), int(widthB))

    heightA = np.sqrt(((tr[0]-br[0])**2)+((tr[1]-bl[1])**2))
    heightB = np.sqrt(((tl[0]-bl[0])**2)+((tl[1]-bl[1])**2))
    maxHeight = max(int(heightA), int(heightB))

    #corrdinate after transform
    dst = np.array([
        [0,0],
        [maxWidth-1,0],
        [maxWidth-1,maxHeight-1],
        [0,maxHeight-1]
    ], dtype="float32")
    
    M=cv2.getPerspectiveTransform(rect, dst)

    warped=cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped

#計算兩點連綫的角度
def calculate_k(pt1,pt2):
    x1,y1=pt1
    x2,y2=pt2
    if x2 - x1 == 0:
        #vertical line
        result = 90
    elif y2 - y1 == 0:
        #horizontal line
        result = 0
    else:
        k = - (y2-y1) / (x2-x1)
        #result = np.arctan(k) * 57.29577
        h = math.atan(k)
        result = math.degrees(h)
    return result


def remove_red_seal(image):
        # 获得红色通道
        blue_c, green_c, red_c = cv2.split(image)
 
        # 多传入一个参数cv2.THRESH_OTSU，并且把阈值thresh设为0，算法会找到最优阈值
        thresh, ret = cv2.threshold(red_c, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # 实测调整为95%效果好一些
        filter_condition = int(thresh * 0.95)
 
        _, red_thresh = cv2.threshold(red_c, filter_condition, 255, cv2.THRESH_BINARY)
 
        # 把图片转回 3 通道
        result_img = np.expand_dims(red_thresh, axis=2)
        result_img = np.concatenate((result_img, result_img, result_img), axis=-1)
 
        return result_img

if __name__=="__main__":
    batchEdgeDetectionProcessing('0')
