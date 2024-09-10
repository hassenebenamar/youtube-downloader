# Youtube Downloader

## This is a script that enables you to download Youtube videos and audios (mp4, mp3).

### Requirements

- Python 3.10
- FFMPEG
- PytubeFix

To install Python, please follow the guides on the official Python website.

For FFMPEG, just download it through the official website.

For PytubeFix, you can simply run this command (available through [PytubeFix](https://pypi.org/project/pytubefix/)) :

```console
pip install pytubefix
```

Once you have installed all those requirements (it is recommended to use a virtual environment), you can run the script like this : 

```console
python youtubeDL.py link video/audio itag
```
A list of itags is available at this link [Pytube Filtering Streams](https://pytubefix.readthedocs.io/en/latest/user/streams.html#filtering-streams).

### It is possible that your video will not be usable if you select a certain itag (2160p). <br/> Nonetheless, the code converts the AV01 codec automatically into H264 (unless you change the code).

