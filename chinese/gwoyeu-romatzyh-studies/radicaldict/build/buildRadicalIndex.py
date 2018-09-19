RADICALS = "CJKRadicals.txt"
JS_OUTPUT = "../radicalIndex.js"
HTML_OUTPUT = "../index.html"

boundaries = [1, 7, 30, 61, 95, 118, 147, 167, 176, 187, 195, 201, 205, 209, 211, 212, 214]
              
curStrokes = 1
strokeRadCount = 0

with open(RADICALS) as radfile, open(HTML_OUTPUT, 'w') as htmlOut:
    print("<!DOCTYPE html><html><head><meta charset='utf-8'><title>Radical dict</title><style>a { text-decoration: none; } body { font-size: 1.5em; } h1 { font-size: 1.2em; }</style></head><body>", file=htmlOut)
    for line in radfile:
        if line[0] == "#" or len(line) < 3:
            continue
        parts = line.split(";")
        if parts[0].find("'") == -1:
            idx = int(parts[0].strip())
            if idx in boundaries:
                if curStrokes > 1:
                    print("<br><br>", file=htmlOut)
                    strokeRadCount = 0
                print("<b>", curStrokes, "</b> ", file=htmlOut)
                curStrokes += 1
            print("<a href='radical{}.html'>&#x{};</a> ".format(parts[0].strip(), parts[1].strip()), file=htmlOut)
            strokeRadCount += 1
            if strokeRadCount % 21 == 0:
                print("<br>", file=htmlOut)
    print("</body></html>", file=htmlOut)
