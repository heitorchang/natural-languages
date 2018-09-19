import re
import os

os.chdir('c:\\Users\\Heitor\\Desktop\\emacs-24.3\\bin\\chinese\\gwoyeu-romatzyh-studies\\emacs')

import sys
sys.path.append('..')

from collections import defaultdict

from convert import convert_syllable

CEDICT = "cedict_ts.u8"
# CEDICT = "cedict_short.txt"
OUTPUT = "grsimp.el"

FREQ = "frequency.txt"
FREQUENCY_CUTOFF = 1500

# build frequency list

freq = {}

# freq_line_ct = 1

with open(FREQ, encoding='utf-8') as freq_txt:
    for line in freq_txt:
        # print(freq_line_ct)
        parts = line.split()
        freq[parts[1]] = int(parts[0])
        # freq_line_ct += 1

def getFreq(char):
    try:
        # print(freq[char])
        return freq[char]
    except:
        return FREQUENCY_CUTOFF + 1

def wordIsCommon(word):
    word_ok = True
    for char in word:
        if getFreq(char) > FREQUENCY_CUTOFF:
            word_ok = False
            break
    return word_ok
    
            
# index of chinese characters. 0 = Traditional, 1 = Simplified
CHINESE_INDEX = 1

def countSyls(line):
    # count the number of syllables in line
    pinyin_pat = re.compile(r'\[.*?\]')
    s = pinyin_pat.search(line)
    return len(s.group().split())

def getPinyin(line):
    pinyin_pat = re.compile(r'\[.*?\]')
    s = pinyin_pat.search(line)
    return s.group()[1:-1]

# single character and multi-character entries

SINGLE = defaultdict(set)
MULTI = defaultdict(set)

# Script to parse cedict_ts.u8 and generate Emacs .el file

HEADER = """
;; Quail package chinese

(require 'quail)
(quail-define-package "chinese-gwoyeu-romatzyh-simplified" "Chinese" "GRS"
t
"Gwoyeu Romatzyh input with simplified characters."

'(("\C-?" . quail-delete-last-char)

(" " . quail-select-current)
([return] . quail-select-current))

;; ("." . quail-next-translation)
;; (">" . quail-next-translation)
;;("," . quail-prev-translation)
;;("<" . quail-prev-translation))

nil nil nil nil)

(quail-define-rules
 
;; Punct-b5..el
("!" "！")

("," "，")
("." "。")
(":" "︰")
(";" "；")
("?" "？")
"""

FOOTER = """
)

(provide 'grsimp)
"""

if __name__ == "__main__":
    with open(CEDICT, encoding="utf-8") as IN, open(OUTPUT, 'w', encoding="utf-8") as OUT:
        # ignore character variant lines
        skip_markers = ['Japanese variant of', 'old variant of', '/variant of']
        for line in IN:
            found_marker = False
            for marker in skip_markers:
                if line.find(marker) > -1:
                    found_marker = True
                    break

            if not found_marker:
                # get Chinese
                chinese = line.split()[CHINESE_INDEX]

                # check number of characters
                py = getPinyin(line)
                num_syls = len(py.split())
                if num_syls <= 2:
                    gr = ''.join([convert_syllable(syl) for syl in py.split()])
                    
                    if num_syls == 1:
                        SINGLE[gr].add(chinese)
                    else:
                        MULTI[gr].add(chinese)
        # build .el file

        print(HEADER, file=OUT)

        for c in SINGLE:
            print('("{}" "{}")'.format(c, ''.join(sorted(SINGLE[c], key=getFreq))), file=OUT)

        for c in MULTI:
            # check that all characters' frequencies are less than 1200
            words = MULTI[c]

            ok_words = list(filter(wordIsCommon, words))
            if len(ok_words) > 0:
                print('("{}" [{}])'.format(c, ' '.join(['"' + word + '"' for word in ok_words])), file=OUT)

        print(FOOTER, file=OUT)

def test():
    pass
                
