from pptx import Presentation

prs = Presentation("pptx_files/simple.pptx")

# Define a list to store structured formatting information for each line
formatted_lines = []

# Define a default font size (you can adjust this as needed)
default_font_size = 12

# Specify the output file path
output_file_path = "formatted_lines.txt"

with open(output_file_path, "w", encoding="utf-8") as output_file:
    for slide in prs.slides:
        for shape in slide.shapes:
            if not shape.has_text_frame:
                continue
            for paragraph in shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    text = run.text
                    line_info = {
                        "text": text,
                        "is_heading": False,
                        "is_bold": run.font.bold,
                        "is_italic": run.font.italic,
                        "is_underline": run.font.underline,
                    }
                    # Check if the line is a heading (based on font size)
                    font_size = run.font.size.pt if run.font.size is not None else default_font_size
                    if font_size > 18:  # You can adjust the font size threshold as needed
                        line_info["is_heading"] = True
                    formatted_lines.append(line_info)

    for line_info in formatted_lines:
        text = line_info["text"]
        is_heading = line_info["is_heading"]
        is_bold = line_info["is_bold"]
        is_italic = line_info["is_italic"]
        is_underline = line_info["is_underline"]

        # Write the information to the output file
        with open(output_file_path, "a", encoding="utf-8") as output_file:
            output_file.write("\n")
            if is_heading:
                output_file.write(f"H: {text}\n")
            else:
                output_file.write(f"T: {text}\n")

            if is_bold:
                output_file.write("  - B\n")
            if is_italic:
                output_file.write("  - I\n")
            if is_underline:
                output_file.write("  - U\n")

print(f"Formatted lines information has been saved to {output_file_path}")
