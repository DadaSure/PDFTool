from struct import pack
import sys, fitz, os, datetime
import time
from cv2 import rotate
import numpy as np

#将4页的PDF转换为4个PNG图片

#def batchPDFConvert():
def batchPDFConvert(inputDir):
    #Manual Input
    if inputDir=='0':
        inputDir = input("Please input the directory for pdf to image processing (parent of the folders to be processed): ")
    
    #C:/Users/slrla/OneDrive/Documents/Shuo/SplitingTest221011/Naming
    #inputDir = 'C:/Users/slrla/OneDrive/Documents/Shuo/***'
    outputDir = inputDir + '/' + 'pdf_img_output'
    if not (os.path.exists(inputDir)):
        print("ERROR: Input path does not exist (pay attention to the windows path format)")
        exit() 
    os.chdir(inputDir)

    pdfCount = 0
    imageCount = 0

    T_start = time.process_time()

    for parent, dirnames, filenames in os.walk(inputDir):
        for filename in filenames:
            pdf_path = os.path.join(parent, filename)
            print(pdf_path)
            if(pdf_path.endswith('.pdf')):
                pdfCount+=1
                imagePlus = singlePDFConvert(pdf_path, outputDir=outputDir)
                imageCount += imagePlus  # type: ignore
    
    T_end = time.process_time()
    time_used = int(T_end-T_start)

    print("PDF to Image Conversion Finished! %s PDF File(s), %s Image(s), Time %ss" % (pdfCount, imageCount, time_used))

def singlePDFConvert(filePath, outputDir):
    #Read File

    fileNameWithExtension = str(os.path.basename(filePath))
    if not fileNameWithExtension.endswith('.pdf'):
        return (0,0)
    fileName = fileNameWithExtension.split('.')[0]
    # docNumbers = hangleNumberRange(fileName=fileName)
    #print(filePath)
    #print(docNumbers)
    #C:/Users/slrla/OneDrive/Documents/Shuo/SplitingCharDocuments/SKM_75822101016280.pdf
    #10103,10104,10105

    if not (os.path.exists(filePath)):
        print("ERROR: Input file does not exist (pay attention to the path format)")
        exit()
    pdfDoc = fitz.open(filePath)  # type: ignore
    pageOfTheDoc = pdfDoc.page_count
    # if (len(docNumbers)*4 != pageOfTheDoc):
    #     print("ERROR: docNumbers does not match actual pages, please check and retry")
    #     exit()
    
    #Initialize
    #fileDir = os.path.dirname(filePath)#Directory of the Input PDF File
    fileDir = outputDir
    currentPageInADoc = 0
    # currentDoc = 0
    successfulWriteCount = 0

    #Start Convert
    for pg in range(pageOfTheDoc):
        #Get Directory to Write the PNG
        # outputDir = str(fileDir)+'/'+str(docNumbers[currentDoc])#Save PNG to the Same Level of Path of the PDF
        outputDir = str(fileDir)+'/'+str(fileName)#Save PNG to the Same Level of Path of the PDF
        if(currentPageInADoc==0 and not os.path.exists(outputDir)):
            os.makedirs(outputDir)
        os.chdir(outputDir)
        #Read PDF Page and Write PNG
        pageData = pdfDoc[pg]
        mat = fitz.Matrix(3.0, 3.0)
        pixData = pageData.get_pixmap(matrix=mat)
        pixData.save(outputDir+'/'+'%s_%s.png' % (fileName,(currentPageInADoc+1)))
        #Change Counters After Wrote the PNG
        successfulWriteCount += 1
        currentPageInADoc += 1
        # #There are 4 pages in a Document, if current page == 4, means a Document finished
        # #Move on to the next one
        # if(currentPageInADoc == 4):
        #     currentDoc += 1
        #     currentPageInADoc = 0
        # #If currentDoc == length of the docNumbers, means all Document finished, break
        # if(currentDoc == len(docNumbers)):
        #     break
    
    #Check if there's no problem
    if(successfulWriteCount != pageOfTheDoc):
        print("WARNING: successful wrote file count does not match actual pages number, please check")
        exit()

    #print("Finished! %s pages of %s Documents converted!" % (successfulWriteCount, len(docNumbers)))
    return successfulWriteCount


def hangleNumberRange(fileName):
    #[1,2,3-10,12, 13-15]
    #split using ','
    docNumbersArr = list(fileName.split(','))
    #print(docNumbersArr)
    #split elements contains '-' using '-'
    rangeCoversionCompleted = 0
    while(not rangeCoversionCompleted):
        for index, value in enumerate(docNumbersArr):
            splitRange = value.split('-')
            #get splited range, if lenth of splited rang >2, means this value contains a range
            if len(splitRange)>1:
                #add corresponding values to the docNumbersArr
                for idx, docNumber in enumerate(np.arange(int(splitRange[0]),int(int(splitRange[1])+1),dtype=int)):
                    docNumbersArr.insert(index+idx, str(docNumber))
                #remove this element contains '-'
                docNumbersArr.remove(value)
                #element of the array changed, enmerate cannot continue, break, start over
                break
            #completed the last element processing, finish the while loop
            if index == len(docNumbersArr)-1:
                rangeCoversionCompleted = 1
    #print(docNumbersArr)
    return docNumbersArr

# def pyMuPDF_fitz(pdfPath, imagePath):
#     print("imagePath="+imagePath)
#     pdfDoc = fitz.open(pdfPath)
#     for pg in range(pdfDoc.page_count):
#         page = pdfDoc[pg]
        
#         mat = fitz.Matrix(3.0,3.0)

#         pix = page.get_pixmap(matrix=mat)

#         if not os.path.exists(imagePath):
#             os.makedirs(imagePath)

#         #pix.writePNG(f'{imagePath}/{page}.png')
#         pix.writePNG(imagePath+'/'+'images_%s.png' % pg)

if __name__ == "__main__":
    #pdfPath = "C:/Users/slrla/OneDrive/Documents/Shuo/SplitingCharDocuments/SKM_75822100714380.pdf"
    #imagePath = "C:/Users/slrla/OneDrive/Documents/Shuo/SplitingCharDocuments/output"
    #pyMuPDF_fitz(pdfPath, imagePath)
    batchPDFConvert('0')