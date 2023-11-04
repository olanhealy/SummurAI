import os
import customtkinter
from tkinter import filedialog

def set_appearance_and_theme():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

def select_pptx_file():
    file_path = filedialog.askopenfilename(
        title="Select a .pptx file",
        filetypes=[("PowerPoint files", "*.pptx")]
    )
    if file_path:
        label.configure(text='SUCCESS: Selected PowerPoint file', font=("Helvetica", 24))
        create_summurai_button()
    else:
        label.configure(text='No file selected', font=("Helvetica", 24))

def create_summurai_button():
    button_summurai = customtkinter.CTkButton(master=frame, text="SummurAI", command=placeholder)
    button_summurai.pack(pady=20, padx=0)

def placeholder():
    print("Debug")
    # Add your code here

def main():
    set_appearance_and_theme()

    global root
    root = customtkinter.CTk()
    root.geometry("1200x800")

    global frame
    frame = customtkinter.CTkFrame(master=root)
    frame.pack(pady=0, padx=0, fill="both", expand=True)

    global label
    label = customtkinter.CTkLabel(master=frame, text="Please select a .pptx file", font=("Helvetica", 24))
    label.pack(pady=20, padx=0)

    global button
    button = customtkinter.CTkButton(master=frame, text="Select PowerPoint File", command=select_pptx_file)
    button.pack(pady=20, padx=0)

    global textbox
    textbox = customtkinter.CTkTextbox(master=frame, font=("Helvetica", 14), height=800, width=800)
    textbox.pack(pady=10, padx=0)

    root.mainloop()

if __name__ == "__main__":
    main()
