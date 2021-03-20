import os
from itertools import chain
from glob import glob

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        f = open(filename, 'r')
        text = f.read()
        
        lines = [text.lower() for line in filename]
        with open(filename, 'w') as out:
            out.writelines(lines)