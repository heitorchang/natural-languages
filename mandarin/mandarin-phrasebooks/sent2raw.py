# Convert English;GR;Character formatted files to raw format

import glob
import re

def convert(inputfilename):
    inputfilename = inputfilename.replace('\\', '/')
    outputfilename = inputfilename.replace('sentences/', 'raw/')

    with open(inputfilename, encoding="utf-8") as inp, open(outputfilename, 'w', encoding="utf-8") as out:
        for line in inp:
            line = line.strip()
            if len(line) < 1:
                continue

            try:
                en, gr, ch = line.split(";")
            except ValueError:
                print("Error splitting line", line)
                exit(1)
                
            print(en, file=out)

            # Add punctuation
            if ch[-1] == "。" and gr[-1] != ".":
                gr += "."

            if ch[-1] == "?" and gr[-1] != "?":
                gr += "?"
            
            if ch[-1] == "﹖" and gr[-1] != "?":
                gr += "?"
            
            if ch[-1] == "!" and gr[-1] != "!":
                gr += "!"
            
            if ch[-1] == "﹗" and gr[-1] != "!":
                gr += "!"
            
            # Split [a-z]? to [a-z] ?, [a-z], to [a-z] , and [a-z]. to [a-z] .
            punctpat = re.compile(r'([a-z])([\.,?!])')

            gr = punctpat.sub(r'\1 \2', gr)
            gr = gr.replace("sherm", "shern .me")
            gr = gr.replace("tzeem", "tzeen .me")
            gr = gr.replace("ig", "yih .ge")

            grlst = gr.split(" ")

            if len(ch) != len(grlst):
                raise ValueError("Char, GR mismatch", gr, inputfilename, ch, gr)
            for c, g in zip(ch, grlst):
                print(g, c, file=out)

            print("--", file=out)
