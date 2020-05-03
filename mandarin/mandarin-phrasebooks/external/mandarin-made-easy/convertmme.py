# Convert text files formatted for vocablists to mandarin-phrasebooks format

import glob
import re

def convert(inputfilename):
    with open(inputfilename, encoding="utf-8") as inp, open('raw/' + inputfilename, 'w', encoding="utf-8") as out:
        for line in inp:
            # print(line)
            if len(line.strip()) < 1:
                continue
            
            ch, gr, en = line.split(";")
            if en[-1] != "\n":
                print(en, file=out)
            else:
                print(en, end="", file=out)

            # Add punctuation
            if ch[-1] == "。" and gr[-1] != ".":
                gr += "."

            if ch[-1] == "?" and gr[-1] != "?":
                gr += "?"
            
            if ch[-1] == "!" and gr[-1] != "!":
                gr += "!"
            
            # Split [a-z]? to [a-z] ?, [a-z], to [a-z] , and [a-z]. to [a-z] .
            punctpat = re.compile(r'([a-z])([\.,?!])')

            gr = punctpat.sub(r'\1 \2', gr)
            gr = gr.replace("sherm", "shern .me")
            gr = gr.replace("tzeem", "tzeen .me")
            gr = gr.replace("ig", "yih .ge")

            grlst = gr.split(" ")

            if len(ch) != len(grlst):
                raise ValueError("Char, GR mismatch", gr, inputfilename)
            for c, g in zip(ch, grlst):
                print(g, c, file=out)

            print("--", file=out)


PRODUCTION = True

if __name__ == "__main__":
    if PRODUCTION:
        for f in glob.glob("*.txt"):
            print("Converting file", f)
            convert(f)
