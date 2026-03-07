from util import converter

if __name__ == "__main__":
    input_file = "idk.mp4"
    output_file = "output_v.webm"
    print("Converting video...")
    converter.convert_video(input_file, output_file)