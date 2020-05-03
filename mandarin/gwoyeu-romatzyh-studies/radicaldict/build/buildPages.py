from collections import defaultdict

DATA = "Unihan_RadicalStrokeCounts.txt"
# DATA = "strokeShort.txt"
HTML_PREFIX = "../radical"

# Want:
# db[radicalIndex][3] = ['char1', 'char2', ...]

db = {}

for i in range(1, 214+1):
    db[i] = defaultdict(list)

def convertCode(uni):
    return uni.replace("U+", "&#x") + ";"

with open(DATA) as unihan:
    for line in unihan:
        if line[:2] == "U+":
            parts = line.split('\t')
            if parts[1] == 'kRSKangXi':
                rad, strokes = map(int, parts[2].strip().split("."))
                db[rad][strokes].append(convertCode(parts[0]))

def convertToHTML(index):
    # convertToHTML(196)
    radical = db[index]
    
    with open(HTML_PREFIX + str(index) + ".html", 'w') as OUT:
        print('<!DOCTYPE html><html><head><meta charset="utf-8"><title>Radical</title><style>body { font-size: 1.8em; } h1 { font-size: 1.2em; }</style></head><body>', file=OUT)
        strokes = sorted(radical.keys())
        for s in strokes:
            print("<a href='#s" + str(s) + "'>" + str(s) + "</a> ", file=OUT)
        for s in strokes:
            print("<h1 id='s" + str(s) + "'>", str(s), "</h1>", file=OUT)
            for c in radical[s]:
                print(c, end=" ", file=OUT)
            print(file=OUT)
    print("Finished converting", index)

for i in range(1, 214+1):
    convertToHTML(i)

