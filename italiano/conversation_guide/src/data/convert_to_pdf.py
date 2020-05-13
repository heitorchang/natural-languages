# Book order
# files = ['Need to know', 'Numbers', 'Time and date', 'Arrival and departure', 'Money', 'Conversation', 'Getting around', 'Places to stay', 'Communications', 'Sightseeing', 'Shopping', 'Sport and leisure', 'Traveling with children', 'Emergencies', 'Police', 'Health', 'Pharmacy', 'Disabled travelers', 'Eating out', 'Meals and cooking', 'Drinks', 'On the menu', 'Going out', 'Romance'];

# Alphabetical order
files = ['Arrival and departure', 'Communications', 'Conversation', 'Disabled travelers', 'Drinks', 'Eating out', 'Emergencies', 'Getting around', 'Going out', 'Health', 'Meals and cooking', 'Money', 'Need to know', 'Numbers', 'Pharmacy', 'Places to stay', 'Police', 'Romance', 'Shopping', 'Sightseeing', 'Sport and leisure', 'Time and date', 'Traveling with children'];


with open("index_pdf.html", "w", encoding="utf-8") as html:
    print("""<!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <style>
    @font-face {
    font-family: 'NotoSans';
    src: url('notosans.ttf') format('truetype');
    font-style: normal;
    }
    
    body {
    font-family: 'NotoSans';
    margin: 1.2em;
    font-size: 200%;
    }
    
    .sectionlink {
    font-size: 130%;
    display: block;
    text-decoration: none;
    margin: 0.6em;
    }

    .sect {
    font-size: 125%;
    margin: 1em 0;
    padding: 1em 0 1em 0.5em;
    background: #9BF;
    font-weight: bold;
    }

    .sect a {
    text-decoration: none;
    }
    
    .subsect {
    margin: 1em 0;
    padding: 1em 0 1em 0.5em;
    background: #FC8;
    font-weight: bold;
    }

    .eng {
    background: #DEF;
    padding: 0.3em 0.5em;
    font-weight: bold;
    }

    .ita {
    background-color: white;
    padding: 0.3em 0.5em;
    }
    
    .blk {
    page-break-inside: avoid;
    }

    .tit {
    font-size: 2em;
    margin: 0.8em 0 0.4em 0;
    }

    </style>
    </head>
    <body>
    <div id="top" class="tit">ITALIAN PHRASEBOOK</div>
    """, file=html)

    # Table of contents
    for index, name in enumerate(files, 1):
        print('<a href="#sec{}" class="sectionlink">{}. {}</a>'.format(index, index, name), file=html)

    # contents
    for index, name in enumerate(files, 1):
        print('<div id="sec{}" class="sect"><a href="#top">{}. {}</a></div>'.format(index, index, name), file=html)

        lines = open(name.replace(" ", "_") + ".txt", encoding="utf-8").readlines()
        lines = [line.strip() for line in lines if len(line) > 1]
        for eng, ita in zip(lines[::2], lines[1::2]):
            if eng[0] == "*":
                subsect = eng.replace("*", "").strip()
                print(f'<div class="subsect">{subsect}</div>', file=html)
            else:
                print(f'<div class="blk">', file=html)
                print(f'<div class="eng">{eng}</div>', file=html)
                print(f'<div class="ita">{ita}</div>', file=html)
                print('<div class="spacer">&nbsp;</div>', file=html)
                print('</div>', file=html)

    print("""</body></html>""", file=html)
