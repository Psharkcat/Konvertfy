import ffmpeg
import os


VIDEO_CODEC_MAP = {
    ".mp4": ("libx264", "aac"),
    ".mkv": ("libx264", "aac"),
    ".webm": ("libvpx-vp9", "libopus"),
    ".avi": ("libxvid", "mp3"),
    ".mov": ("libx264", "aac")
}

AUDIO_CODEC_MAP = {
    ".mp3": "libmp3lame",
    ".wav": "pcm_s16le",
    ".aac": "aac",
    ".flac": "flac",
    ".ogg": "libvorbis"
}

def convert_video(input_file: str, output_file: str, video_codec: str = "", audio_codec: str = ""):
    if video_codec == "" or audio_codec == "":
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
    if audio_codec == "":
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
