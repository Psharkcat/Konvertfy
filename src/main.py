import sys
from util import converter

def main():
    args = sys.argv
    
    if len(args) < 2 or args[1] in ("-h", "--help"):
        print("Usage: python main.py -cli <conversion_type> <input_file> <output_file>")
        print("conversion_type: video, audio, or image")
        sys.exit(0)

    if args[1] == "-cli":
        if len(args) != 5:
            print("Error: Invalid number of arguments.")
            print("Usage: python main.py -cli <conversion_type> <input_file> <output_file>")
            sys.exit(1)

        conversion_type = args[2].lower()
        input_file = args[3]
        output_file = args[4]

        if conversion_type == "video":
            converter.convert_video(input_file, output_file)
        elif conversion_type == "audio":
            converter.convert_audio(input_file, output_file)
        elif conversion_type == "image":
            converter.convert_image(input_file, output_file)
        else:
            print(f"Error: '{conversion_type}' is not a valid type (video, audio, image).")
            sys.exit(1)

if __name__ == "__main__":
    main()