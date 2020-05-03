from collections import defaultdict

DATA = "/home/heitor/chinese/gwoyeu-romatzyh-studies/radicaldict/build/Unihan_RadicalStrokeCounts.txt"
# DATA = "strokeShort.txt"
OUTFILE = "/home/heitor/chinese/gwoyeu-romatzyh-studies/cedict-interf/strokeContents.js"
VALIDCHARS = "/home/heitor/chinese/gwoyeu-romatzyh-studies/radicaldict/build/cedict_charsonly.txt"

# prepare valid chars
VC = open(VALIDCHARS)
vcs = VC.readline().strip()
VC.close()

vcset = set(vcs)

db = {}

for i in range(1, 214+1):
    db[i] = defaultdict(list)

def convertCode(uni):
    return uni.replace("U+", "&#x") + ";"

with open(DATA) as unihan:
    for line in unihan:
        if line[:2] == "U+":
            parts = line.split('\t')
            if parts[1] == 'kRSKangXi' and chr(int(parts[0][2:], 16)) in vcset:
                rad, strokes = map(int, parts[2].strip().split("."))
                db[rad][strokes].append(convertCode(parts[0]))

def convertToHTML(index, OUT):
    # convertToHTML(196)
    radical = db[index]
    
    strokes = sorted(radical.keys())
    for s in strokes:
        print("<b>", str(s), "</b><br>", end='', file=OUT)
        for c in radical[s]:
            print("<a href='#s' onclick='a(fc(0x{}))'>{}</a>".format(c[3:-1], c), end=" ", file=OUT)

    print("Finished converting", index)

def getRadicalStrokes(index):
    result = ""
    radical = db[index]
    
    strokes = sorted(radical.keys())
    first = True
    for s in strokes:
        if not first:
            result += "<br>"
        first = False
        result += "<b>" + str(s) + "</b> "
        for c in radical[s]:
            result += "<a href='#s' onclick='a(fc(0x{}))'>{}</a> ".format(c[3:-1], c)
    return result
    
with open(OUTFILE, 'w') as OUT:
    print("var strokeContents = {", file=OUT)
    for i in range(1, 214+1):
        print(str(i) + ': "', end="", file=OUT)
        print(getRadicalStrokes(i), end="", file=OUT)
        print('",', file=OUT)

    print("};", file=OUT)
