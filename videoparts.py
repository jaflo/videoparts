import pysrt
import fileinput
from glob import glob
from moviepy.editor import *
import random
import os.path

words = "Just a few words to look for".lower().split() # the words to look for
maximum = 20 # maximum number of occurrences of each word to look for

with open("all.srt", "w") as final: # merge all files
    for file in glob("*.srt"):
        with open(file) as part:
            for line in part:
                final.write(line)
subtitles = open("all.srt").read().lower() # used later to check if the word exists in any video
count = 1

for word in words: # loop through all words
	print "Looking for", word
	if word in subtitles: # if the word exists at all
		prevfile = "all.srt"
		written = 0
		for file in glob("*.srt"): # go through all srt files
			if file != prevfile: # and make sure we have not already looked at it
				#print "| Reading", file
				subs = pysrt.open(file) # parse the srt-file
				indices = [i for i, x in enumerate(subs) if word in x.text] # get all indices of subs that contain the word we are looking for
				video = file.replace(".en.srt", ".mp4") # get the video file for the srt-file
				for index in indices: # go through each line in the srt-file that contains the word
					if written < maximum: # if we have not already gotten enough clips
						if not os.path.isfile("out/"+str(count)+"_"+word+str(written)+".mp4"): # skip if already exists
							clip = VideoFileClip(video).subclip(subs[index].start.minutes*60+ # convert to s from minutes
								subs[index].start.seconds,
								subs[index].end.minutes*60+subs[index].end.seconds)
							clip.to_videofile("out/"+str(count)+"_"+word+str(written)+".mp4") # save the subsection
					written+=1
				prevfile = file # don't repeat search
		count+=1
	else:
		print "| Failed!"
		with open("failed.txt", "a") as f: # any issues? log them
			f.write(word)
