"qrcode in GUI"

import os
import qrcode
from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import asksaveasfile
from tkinter.scrolledtext import *

root = Tk()
root.title("QRCode Maker")
root.geometry("+200+300")
root.resizable(0,0)
root.iconbitmap("qr.ico")

frame_up_up = Frame(root)
frame_up_up.pack()
frame_up = Frame(root)
frame_up.pack(pady=5)
frame_mid = Frame(root)
frame_mid.pack(padx=5)
frame_down = Frame(root)
frame_down.pack()
frame_down_down = Frame(root)
frame_down_down.pack()

label_info = Label(frame_up_up, text="QRCODE SETTINGS", font="Vrinda 16 bold")
label_info.pack()

label_correct = Label(frame_up, text="Correction")
label_version = Label(frame_up, text="Size Version")
label_box_size = Label(frame_up, text="Box Size")
label_border = Label(frame_up, text="Border Size")

combo_correct = Combobox(frame_up, width=18)
combo_correct["values"] = ["Below 7%", "Below 15%", "Below 25%", "Below 30%"]
combo_correct["state"] = "readonly"
combo_correct.current(1)
entry_version = Entry(frame_up)
entry_version.insert(INSERT, "1")
entry_box_size = Entry(frame_up)
entry_box_size.insert(INSERT, "10")
entry_border = Entry(frame_up)
entry_border.insert(INSERT, "4")

label_correct.grid(row=1, column=1, pady=2)
label_version.grid(row=2, column=1, pady=2)
label_box_size.grid(row=3, column=1, pady=2)
label_border.grid(row=4, column=1, pady=2)

combo_correct.grid(row=1, column=2, pady=2)
entry_version.grid(row=2, column=2, pady=2)
entry_box_size.grid(row=3, column=2, pady=2)
entry_border.grid(row=4, column=2, pady=2)

label_text = Label(frame_mid, text="Content/URL")
label_text.pack()
text = ScrolledText(frame_mid, width=30, height=5)
text.insert(INSERT, "Hello, George!")
text.pack()

def submit():
    error = False
    correction_get = combo_correct.get()
    version_get = entry_version.get()
    box_size_get = entry_box_size.get()
    border_get = entry_border.get()
    text_get = text.get("1.0", END)

    if correction_get == "Below 7%":
        error_correction_get = qrcode.ERROR_CORRECT_L
    elif correction_get == "Below 15%":
        error_correction_get = qrcode.ERROR_CORRECT_M
    elif correction_get == "Below 25%":
        error_correction_get = qrcode.ERROR_CORRECT_Q
    elif correction_get == "Below 30%":
        error_correction_get = qrcode.ERROR_CORRECT_H
    else:
        error = True
        showerror("Error", "Wrong Value")
        root.destroy()
        
    if error == False:
        code = qrcode.QRCode(
            version = int(version_get),
            error_correction = error_correction_get,
            box_size = int(box_size_get),
            border = int(border_get),
            image_factory = None,
            mask_pattern = None)

    path_get = asksaveasfile(
        parent=root,
        title="Save As",
        initialdir=os.getcwd(),
        filetypes=[("PNG图片", ".png"), ("JPEG图片", ".jpg"), ("BMP图片", ".bmp"), ("TIF图片", ".tif"), ("所有文件", "*")],
        defaultextension=".png")

    qrcode_get = qrcode.make(text_get)
    qrcode_get.save(path_get.name)

    question = askquestion("Prompt", "QRCode has been created successfully.\nDo you want to see it now?")

    if question == "yes":
        qrcode_get.show()

    root.destroy()
        
button_cancel = Button(frame_down, text="Cancel", command=root.destroy)
button_submit = Button(frame_down, text="Submit", command=submit)

button_cancel.grid(row=1, column=1, padx=10, pady=10, ipadx=8)
button_submit.grid(row=1, column=2, padx=10, pady=10, ipadx=8)

label_info_2 = Label(frame_down_down, text="QRCode Maker 1.1 -- By lanlan2_")
label_info_2.pack()
root.mainloop()
