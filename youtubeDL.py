import sys
import subprocess
from pytubefix import YouTube
from moviepy.editor import *


def download_video(link, itag=None):
    video = YouTube(link)

    if not itag:
        # If no itag is provided, get the highest resolution stream
        stream = video.streams.get_highest_resolution()
    else:
        # Get stream by itag (provided by user)
        stream = video.streams.get_by_itag(itag)

    if stream:
        if "av01" in stream.video_codec:
            print("Video uses AV1 codec (av01). Downloading and converting to H.264.")

        # Download the video stream
        file_path = stream.download()
        print(f"Video downloaded successfully: {file_path}")

        # If the video codec is AV1, convert it to H.264
        if "av01" in stream.video_codec:
            convert_av1_to_h264(file_path)
    else:
        print(f"No stream found with itag {itag}")


def convert_av1_to_h264(input_file):
    output_file = input_file.replace('.webm', '_h264.mp4')  # Change extension to .mp4 for H.264

    # Ensure the output file doesn't already exist (auto-increment the filename if necessary)
    base, ext = os.path.splitext(output_file)
    counter = 1
    while os.path.exists(output_file):
        output_file = f"{base}_{counter}{ext}"
        counter += 1

    command = [
        'ffmpeg',
        '-i', input_file,  # Input file
        '-c:v', 'libx264',  # Video codec set to H.264
        '-preset', 'medium',  # Preset for compression speed
        '-crf', '23',  # Constant Rate Factor for quality (23 is a good default)
        '-c:a', 'copy',  # Copy the audio stream without re-encoding
        '-y',  # overwrite
        output_file
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Video converted to H.264 successfully: {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")


def download_audio(link):
    video = YouTube(link)
    stream = video.streams.get_by_itag("251")
    file = stream.download()
    print("Audio downloaded successfully.")
    return file


def convert_webm_to_mp3(input_file):
    print(input_file)
    output_file = input_file.replace('.webm', '.mp3')
    audio = AudioFileClip(input_file)
    audio.write_audiofile(output_file)
    audio.close()
    print("Converted to MP3 successfully.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: script.py <link> <mode> [itag]")
        print("<mode> should be 'video' or 'audio'. If 'video', [itag] is required.")
        sys.exit(1)

    link = sys.argv[1]
    mode = sys.argv[2]

    if mode == "video":
        if len(sys.argv) < 4:
            download_video(link)
        elif len(sys.argv) == 4:
            itag = sys.argv[3]
            download_video(link, itag)
        else:
            sys.exit(1)
    elif mode == "audio":
        file_path = download_audio(link)
        convert_webm_to_mp3(file_path)
    else:
        print("Invalid mode. Use 'video' or 'audio'.")

# to download a video at more than 720p, do this in terminal pytube --itag=137 link or --itag=313 for 2160p - webm
