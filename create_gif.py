#!/usr/bin/env python

import os
import sys

directory = "./"
if len(sys.argv) > 1:
    directory = sys.argv[1]

files = os.listdir(directory)
pdf_files = [f for f in files if "darts.pdf" in f]
file_lengths = [len(f) for f in pdf_files]
max_file_length = max(file_lengths)
print "%s pdf files found" % len(pdf_files)

print "Renaming files"
for f in pdf_files:
    os.rename(f, (max_file_length - len(f)) * "0" + f)

print "Creating rain_drop_animation.gif"
os.system("convert -delay 10 *.pdf rain_drop_animation.gif")
