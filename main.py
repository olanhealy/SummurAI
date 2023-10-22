import os

script_dir = os.path.dirname(os.path.abspath(__file__))
rootDir = os.path.join(os.path.dirname(script_dir), "SummurAI", "pptx_files")

def opening():
    print("  █████  █   █  ███████   ███████    █   █   ██████   ██████   ██████")
    print("  █      █   █  █  █  █   █  █   █   █   █   █    █   █    █     ██  ")
    print("  █      █   █  █  █  █   █  █   █   █   █   █    █   █    █     ██  ")
    print("  █████  █   █  █  █  █   █  █   █   █   █   █    █   ██████     ██  ")
    print("      █  █   █  █  █  █   █  █   █   █   █   █        █    █     ██  ")
    print("      █  █   █  █  █  █   █  █   █   █   █   █        █    █     ██  ")
    print("  █████  █████  █  █  █   █  █   █   █████   █        █    █   ██████")

def main():
    opening()
    file_name = input("Please enter the name of the PowerPoint file you wish to SummarAI, followed by .pptx: ")
    search_pptx(file_name)

def search_pptx(file_name):
    print("Searching for pptx file, please make yourself a cup of tea")

    if file_name in os.listdir(rootDir):
        print("File Found. Let me SUMMARAI")
    else:
        print("ERROR: File cannot be found. Please try again so we can SUMMURAI")

if __name__ == "__main__":
    main()
