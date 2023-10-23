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
    


   

def on_file_drop(event):
    file_path = event.data[1:-1]  
    print(f"File path: {file_path}")
    if file_path.lower().endswith('.pptx'):
        message_label.config(text="SUCCESS", fg="green")
        title.config(state='normal')
        title.delete('1.0', 'end')
        title.insert('end', f"Powerpoint Title: {file_path}")
        title.config(state='disabled')
    else:
        message_label.config(text="FAIL", fg="red")

root = TkinterDnD.Tk()
root.title("SummarAI PowerPoint")
root.geometry('1200x600')

title_label = tk.Label(root, text="SummurAI")
title_label.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

message_label = tk.Label(root, text="Please drop a .pptx file here")
message_label.pack()


bottom_frame = tk.Frame(root, height=100, bg='#cccccc')
bottom_frame.pack(fill='x', side='bottom')


bottom_frame.drop_target_register(DND_FILES)
bottom_frame.dnd_bind('<<Drop>>', on_file_drop)

root.mainloop()


