# This is a sample Python script.
import os
import shutil

import fitz


def adjust_page_width(file_path, width):
    #221112 效果有点奇怪
    output_file = file_path.split(".pdf")[-2] + "_width_" + str(width) + ".pdf"
    srcDoc = fitz.Document(file_path)
    newDoc = fitz.Document()
    for ipage in srcDoc:
        ratio = ipage.rect.width / width
        height = ipage.rect.height / ratio
        page = newDoc.new_page(width=width, height=height)  # type: ignore
        # page.show_pdf_page(page.rect, srcDoc, ipage.number)
        constant = 4/3
        mat = fitz.Matrix(constant*ratio/100.0, constant*ratio/100.0)
        pix = page.get_svg_image(matrix=mat)# type: ignore

        page.insert_image(pix)
    newDoc.save(output_file)


def change_pdf_to_images(file_path):
    file_name = file_path.split("/")[-1]
    output_dir = os.path.dirname(file_path) + "/" + file_name.split(".pdf")[0] + "_to_images"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    doc = fitz.Document(file_path)
    for page in doc:
        pix = page.get_pixmap()# type: ignore
        image_name = output_dir + "/" + file_name.split(".pdf")[0] + "-" + str(page.number) + ".png"
        pix.save(image_name)


def pdf_compression(file_path, ratio):
    output_file = file_path.split(".pdf")[-2] + "_ratio_" + str(ratio) + ".pdf"
    tmp_dir = os.path.dirname(file_path) + "/" + "tmp"
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    doc = fitz.Document(file_path)
    for page in doc:
        #1277x720 -> Matrix(1,1) ->957*540
        #multiply and consant to preseve original ratio
        constant = 4/3
        mat = fitz.Matrix(constant*ratio/100.0, constant*ratio/100.0)
        pix = page.get_pixmap(matrix=mat)# type: ignore
        pix.save(tmp_dir + "/" + str(page.number) + ".jpg")
    output = fitz.Document()
    for i in range(len(os.listdir(tmp_dir))):
        img = tmp_dir + "/" + str(i) + ".jpg"
        img_doc = fitz.open(img)# type: ignore
        pdf_bytes = img_doc.convert_to_pdf()
        img_pdf = fitz.open("pdf", pdf_bytes)# type: ignore
        output.insert_pdf(img_pdf)
    output.save(output_file)
    shutil.rmtree(tmp_dir)


if __name__ == '__main__':
    testFilePath = "/Users/shuo/Documents/PyProjects/PDFTest/Vue1-10.pdf"
    adjust_page_width(testFilePath, 2000)
    # change_pdf_to_images(testFilePath)
    # pdf_compression(testFilePath, 50)
