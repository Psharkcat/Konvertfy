import ffmpeg
import os

# Codec maps for video formats, audio formats, and image formats.
VIDEO_CODEC_MAP = {
    ".mp4": ("libx264", "aac"),          # software
    ".mkv": ("libx264", "aac"),          # software
    ".webm": ("libvpx-vp9", "libopus"),  # software
    ".avi": ("libxvid", "mp3"),          # software
    ".mov": ("libx264", "aac"),          # software

    # hardware accelerated (NVIDIA, Intel, AMD)
    ".mp4_hw": ("h264_nvenc", "aac"),    # NVIDIA
    ".mp4_qsv": ("h264_qsv", "aac"),     # Intel QuickSync
    ".mp4_vaapi": ("h264_vaapi", "aac"), # Intel/AMD VAAPI on Linux
    ".mkv_hw": ("hevc_nvenc", "aac"),    # NVIDIA HEVC
    ".webm_hw": ("vp8_vaapi", "libopus") # VAAPI VP8
}
AUDIO_CODEC_MAP = {
    ".mp3": "libmp3lame", 
    ".wav": "pcm_s16le",
    ".aac": "aac",
    ".flac": "flac",
    ".ogg": "libvorbis"
}
IMAGE_CODEC_MAP = { 
    ".jpg": "mjpeg",
    ".jpeg": "mjpeg",
    ".png": "png",
    ".webp": "libwebp",
    ".bmp": "bmp",
    ".tiff": "tiff"
}


def convert_video(input_file: str, output_file: str, video_codec: str = "", audio_codec: str = ""):
    if video_codec == "" or audio_codec == "": # If either codec is not specified, determine them based on the output file extension.
            ext = os.path.splitext(output_file)[1].lower()
            video_codec, audio_codec = VIDEO_CODEC_MAP.get(ext, ("libx264", "aac"))
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec=video_codec, acodec=audio_codec) 
            .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )
        print('Video conversion successful!')
    except ffmpeg.Error as e:
        print('Error converting video:', e.stderr.decode())

def convert_audio(input_file: str, output_file: str, audio_codec: str = 'mp3'):
    if audio_codec == "": # If audio codec is not specified, determine it based on the output file extension.
            ext = os.path.splitext(output_file)[1].lower()
            audio_codec = AUDIO_CODEC_MAP.get(ext, "libmp3lame")
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file,vn=True, acodec=audio_codec)
            .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )
        print('Audio conversion successful!')
    except ffmpeg.Error as e:
        print('Error converting audio:', e.stderr.decode())

def convert_image(input_file: str, output_file: str, image_codec: str = ""):
    if image_codec == "": # If image codec is not specified, determine it based on the output file extension.
        ext = os.path.splitext(output_file)[1].lower()
        image_codec = IMAGE_CODEC_MAP.get(ext, "png")

    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec=image_codec, frames=1)
            .run(overwrite_output=True, capture_stdout=True, capture_stderr=True)
        )
        print("Image conversion successful!")
    except ffmpeg.Error as e:
        print("Error converting image:", e.stderr.decode())
