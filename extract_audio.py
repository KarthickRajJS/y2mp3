import sys,time
from moviepy.editor import *

import pytube, sys
link = sys.argv[1]
filename = sys.argv[2] 
yt = pytube.YouTube(link)
stream = yt.streams.filter(file_extension = 'mp4').first()
stream.download(filename = filename)
time.sleep(2)
video = VideoFileClip(filename+".mp4")
audio = video.audio
audio.write_audiofile(filename + ".mp3") 