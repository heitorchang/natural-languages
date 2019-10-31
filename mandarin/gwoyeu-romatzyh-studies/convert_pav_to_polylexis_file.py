import sys, os, re
from convert import convert_word

DEST_DIR = "c:/Users/Heitor/Desktop/code/natural-languages/mandarin/gwoyeu-romatzyh-studies/polylexis/pav/"

if __name__ == "__main__":
    PAV_PATTERN = re.compile(r'\[PAVC-\d{3}\]')
    
    fname = sys.argv[1]
    with open(fname, encoding="utf-8") as fin, open(DEST_DIR + fname, 'w', encoding="utf-8") as fout:
        print(fname.replace(".txt", ""), file=fout)
        print("===", file=fout)
        print("Write in GR.", file=fout)
        print("===", file=fout)
        
        for line in fin:
            if len(line) < 5 or line.startswith("//"):
                continue
            zh, py, en = line.split("\t")
            py = py.strip()
            en = PAV_PATTERN.sub("", en)
            en = en.strip()
            en = en.replace('"', "'")
            gr = convert_word(py)
            print(f"{en}*{gr}", file=fout)
            
