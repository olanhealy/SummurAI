import os
import customtkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def select_pptx_file():
    file_path = filedialog.askopenfilename(
        title="Select a .pptx file",
        filetypes=[("PowerPoint files", "*.pptx")]
    )
    if file_path:
        label.configure(text='SUCCESS: Selected PowerPoint file', font=("Helvetica", 24))
    else:
        label.configure(text='No file selected', font=("Helvetica", 24))

root = customtkinter.CTk()
root.geometry("1200x800")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=0, padx=0, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Please select a .pptx file", font=("Helvetica", 24))
label.pack(pady=200, padx=0)

button = customtkinter.CTkButton(master=frame, text="Select PowerPoint File", command=select_pptx_file)
button.pack(pady=20, padx=0)

root.mainloop()
