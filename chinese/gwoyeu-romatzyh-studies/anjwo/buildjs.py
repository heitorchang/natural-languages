"""
Take the downloaded CEDICT text file as input and generate a
JS dictionary object.

Use the structure of cedict-interf
"""

import sys
import re

sys.path.append('/home/heitor/chinese/gwoyeu-romatzyh-studies/')

from convert import convert_syllable

IN_FILENAME = "/home/heitor/chinese/gwoyeu-romatzyh-studies/anjwo/cedict.txt"
OUT_FILENAME = "/home/heitor/chinese/gwoyeu-romatzyh-studies/anjwo/cedict.js"

def build():
    line_pattern = re.compile(r'(?P<trad>.+?)\s(?P<simp>.+?)\s\[(?P<pinyin>.+?)\]\s(?P<english>.+?)$')
    
    with open(IN_FILENAME) as cedict, open(OUT_FILENAME, 'w') as words_js:
        print("var words = [", file=words_js)
        
        for line in cedict:
            line = line.replace('"', "'")
            m = line_pattern.search(line)
            try:
                trad, simp = m.group("trad"), m.group("simp")
                pinyin, english = m.group("pinyin"), m.group("english")
                if (english.find('/variant') > -1 or
                    english.find('/old var') > -1 or
                    english.find('/Japanese var') > -1 or
                    english.find('/archaic var') > -1):
                    continue
                if len(trad) <= 4 and pinyin[0].islower():
                    print("\"{}\"".format(line.strip()), file=words_js, end=",\n")
            except AttributeError:
                raise ValueError("Could not parse " + line)

        # end words array
        print("];", file=words_js)
def test():
    build()
