# Given a book name and a raw text file with phrases, generate its public HTML

import os
from config import LOCAL_ROOT, VERBOSE

def readcontents(book):
    # Parse contents.py into a dictionary
    contentsdict = {}
    prevlink = {}
    nextlink = {}
    indexlink = {}
    
    lines = open(LOCAL_ROOT + "books/{}/contents.txt".format(book), encoding="utf-8").readlines()

    basenames = []
    
    for i, line in enumerate(lines):
        parts = line.split(" ")
        basenames.append(parts[0].split('.')[0])

        basename = basenames[-1]
        
        contentsdict[basename + ".txt"] = " ".join(parts[1:])
        contentsdict[basename + "_py.txt"] = " ".join(parts[1:])
        contentsdict[basename + "_py_s.txt"] = " ".join(parts[1:])
        indexlink[basename + ".txt"] = "index.html"
        indexlink[basename + "_py.txt"] = "index_py.html"
        indexlink[basename + "_py_s.txt"] = "index_py_s.html"
        
    for i in range(len(basenames)):
        basename = basenames[i]

        if i == 0:
            prev = 'index'
        else:
            prev = basenames[i-1]

        if i == len(lines) - 1 or not os.path.exists(LOCAL_ROOT + "books/{}/raw/{}.txt".format(book, basenames[i+1])):
            nextname = 'index'
        else:
            nextname = basenames[i+1]
            
        prevlink[basename + ".txt"] = prev + '.html'
        prevlink[basename + "_py.txt"] = prev + '_py.html'
        prevlink[basename + "_py_s.txt"] = prev + '_py_s.html'

        nextlink[basename + ".txt"] = nextname + '.html'
        nextlink[basename + "_py.txt"] = nextname + '_py.html'
        nextlink[basename + "_py_s.txt"] = nextname + '_py_s.html'
        
    return contentsdict, prevlink, nextlink, indexlink


def raw2html(book, rawfile):
    contentsdict, prevlink, nextlink, indexlink = readcontents(book)
    
    fname = "{}books/{}/raw/{}".format(LOCAL_ROOT, book, rawfile)
    
    raw = open(fname, encoding="utf-8").read()
    raw = raw.replace("---", "--")
    
    phrases = raw.split("--")
    if len(phrases[-1].strip()) < 1:
        phrases = phrases[:-1]

    htmlname = "{}public_html/{}/{}".format(LOCAL_ROOT, book, rawfile[:-4] + '.html')

    if VERBOSE:
        print("    Creating HTML for", contentsdict[rawfile])
    
    with open(htmlname, 'w', encoding="utf-8") as out:
        topichtml = open("{}templates/topic.html".format(LOCAL_ROOT), encoding="utf-8").read()
        
        jsraw = 'const raw = [\n'
        
        for i, phrase in enumerate(phrases, 1):
            phraselines = phrase.strip().split("\n")
            english = phraselines[0]
            jsraw += '[`{}`, `\n'.format(english)

            chars = phraselines[1:]

            for char in chars:
                jsraw += '{}\n'.format(char)

            jsraw += '`],\n'
        jsraw += '];'
        
        print(topichtml % {'topic': contentsdict[rawfile], 'jsraw': jsraw, 'prev': prevlink[rawfile], 'next': nextlink[rawfile], 'indexlink': indexlink[rawfile]}, file=out)

        
