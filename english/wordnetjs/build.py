# Convert CSV files to JS data files

import csv
import json
from collections import defaultdict

SYNSET_IN = "wn_synset.csv"
# SYNSET_IN = "synset_short.csv"
GLOSS_IN = "wn_gloss.csv"
# GLOSS_IN = "gloss_short.csv"

SYNSET_OUT = "synset.js"
GLOSS_OUT = "gloss.js"

s_dict = defaultdict(list)
g_dict = defaultdict(list)

with open(SYNSET_IN, newline='') as s_in:
    s_reader = csv.reader(s_in)
    for row in s_reader:
        # exclude proper names
        if row[0][0].islower():
            s_dict[row[0]].append(row[1])

for k in s_dict:
    s_dict[k].sort()

# glosses
with open(GLOSS_IN, newline='') as g_in:
    g_reader = csv.reader(g_in)
    for row in g_reader:
        g_dict[row[0]].append(row[1])

with open(SYNSET_OUT, 'w') as s_out:
    print('; var synset = ', end='', file=s_out)
    json.dump(s_dict, s_out)

with open(GLOSS_OUT, 'w') as g_out:
    print('; var gloss = ', end='', file=g_out)
    json.dump(g_dict, g_out)
        
def test():
    print("in test")
