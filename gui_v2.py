# created by Xiang Yuyan in 2022.11.21
# gui version 2

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import tkinter.filedialog 
import tkinter as tk
import pdftool

import sys
import os


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./gui_pic")

def get_resource_path(relative_path):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

ASSETS_PATH = get_resource_path(ASSETS_PATH)

# variables
output_path = ""
output_path1 = ""
output_path2 = ""
output_path3 = ""
operationCode = -1

# function
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def reset():
    if(var1.get()==1, var2.get()==1 or var3.get()==1 or var4.get()==1 or var5.get()==1 or var6.get()==1 or var7.get()==1 or var8.get()==1 or var9.get()==1 or var10.get()==1 ):
        if(var1.get()==1):
            c2.config(state='disabled'), c3.config(state='disabled') ,c4.config(state='disabled'), c5.config(state='disabled'), c6.config(state='disabled')
            c7.config(state='disabled'), c8.config(state='disabled'), c9.config(state='disabled'), c10.config(state='disabled'), c1.config(state = 'disabled')
            c_cv.config(state='normal')
        else: 
            c2.config(state='disabled'), c3.config(state='disabled') ,c4.config(state='disabled'), c5.config(state='disabled'), c6.config(state='disabled')
            c7.config(state='disabled'), c8.config(state='disabled'), c9.config(state='disabled'), c10.config(state='disabled'), c1.config(state = 'disabled'), c_cv.config(state='disabled')
    else:
        c2.config(state='normal'), c1.config(state='normal'), c3.config(state='normal'), c4.config(state='normal'), c5.config(state='normal')
        c6.config(state='normal'), c7.config(state='normal'), c8.config(state='normal'), c9.config(state='normal'), c10.config(state='normal'), c_cv.config(state='normal')

def resetall():
        global operationCode
        c2.config(state='normal'), c1.config(state='normal'), c3.config(state='normal'), c4.config(state='normal'), c5.config(state='normal')
        c6.config(state='normal'), c7.config(state='normal'), c8.config(state='normal'), c9.config(state='normal'), c10.config(state='normal'), c_cv.config(state='disabled')
        var1.set(0), var2.set(0), var3.set(0), var4.set(0), var5.set(0)
        var6.set(0), var7.set(0), var8.set(0), var9.set(0), var10.set(0), varcv.set(0)
        path_entry.config(state='disabled'), path_entry2.config(state='disabled'), path_entry3.config(state='disabled'), path_entry4.config(state='disabled')
        path_entry5.config(state='disabled'), path_entry6.config(state='disabled'),path_entry7.config(state='disabled'), path_entry8 .config(state='disabled')
        operationCode = -1

        # clear all input
        path_entry.delete

def find_operation_code():
    global operationCode
    arr = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get(), var10.get()]
    for i in range(0, len(arr)):
        if arr[i] == 1:
            operationCode = i+1
    return operationCode

def confirmButton():
    global operationCode
    o_code = find_operation_code()

    print("operation code", o_code)
    print("O1 : %d, O2: %d, O3 : %d, O4: %d, O5 : %d, O6: %d, O7 : %d, O8: %d, O9 : %d, 10: %d" % (var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get(), var10.get()))

    if(operationCode == 1):
        path_entry.config(state='normal')
        # input path entry
    
    if(operationCode == 2):
        path_entry.config(state='normal')
        # input path entry
   
    if(operationCode == 3):
        path_entry3.config(state='normal')
        path_entry5.config(state='normal')
        # input path entry

    if(operationCode == 4):
        path_entry3.config(state='normal')
        path_entry2.config(state='normal')
        # input path entry

    if(operationCode == 5):
        path_entry3.config(state='normal')
        # input path entry

    if(operationCode == 6):
        path_entry3.config(state='normal')
        path_entry4.config(state='normal')
        # input path entry

    if(operationCode == 7):
        path_entry3.config(state='normal')
        path_entry6.config(state='normal')
        # input path entry

    if(operationCode == 8):
        path_entry3.config(state='normal')
        path_entry7.config(state='normal')
        # input path entry

    if(operationCode == 9):
        path_entry3.config(state='normal')
        # input path entry

    if(operationCode == 10):
        path_entry3.config(state='normal')
        path_entry8.config(state='normal')
        # input path entry

# gui by tkinter
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
window = Tk()
window.geometry("1000x800")
window.configure(bg = "#FFFFFF")
window.title("PDF_Tool From Group 7")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
canvas.place(x = 0, y = 0)



# checkbox part 
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
x = -25
y = -21
t = 40
t_x_width = -140
checkbox_width = 33
checkbox_height =2 

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
varcv = IntVar()


c1 = tk.Checkbutton(window, text="Create a PDF", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF", width=16, height=checkbox_height, variable=var1,command=reset)
c1.place(x=25, y=154)
c2 = tk.Checkbutton(window, text="Merge PDFs", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF",  width=checkbox_width, height=checkbox_height, variable=var2,command=reset)
c2.place(x=50+x, y=175+t+y)
c3 = tk.Checkbutton(window, text="Delete Pages in a PDF", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF",  width=checkbox_width, height=checkbox_height, variable=var6,command=reset)
c3.place(x=520+x+t_x_width, y=175+y)
c4 = tk.Checkbutton(window, text="Rearrange PDF pages", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0, bg="#FFFFFF", width=checkbox_width, height=checkbox_height, variable=var7,command=reset)
c4.place(x=520+x+t_x_width, y=175+t+y)
c5 = tk.Checkbutton(window, text="Divide a PDF", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF",  width=checkbox_width, height=checkbox_height, variable=var3,command=reset)
c5.place(x=50+x, y=175+t*2+y)
c6 = tk.Checkbutton(window, text="Insert another into a PDF", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF",  width=checkbox_width, height=checkbox_height, variable=var4,command=reset)
c6.place(x=50+x, y=175+t*3+y)
c7 = tk.Checkbutton(window, text="Adjust PDF page width", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF",  width=checkbox_width, height=checkbox_height, variable=var8,command=reset)
c7.place(x=520+x+t_x_width, y=175+t*2+y)
c8 = tk.Checkbutton(window, text="Export PDF as PNG images", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF",  width=checkbox_width, height=checkbox_height, variable=var9,command=reset)
c8.place(x=520+x+t_x_width, y=175+t*3+y)
c9 = tk.Checkbutton(window, text="Add a blank page to a PDF", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF",  width=checkbox_width, height=checkbox_height, variable=var5,command=reset)
c9.place(x=50+x, y=175+t*4+y)
c10 = tk.Checkbutton(window, text="PDF page resize", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF",  width=checkbox_width, height=checkbox_height, variable=var10,command=reset)
c10.place(x=520+x+t_x_width, y=175+t*4+y)

c_cv = tk.Checkbutton(window, text="<- Use Opencv", font="BahnschriftLight 13", takefocus=0,  fg="black", bd=0,bg="#FFFFFF",  width=16, height=checkbox_height, variable=varcv,command=reset,state= "disabled")
c_cv.place(x=170, y=154)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




# Title of the project 
canvas.create_text(677.0,38.0,anchor="nw",text="PDFTool   IDAT7215",fill="#000000",font=("Inter Bold", 30 * -1))
canvas.create_text(677.0,70.0,anchor="nw",text="#Group 7",fill="#000000",font=("Inter Bold", 30 * -1))

# Step 1
canvas.create_text(700.0,162.0,anchor="nw",text="Step 1: Confirm the operation",fill="#000000",font=("Arial", 15 * -1))

# Step 2
canvas.create_text(700.0,202.0,anchor="nw",text="Step 2: Enter input and process",fill="#000000",font=("Arial", 15 * -1))




 

tk.Button(window, text="Reset", font="Arial 20",bd=0,bg="#FFFFFF", relief=FLAT, height=2, width=15, command= resetall).place(x=700, y=240)
tk.Button(window, text="confirm", font="Arial 20",bd=0,bg="#FFFFFF", relief=FLAT, height=2, width=15, command= confirmButton).place(x=700, y=300)

# Input Part






# Input box 
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 8 input box postion
path_entry = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716", highlightthickness=0, state = "disabled")
path_entry.place(x=45, y=390, width=410.0, height=35)
path_entry2 = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716", highlightthickness=0, state = "disabled")
path_entry2.place(x=500, y=390, width=410.0, height=35)
path_entry3 = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716", highlightthickness=0, state = "disabled")
path_entry3.place(x=45, y=466, width=410.0, height=35)
path_entry4 = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716", highlightthickness=0, state = "disabled")
path_entry4.place(x=500, y=466, width=410.0, height=35)
path_entry5 = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716", highlightthickness=0, state = "disabled")
path_entry5.place(x=45, y=542, width=410.0, height=35)
path_entry6 = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716", highlightthickness=0, state = "disabled")
path_entry6.place(x=500, y=542, width=410.0, height=35)
path_entry7 = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716", highlightthickness=0, state = "disabled")
path_entry7.place(x=45, y=618, width=410.0, height=35)
path_entry8 = tk.Entry(bd=0, bg="#F6F7F9", fg="#000716", highlightthickness=0, state = "disabled")
path_entry8.place(x=500, y=618, width=410.0, height=35)
# state = "disabled"

def select_path1():
    global output_path
    output_path = tk.filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, output_path)
def select_path2():
    global output_path2
    output_path2 = tk.filedialog.askopenfilename()
    path_entry2.delete(0, tk.END)
    path_entry2.insert(0, output_path2)
def select_path3():
    global output_path3
    output_path3 = tk.filedialog.askopenfilename()
    path_entry3.delete(0, tk.END)
    path_entry3.insert(0, output_path3)

path_picker_img = tk.PhotoImage(file = ASSETS_PATH + "/path_picker.png")

# Select box Image and postion 
path_picker_button = tk.Button(image = path_picker_img,text = '',compound = 'center',fg = 'white',borderwidth = 0,highlightthickness = 0,command = select_path1,relief = 'flat')
path_picker_button2 = tk.Button(image = path_picker_img,text = '',compound = 'center',fg = 'white',borderwidth = 0,highlightthickness = 0,command =  select_path2,relief = 'flat')
path_picker_button3 = tk.Button(image = path_picker_img,text = '',compound = 'center',fg = 'white',borderwidth = 0,highlightthickness = 0,command =  select_path3,relief = 'flat')
path_picker_button.place(x = 420, y = 395,width = 24,height = 22)
path_picker_button2.place(x = 875, y = 395,width = 24,height = 22)
path_picker_button3.place(x = 420, y = 471,width = 24,height = 22)

# input box image
text_box_bg = tk.PhotoImage(file=ASSETS_PATH + "/TextBox_Bg.png")
O1 = canvas.create_image(36.0,365.0, anchor="nw",image=text_box_bg)
O2 = canvas.create_image(491.0,365.0, anchor="nw",image=text_box_bg)
O3 = canvas.create_image(36, 441.0, anchor="nw",image=text_box_bg)
O4 = canvas.create_image(491, 441.0, anchor="nw",image=text_box_bg)
O5 = canvas.create_image(36, 517.0, anchor="nw",image=text_box_bg)
O6 = canvas.create_image(491, 517.0, anchor="nw",image=text_box_bg)
O7 = canvas.create_image(36, 593.0, anchor="nw",image=text_box_bg)
O8 = canvas.create_image(491, 593.0, anchor="nw",image=text_box_bg)

# Have to select PATH from the folder
canvas.create_text(45.0,370.0,anchor="nw",text="Select a folder",fill="#000000",font=("Arial-BoldMT", 16 * -1))
canvas.create_text(500.0,370.0,anchor="nw",text="Select a PDF File to be inserted",fill="#000000",font=("Arial-BoldMT", 16 * -1))
canvas.create_text(45.0,446.0,anchor="nw",text="Select a PDF File",fill="#000000",font=("Arial-BoldMT", 16 * -1))
# Input the number 
canvas.create_text(500.0,446.0,anchor="nw",text="Page ranges to be deleted, e.g., 2,5",fill="#000000",font=("Arial-BoldMT", 16 * -1))
canvas.create_text(500.0,522.0,anchor="nw",text="Page numbers selected to rearrange, e.g. 1,3,5",fill="#000000",font=("Arial-BoldMT", 16 * -1))
canvas.create_text(45.0,522.0,anchor="nw",text="Page ranges to be devided, e.g. 1, 3-5, 7-9",fill="#000000",font=("Arial-BoldMT", 16 * -1))
canvas.create_text(500.0,598.0,anchor="nw",text="Page resize ratio to adjust (0-100), e.g. 50",fill="#000000",font=("Arial-BoldMT", 16 * -1))
canvas.create_text(45.0,598.0,anchor="nw",text="Page witdh to adjust, e.g. 400",fill="#000000",font=("Arial-BoldMT", 16 * -1))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# process function 
def process_button():
    input1_img_or_pdf_inputDir = path_entry.get()
    input2_insert_pdf_path = path_entry2.get()
    input3_pdf_input_path = path_entry3.get()
    input4_delete_range = path_entry4.get()
    input5_divide_range = path_entry5.get()
    input6_re_order = path_entry6.get()
    input7_adjust_width = path_entry7.get()
    input8_adjust_ratio = path_entry8.get()

    print("Process button clicked" + "Operation code: %d" % operationCode)

    if operationCode == 1:
        pdftool.pdf_tool(1, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)
    if operationCode == 2:
        pdftool.pdf_tool(2, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)
    if operationCode == 3:
        pdftool.pdf_tool(3, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)
    if operationCode == 4:
        pdftool.pdf_tool(4, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)
    if operationCode == 5:
        pdftool.pdf_tool(5, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)
    if operationCode == 6:
        pdftool.pdf_tool(6, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)
    if operationCode == 7:
        pdftool.pdf_tool(7, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)
    if operationCode == 8:
        pdftool.pdf_tool(8, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)
    if operationCode == 9:
        pdftool.pdf_tool(9, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)
    if operationCode == 10:
        pdftool.pdf_tool(10, input1_img_or_pdf_inputDir, varcv, input3_pdf_input_path, input2_insert_pdf_path, input5_divide_range, input4_delete_range, input6_re_order, input7_adjust_width, input8_adjust_ratio)



# The final process button
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(323.0,75.0,image=image_image_1)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=process_button,relief="flat")
button_1.place(x=365.0,y=713.0,width=269.0,height=63.0)


window.resizable(False, False)
window.mainloop()
