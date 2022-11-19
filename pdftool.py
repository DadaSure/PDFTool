import mod1_create as create
import mod2_merge as merge
import mod3_batch_processing as batch

inputFile = "0"

operationCode = -1
#mod1_create
#1-PDF_Create(imgdir) img_or_pdf_inputDir
#2-PDF_Merge(pdfdir) img_or_pdf_inputDir
#3-PDF_division(divdoc, range) pdf_input_path divide_range
#mod2_merge
#4-PDF_insert(pdfpath1,pdfpath2) pdf_input_path inserted_pdf_path
#5-PDF_add(pdfpath) pdf_input_path
#6-PDF_delete_page(pdfpath, pagerange)， pdf_input_path delete_range
#7-PDF_adjust_page(pdfpath, re_order) pdf_input_path re_order
#mod3_batch_processing
#8-adjust_page_width(file_path, width) pdf_input_path adjust_width
#9-change_pdf_to_images(file_path) pdf_input_path
#10-pdf_compression(file_path, ratio) pdf_input_path adjust_ratio


'''
(operationCode, 
img_or_pdf_inputDir, 
pdf_input_path,
insert_pdf_path, 
divide_range,
delete_range,
re_order,
adjust_width,
adjust_ratio)
'''
def pdf_tool(pdf_tool_params: dict):
    #extract params
    operationCode = pdf_tool_params["operationCode"]
    img_or_pdf_inputDir = pdf_tool_params["img_or_pdf_inputDir"]
    pdf_input_path = pdf_tool_params["pdf_input_path"]
    insert_pdf_path = pdf_tool_params["insert_pdf_path"]
    divide_range = pdf_tool_params["divide_range"]
    delete_range = pdf_tool_params["delete_range"]
    re_order = pdf_tool_params["re_order"]
    adjust_width = pdf_tool_params["adjust_width"]
    adjust_ratio = pdf_tool_params["adjust_ratio"]

    #path format checking
    print(img_or_pdf_inputDir)
    print(pdf_input_path)
    print(insert_pdf_path)

    #call
    if operationCode==1:
        create.PDF_Create(img_or_pdf_inputDir)
    if operationCode==2:
        create.PDF_Merge(img_or_pdf_inputDir)
    if operationCode==3:
        create.PDF_Division(pdf_input_path, divide_range)
    if operationCode==4:
        merge.PDF_insert(pdf_input_path, insert_pdf_path)
    if operationCode==5:
        merge.PDF_add(pdf_input_path)
    if operationCode==6:
        merge.PDF_delete_page(pdf_input_path, delete_range)
    if operationCode==7:
        merge.PDF_adjust_page(pdf_input_path, re_order)
    if operationCode==8:
        batch.adjust_page_width(pdf_input_path, adjust_width)
    if operationCode==9:
        batch.change_pdf_to_images(pdf_input_path)
    if operationCode==10:
        batch.pdf_compression(pdf_input_path, adjust_ratio)

if __name__ == "__main__":
    print("pdftool")
    pdf_tool({"operationCode":1,"img_or_pdf_inputDir":"/Users/shuo/Documents/PyProjects/PDFTest/Vue1-10_to_images"})