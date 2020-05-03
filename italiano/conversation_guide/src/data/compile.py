# Join all raw text files into processed.js

import re

if __name__ == "__main__":
    processed = "const processedData = [\n"
    order = eval(re.search(r'(\[.*\])', open('order.js', encoding="utf-8").readline()).group(0))

    with open('processed.js', 'w', encoding="utf-8") as out:

        for category in order:
            try:
                lines = open(category.replace(" ", "_") + ".txt", encoding="utf-8").readlines()
                lines = [line.strip() for line in lines if len(line) > 1]
                for eng, ita in zip(lines[::2], lines[1::2]):
                    processed += '["{}", "{}", "{}"],'.format(category, eng, ita)
            except FileNotFoundError:
                print("Category", category, "does not exist.")

        processed += "];\nexport { processedData };"

        print(processed, file=out)
