import numpy as np

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

if __name__ == "__main__":
    #pdfPath = "C:/Users/slrla/OneDrive/Documents/Shuo/SplitingCharDocuments/SKM_75822100714380.pdf"
    #imagePath = "C:/Users/slrla/OneDrive/Documents/Shuo/SplitingCharDocuments/output"
    #pyMuPDF_fitz(pdfPath, imagePath)
    hangleNumberRange('1,2,3-10,12, 13-15')