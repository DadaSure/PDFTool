#PDFMerge
import numpy as np
import sys, fitz, os, datetime


def PDF_insert(pdfpath1,pdfpath2):
    output_file = pdfpath1.split(".pdf")[-2] + "inserted" + ".pdf"
    pdf1 = fitz.open(pdfpath1)
    pdf2 = fitz.open(pdfpath2)
    pdf1.insert_pdf(pdf2)
    pdf1.save(output_file)

#PDF ADD    
def PDF_add(pdfpath):
    output_file = pdfpath.split(".pdf")[-2] + "added" + ".pdf"
    pdf = fitz.open(pdfpath)
    page=pdf[-2]
    bd = page.bound()
    pdf.insert_page(-1,  # default insertion point
                        text = None,  # string or sequence of strings
                        fontsize = 11,
                        width = bd[2],
                        height = bd[3],
                        fontname = "Helvetica",  # default font
                        fontfile = None,  # any font file name
                        color = (2, 5, 5))  # text color
    pdf.save(output_file)

#PDF delect
def PDF_delete_page(pdfpath, pagerange):
    output_file = pdfpath.split(".pdf")[-2] + "deleted_page" + ".pdf"
    pdf = fitz.open(pdfpath)
    pdf.delete_pages(pagerange)
    pdf.save(output_file)


#PDF re-arrange
def PDF_adjust_page(pdfpath, re_order, outputFolder):
    output_file = pdfpath.split(".pdf")[-2] + "ajust_page" + ".pdf"
    pdf = fitz.open(pdfpath)
    pdf.select(re_order) # Input ordered page
    pdf.save(output_file)
