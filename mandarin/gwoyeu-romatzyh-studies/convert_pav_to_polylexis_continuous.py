import sys, os, re
from convert import convert_word

# Source has 6800 lines

SOURCE_FILE = "c:/Users/Heitor/Desktop/code/natural-languages/mandarin/captain_planet_pav/continuousflash.txt"
DEST_DIR = "c:/Users/Heitor/Desktop/code/natural-languages/mandarin/gwoyeu-romatzyh-studies/polylexis/pav/continuous/"


if __name__ == "__main__":
    PAV_PATTERN = re.compile(r'\[PAVC-\d{3}\]')

    line_num = 1
    fout = None
    with open(SOURCE_FILE, encoding="utf-8") as fin:
        for line in fin:
            if line_num % 200 == 1:
                if fout:
                    fout.close()
                fname = DEST_DIR + "pav_{:04d}_{:04d}.txt".format(line_num, line_num+199)
                print("Writing to", fname)
                fout = open(fname, 'w', encoding="utf-8")
                print(fname.replace(".txt", ""), file=fout)
                print("===", file=fout)
                print("Write in GR.", file=fout)
                print("===", file=fout)
                
            if len(line) < 5 or line.startswith("//"):
                continue
            zh, py, en = line.split("\t")
            py = py.strip()
            en = PAV_PATTERN.sub("", en)
            en = en.strip()
            en = en.replace('"', "'")
            gr = convert_word(py)
            print(f"{en}*{gr}", file=fout)

            line_num += 1
