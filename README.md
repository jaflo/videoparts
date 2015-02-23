# videoparts.py
Python script to collects clips of video containing specified words. Requires [pysrt](https://pypi.python.org/pypi/pysrt) and [moviepy](http://zulko.github.io/moviepy/).

Put python script in folder with videos and SRT files, each video file (`example.mp4`) having a counterpart with similar file name (`example.en.srt`) ending with `.en.srt`. Change `words` on line 8 to the words you are looking for, separated by a space. Change `maximum` to be the maximum number of occurences of each word to look for.

videoparts will output videos in the folder `out` using the following format:

| # of word | _ | word | occurance | .mp4 |
|-----------|---|------|-----------|------|
| 1 | _ | just | 0 | .mp4 |
| 1 | _ | just | 1 | .mp4 |
| 2 | _ | a | 0 | .mp4 |
| 3 | _ | few | 0 | .mp4 |

and so on
