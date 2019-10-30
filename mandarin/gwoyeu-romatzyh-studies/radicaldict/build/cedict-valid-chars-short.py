cedict = [
"% % [pa1] /percent (Tw)/",
"21三體綜合症 21三体综合症 [er4 shi2 yi1 san1 ti3 zong1 he2 zheng4] /trisomy/Down's syndrome/",
"3C 3C [san1 C] /abbr. for computers, communications, and consumer electronics/China Compulsory Certificate (CCC)/",
"AA制 AA制 [A A zhi4] /to split the bill/to go Dutch/",
"AB制 AB制 [A B zhi4] /to split the bill (where the male counterpart foots the larger portion of the sum)/(theater) a system where two actors take turns in acting the main role, with one actor replacing the other if either is unavailable/",
]

OUTFILE = "/home/heitor/chinese/gwoyeu-romatzyh-studies/radicaldict/build/cedict_charsonly.txt"

validchars = set()

for line in cedict:
    trad = line.split()[0]
    validchars.update(set(trad))

with open(OUTFILE, 'w') as OUT:
    print("".join(validchars), end='', file=OUT)
