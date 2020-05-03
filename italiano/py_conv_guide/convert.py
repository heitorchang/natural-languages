HEADER = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="style.css">
  <title>Italian Conversation Guide</title>
</head>
<body>
<div class="toolbar">
Italian Guide
<span class="rt">
<input type="text" placeholder="Search" class="search" size="14">
</span>
</div>

<div class="topspacer">&nbsp;</div>
"""

FOOTER = """</body></html>"""

def buildHTML():
    lines = open("raw.txt", encoding="utf-8").readlines()
    lines = [line.strip() for line in lines if len(line) > 1]
    
    print(lines)
    with open("index.html", 'w', encoding="utf-8") as out:
        print(HEADER, file=out)
        for eng, ita in zip(lines[::2], lines[1::2]):
            print(eng, ita)
            print(processLines(eng, ita), file=out)
        print(FOOTER, file=out)

        
def processLines(eng, ita):
    return f"""
    <div class="line eng">{eng}</div>
    <div class="line ita">{ita}</div>
    <div class="spacer">&nbsp;</div>
    """

if __name__ == "__main__":
    buildHTML()
