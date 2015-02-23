import pysrt
import fileinput
from glob import glob
from moviepy.editor import *
import random
import os.path

words = "Just a few words to look for".lower().split()
maximum = 20

with open("all.srt", "w") as final:
    for file in glob("*.srt"):
        with open(file) as part:
            for line in part:
                final.write(line)
subtitles = open("all.srt").read().lower()
count = 1

for word in words:
	print "Looking for", word
	if word in subtitles:
		prevfile = "all.srt"
		written = 0
		for file in glob("*.srt"):
			if file != prevfile:
				#print "| Reading", file
				subs = pysrt.open(file)
				indices = [i for i, x in enumerate(subs) if word in x.text]
				video = file.replace(".en.srt", ".mp4")
				for index in indices:
					if not written > maximum:
						if not os.path.isfile("out/"+str(count)+"_"+word+str(written)+".mp4"):
							clip = VideoFileClip(video).subclip(subs[index].start.minutes*60+
								subs[index].start.seconds,
								subs[index].end.minutes*60+subs[index].end.seconds)
							clip.to_videofile("out/"+str(count)+"_"+word+str(written)+".mp4")
					written+=1
				prevfile = file
		count+=1
	else:
		print "| Failed!"
		with open("failed.txt", "a") as f:
			f.write(word)
