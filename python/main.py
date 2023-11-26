import customtkinter
from tkinter import filedialog
from pptx import Presentation
from collections import Counter

def set_appearance_and_theme():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    
def get_font_size(paragraph):
    """
    Get the font size of a paragraph in points.
    """
    font_size = None
    if paragraph.runs and paragraph.runs[0].font.size:
        font_size = paragraph.runs[0].font.size.pt
    return font_size

def most_common_font_size(presentation):
    """
    Find the most common font size in a PowerPoint presentation.
    """
    font_sizes = []

    for slide in presentation.slides:
        for shape in slide.shapes:
            if shape.has_text_frame:
                for paragraph in shape.text_frame.paragraphs:
                    font_size = get_font_size(paragraph)
                    if font_size is not None:
                        font_sizes.append(font_size)

    if font_sizes:
        most_common_size = Counter(font_sizes).most_common(1)[0][0]
        return most_common_size
    else:
        return None

# Edit of read.py here in new method
def process_powerpoint_file(file_path, button_summurai):
    formatted_lines = []
    output_text = ""
    prs = Presentation(file_path)

    # Calculate the most common font size
    common_font_size = most_common_font_size(prs)
    
    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    text = run.text
                    font_size = get_font_size(paragraph)
                    line_info = {
                        "text": text,
                        "is_key_text": False,
                        "is_bold": run.font.bold,
                        "is_italic": run.font.italic,
                        "is_underline": run.font.underline,
                    }

                    # Check if the line is Key Text based on font size
                    if font_size is not None and font_size > 1.1 * common_font_size:
                        line_info["is_key_text"] = True

                    # Check if the line is a title based on its position in the slide
                    if shape == slide.shapes[0]:
                        line_info["is_key_text"] = True

                    formatted_lines.append(line_info)

    for line_info in formatted_lines:
        text = line_info["text"]
        is_key_text = line_info["is_key_text"]
        is_bold = line_info["is_bold"]
        is_italic = line_info["is_italic"]
        is_underline = line_info["is_underline"]

        output_text += "\n"
        if is_key_text:
            output_text += f"Key Text: {text}\n"
        else:
            output_text += f"Text: {text}\n"

        if is_bold:
            output_text += "  - Bold\n"
        if is_italic:
            output_text += "  - Italic\n"
        if is_underline:
            output_text += "  - Underline\n"

    textbox.delete("1.0", "end")
    textbox.insert("1.0", output_text)
    print(f"PowerPoint file processed successfully. Content displayed in the textbox.")
    if button_summurai[0]:
        button_summurai[0].configure(state="normal", command=lambda: process_powerpoint_file(file_path, button_summurai))

def select_pptx_file(button_summurai):
    file_path = filedialog.askopenfilename(
        title="Select a .pptx file",
        filetypes=[("PowerPoint files", "*.pptx")]
    )
    if file_path:
        label.configure(text='SUCCESS: Selected PowerPoint file', font=("Helvetica", 24))
        create_summurai_button(file_path, button_summurai)
        if button_summurai[0]:
            button_summurai[0].configure(state="normal", command=lambda: process_powerpoint_file(file_path, button_summurai))
    else:
        label.configure(text='No file selected', font=("Helvetica", 24))

def create_summurai_button(file_path, button_summurai):
    if not button_summurai[0]:
        button = customtkinter.CTkButton(master=frame, text="SummurAI", state="disabled")
        button.pack(pady=20, padx=0)
        button_summurai[0] = button
        print("SummurAI button created")
    else:
        button_summurai[0].configure(command=lambda: process_powerpoint_file(file_path, button_summurai))

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

    global button_summurai
    button_summurai = [None]  
    button = customtkinter.CTkButton(master=frame, text="Select PowerPoint File", command=lambda: select_pptx_file(button_summurai))
    button.pack(pady=20, padx=0)
    print("Select PowerPoint File button created")

    global textbox
    textbox = customtkinter.CTkTextbox(master=frame, font=("Helvetica", 14), height=400, width=800)
    textbox.pack(pady=10, padx=0)

    root.mainloop()

if __name__ == "__main__":
    main()
