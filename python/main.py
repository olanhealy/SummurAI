import customtkinter
from tkinter import filedialog
from pptx import Presentation
from collections import Counter

def set_appearance_and_theme():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

def get_font_size(paragraph):
    font_size = None
    if paragraph.runs and paragraph.runs[0].font.size:
        font_size = paragraph.runs[0].font.size.pt
    return font_size

def most_common_font_size(presentation):
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

def process_powerpoint_file(file_path):
    formatted_lines = []
    output_text = ""
    prs = Presentation(file_path)
    
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

                    common_font_size = most_common_font_size(prs)
                    if font_size is not None and font_size > 1.1 * common_font_size:
                        line_info["is_key_text"] = True

                    if shape == slide.shapes[0]:
                        line_info["is_key_text"] = True

                    formatted_lines.append(line_info)

    return formatted_lines

def process_and_save_powerpoint_info(file_path):
    lines_info = process_powerpoint_file(file_path)

    # Find the first key text
    first_key_text = None
    for line_info in lines_info:
        if line_info["is_key_text"]:
            first_key_text = line_info["text"]
            break

    if not first_key_text:
        print("No key text found. Unable to determine file name.")
        return

    # Use the first key text as the name of the output text file
    file_name = f"{first_key_text.replace(' ', '_')}.txt"
    save_path = file_name

    with open(save_path, "w", encoding="utf-8") as file:
        for line_info in lines_info:
            text = line_info["text"]
            is_key_text = line_info["is_key_text"]
            is_bold = line_info["is_bold"]
            is_italic = line_info["is_italic"]
            is_underline = line_info["is_underline"]

            file.write("\n")
            if is_key_text:
                file.write(f"Key Text: {text}\n")
            else:
                file.write(f"Text: {text}\n")

            if is_bold:
                file.write("  - Bold\n")
            if is_italic:
                file.write("  - Italic\n")
            if is_underline:
                file.write("  - Underline\n")

    print(f"PowerPoint file processed successfully. Content saved to {save_path}.")

def select_pptx_file():
    file_path = filedialog.askopenfilename(
        title="Select a .pptx file",
        filetypes=[("PowerPoint files", "*.pptx")]
    )
    if file_path:
        label.configure(text='SUCCESS: Selected PowerPoint file', font=("Helvetica", 24))
        process_and_save_powerpoint_info(file_path)
    else:
        label.configure(text='No file selected', font=("Helvetica", 24))

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
    button_summurai = None
    button = customtkinter.CTkButton(master=frame, text="Select PowerPoint File", command=select_pptx_file)
    button.pack(pady=20, padx=0)
    print("Select PowerPoint File button created")

    global textbox
    textbox = customtkinter.CTkTextbox(master=frame, font=("Helvetica", 14), height=400, width=800)
    textbox.pack(pady=10, padx=0)

    root.mainloop()

if __name__ == "__main__":
    main()
