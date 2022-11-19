import numpy as np
import fitz
import cv2
import glob
import os


def PDF_Create(imgdir):
    output_file = imgdir + "/new_pdf.pdf"
    doc = fitz.open()
    pic = os.listdir(imgdir)
    # print(pic)
    imglist = [imgdir + "/" + x for x in pic]
    # print(imglist)
    for img in imglist:
        if (img.endswith('png')):
            imgdoc = fitz.open(img)  # open image as a document
            pdfbytes = imgdoc.convert_to_pdf()  # make a 1-page PDF of it
            imgpdf = fitz.open("pdf", pdfbytes)
            doc.insert_pdf(imgpdf)  # insert the image PDF
    doc.save(output_file)


def PDF_Merge(pdfdir):
    output_file = pdfdir + "/merged_pdf.pdf"
    Merge = fitz.open()
    folder = os.listdir(pdfdir)
    print("These are the docs will be merged :", folder)
    pdflist = [pdfdir + "/" + y for y in folder]
    for pdf in pdflist:
        if (pdf.endswith('pdf')):
            pdfdoc = fitz.open(pdf)
            Merge.insert_pdf(pdfdoc)
    Merge.save(output_file)


def PDF_Division(divdoc, range):
    output_folder = divdoc.split(".pdf")[-2]
    if not (os.path.exists(output_folder)):
        os.mkdir(output_folder)
    os.chdir(output_folder)
    file = fitz.open(divdoc)
    docNumbersArr = list(range.split(','))
    for index, value in enumerate(docNumbersArr):
        # print(index)
        newDoc = fitz.Document()
        splitRange = value.split('-')
        # get splited range, if lenth of splited rang >2, means this value contains a range
        if len(splitRange) > 1:
            newDoc.insert_pdf(file, from_page=int(splitRange[0]) - 1, to_page=int(splitRange[1]) - 1)
        else:
            newDoc.insert_pdf(file, from_page=int(splitRange[0]) - 1, to_page=int(splitRange[0]) - 1)
            # element of the array changed, enmerate cannot continue, break, start over
        # completed the last element processing, finish the while loop
        newDoc.save("split" + str(index + 1) + ".pdf")


if __name__ == "__main__":
    imgdir = input("Please enter img path")
    # "C:/Users/Cui/OneDrive/桌面/HKU/Computer programming for product development and applications/Homework/Group Work/image"
    pdfdir = input("Please enter pdf path")
    # "C:/Users/Cui/OneDrive/桌面/HKU/Computer programming for product development and applications/Homework/Group Work/pdf"
    divdoc = input("Please enter the document you want to divide")
    # divdoc = "C:/Users/Cui/OneDrive/桌面/HKU/Computer programming for product development and applications/Homework/Group Work/allmyimages.pdf"
    range = input("Please enter the division range of the document")
    # range = "1,2,3-4"
    PDF_Create(imgdir)
    PDF_Merge(pdfdir)
    PDF_Division(divdoc, range)
