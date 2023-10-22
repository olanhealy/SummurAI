import os
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD

#script_dir = os.path.dirname(os.path.abspath(__file__))
#rootDir = os.path.join(os.path.dirname(script_dir), "SummurAI", "pptx_files")

# def opening():
    #print("  █████  █   █  ███████   ███████    █   █   ██████   ██████   ██████")
    #print("  █      █   █  █  █  █   █  █   █   █   █   █    █   █    █     ██  ")
    #print("  █      █   █  █  █  █   █  █   █   █   █   █    █   █    █     ██  ")
    #print("  █████  █   █  █  █  █   █  █   █   █   █   █    █   ██████     ██  ")
    #print("      █  █   █  █  █  █   █  █   █   █   █   █        █    █     ██  ")
    #print("      █  █   █  █  █  █   █  █   █   █   █   █        █    █     ██  ")
    # print("  █████  █████  █  █  █   █  █   █   █████   █        █    █   ██████")
    


   
root = tk.Tk()
root.title("SummarAI PowerPoint")
root.geometry('1200x600')  # Note the lowercase 'x'

tlabel = tk.Label(root, text="Title")
tlabel.pack()

title = tk.Text(root, height=1, width =140)

root.mainloop()
   





