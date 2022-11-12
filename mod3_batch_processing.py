# This is a sample Python script.
import os
import shutil

import fitz


def adjust_page_width(file_path, width):
    output_file = file_path.split(".pdf")[-2] + "_width_" + str(width) + ".pdf"
    src = fitz.Document(file_path)
    doc = fitz.Document()
    for ipage in src:
        ratio = ipage.rect.width / width
        height = ipage.rect.height / ratio
        page = doc.new_page(width=width, height=height)  # type: ignore
        page.show_pdf_page(page.rect, src, ipage.number)
    doc.save(output_file)


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
        mat = fitz.Matrix(ratio/100.0, ratio/100.0)
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
    testFilePath = "/Users/shuo/Documents/PyProjects/PDFTest/Hand Interfaces - Using Hands to Imitate Objects in AR:VR for Expressive Interactions.pdf"
    # adjust_page_width(testFilePath, 250)
    # change_pdf_to_images(testFilePath)
    pdf_compression(testFilePath, 75)
