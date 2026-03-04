import ffmpeg

def convert_video(input_file: str, output_file: str, video_codec: str = 'libx264', audio_codec: str = 'copy'):
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vcodec=video_codec, acodec=audio_codec) 
            .run()
        )
        print('Video conversion successful!')
    except ffmpeg.Error as e:
        print('Error converting video:', e.stderr.decode())

def convert_audio(input_file: str, output_file: str, audio_codec: str = 'mp3'):
    try:
        (
            ffmpeg
            .input(input_file)
            .output(output_file,vn=True, acodec=audio_codec)
            .run()
        )
        print('Audio conversion successful!')
    except ffmpeg.Error as e:
        print('Error converting audio:', e.stderr.decode())
