import re
from collections import defaultdict

# Global variables
FREQ = defaultdict(int)
CTOGR = defaultdict(set)

def discardPunct(gr):
    pat = re.compile(r'\.?[a-z]*', re.IGNORECASE)
    return pat.match(gr).group()

TESTCASE = "他是我公司的同事，宋先生。;ta shyh woo gong sy .de torng shyh, sonq shian sheng;This is my colleague, Mr. Song"

TESTCASE2 = "好，馬上來;hao, maa shanq lai;OK, coming right up!"

def splitCompound(lst):
    out = []
    for w in lst:
        if w == "sherm":
            out.append("sher")
            out.append(".me")
        elif w == "ig":
            out.append("yih")
            out.append(".ge")
        elif w == "jey":
            out.append("jeh")
            out.append("i")
        elif w == "jeyg":
            out.append("jey")
            out.append(".ge")
        elif w == "neyg":
            out.append("ney")
            out.append(".ge")
        elif w == "tzeem":
            out.append("tzeen")
            out.append(".me")
        elif w == "jell":
            out.append("jeh")
            out.append("erl")
        else:
            out.append(w)
    return out

def processLine(line):
    if line.strip() == "":
        return
    reps = line.split(";")  # split chars, GR, and English
    
    chars = list(reps[0])

    # discard punctuation
    # for c in chars:
    #     print(c, hex(ord(c)))

    chars = list(filter(lambda c: ord(c) == 0x3127 or 0x4e00 <= ord(c) <= 0x9fff or 65 <= ord(c) <= 122, chars))
        
    grs = list(map(discardPunct, reps[1].split()))

    # separate compound GR like sherm, jeyg
    grs = splitCompound(grs)

    # ensure sizes match        
    if len(chars) != len(grs):
        print(line)
        raise ValueError("ERROR: Length of Chars and GRs don't match", line)

    for i in range(len(chars)):
        FREQ[chars[i]] += 1
        CTOGR[chars[i]].add(grs[i])

def swapGRandC(d):
    # swap character and GR keys and values
    grToC = defaultdict(set)
    for c in d:
        for g in d[c]:
            grToC[g].add(c)
    return grToC

def processFile(fname):
    print(fname)
    with open(fname) as fin:
        for line in fin:
            processLine(line)

def processList(fname):
    with open(fname) as fin:
        for line in fin:
            processFile(line.strip())

def filterCommon(freq, times):
    # keep only chars occurring more or equal than TIMES times
    return list(filter(lambda ch: freq[ch] >= times, freq))
            
def test():
    processList("/home/heitor/chinese/gwoyeu-romatzyh-studies/vocablists/compile/vocablist_files.txt")
    # processLine(TESTCASE2)
    # processFile("/home/heitor/chinese/gwoyeu-romatzyh-studies/vocablists/chinese-made-easy/0004_change_of_tones.txt")
    # testeql(discardPunct(".le,"), ".le")
    # testeql(discardPunct("mha"), "mha")
    # testeql(splitCompound(["woo", "jeyg"]), ["woo", "jey", ".ge"])
