import sys
from powerpoint_processor import process_powerpoint
from pptx import Presentation

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        return

    file_path = sys.argv[1]

    # Open the PowerPoint presentation
    prs = Presentation(file_path)
    
    # Call the function from process_powerpoint.py and capture the result
    formatted_data = process_powerpoint(prs)

    # Print the formatted_data
    print(formatted_data)

if __name__ == "__main__":
    main()