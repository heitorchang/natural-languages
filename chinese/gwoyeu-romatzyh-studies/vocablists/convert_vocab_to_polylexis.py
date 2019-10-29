# convert gr vocablists to polylexis gr
# create a folder called polylexis in the source folder

from glob import glob
import sys
import os

def convert_line(line):
    if len(line.strip()) < 2:
        return ""
    if ";" not in line:
        raise ValueError("; not found, aborting")
    parts = list(map(str.strip, line.split(";")))
    return f"{parts[2]}*{parts[1]}"

def convert_vocablist(filename):
    with open(filename, encoding="utf-8") as infile, open(os.path.dirname(filename) + "/polylexis/" + os.path.basename(filename), 'w', encoding="utf-8") as outfile:
        for line in infile:
            print(convert_line(line), file=outfile)

def convert_directory(directory):
    files = glob(directory + "*")
    for fname in files:
        if os.path.basename(fname)[0].isdigit():
            print("Processing", fname)
            convert_vocablist(fname)


if __name__ == "__main__":
    convert_directory(sys.argv[1])
