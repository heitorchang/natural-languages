import os
from glob import glob
import subprocess

import gr2py
import trad2simp
import sent2raw
from config import LOCAL_ROOT
from render import raw2html

if __name__ == "__main__":
    print("Building Phrasebooks from", LOCAL_ROOT)
    print()

    index_template = open('{}templates/index.html'.format(LOCAL_ROOT), encoding="utf-8").read()
    
    book_links = []
    book_links_py = []
    book_links_py_s = []
    
    book_index_template = open('{}templates/bookindex.html'.format(LOCAL_ROOT), encoding="utf-8").read()
    
    # Traverse books/ directory
    for d in glob(LOCAL_ROOT + 'books/*'):
        d = d.replace('\\', '/')
        dir_name = d.split('/')[-1]
    
        print("  In", '/'.join(d.split('/')[-2:]))

        # Convert sentences to raw
        for s in glob(d + '/sentences/*'):
            sent2raw.convert(s)

        book_links.append('<a href="{}"><div class="booklink">{}</div></a>'.format(dir_name + "/index.html", dir_name.replace("-", " ").title()))
        book_links_py.append('<a href="{}"><div class="booklink">{}</div></a>'.format(dir_name + "/index_py.html", dir_name.replace("-", " ").title()))
        book_links_py_s.append('<a href="{}"><div class="booklink">{}</div></a>'.format(dir_name + "/index_py_s.html", dir_name.replace("-", " ").title()))

        phrases_links = []
        phrases_links_py = []
        phrases_links_py_s = []

        with open(LOCAL_ROOT + 'books/{}/contents.txt'.format(dir_name), encoding='utf-8') as contents_file:
            for topic_line in contents_file:
                topic_parts = topic_line.split(" ")
                topic_filename = topic_parts[0]
                if os.path.exists(LOCAL_ROOT + 'books/{}/raw/{}'.format(dir_name, topic_filename)):
                    phrases_links.append('<li><a href="{}">{}</a></li>'.format(topic_filename.replace(".txt", ".html"), " ".join(topic_parts[1:])))
                    phrases_links_py.append('<li><a href="{}">{}</a></li>'.format(topic_filename.replace(".txt", "_py.html"), " ".join(topic_parts[1:])))
                    phrases_links_py_s.append('<li><a href="{}">{}</a></li>'.format(topic_filename.replace(".txt", "_py_s.html"), " ".join(topic_parts[1:])))
        
        if not os.path.exists(LOCAL_ROOT + 'public_html/' + dir_name):
            os.makedirs(LOCAL_ROOT + 'public_html/' + dir_name)
            
        # Traverse book/raw/ directory
        for r in glob(d + '/raw/*'):
            r = r.replace('\\', '/')
            raw_name = r.split('/')[-1]

            # print("    Loading raw file", raw_name)
            if '_py' not in raw_name:
                # converts raw GR text to Pinyin
                gr2py.convert(r)

        # convert all raw, including ones created above
        for r in glob(d + '/raw/*'):
            r = r.replace('\\', '/')
            raw_name = r.split('/')[-1]
            raw2html(dir_name, raw_name)

        with open(LOCAL_ROOT + "public_html/" + dir_name + "/index.html", 'w', encoding="utf-8") as out:
            print(book_index_template % {'index_version': 'index', 'phrases_links': "".join(phrases_links), 'book_title': dir_name}, file=out)

        with open(LOCAL_ROOT + "public_html/" + dir_name + "/index_py.html", 'w', encoding="utf-8") as out:
            print(book_index_template % {'index_version': 'index_py', 'phrases_links': "".join(phrases_links_py), 'book_title': dir_name}, file=out)

        with open(LOCAL_ROOT + "public_html/" + dir_name + "/index_py_s.html", 'w', encoding="utf-8") as out:
            print(book_index_template % {'index_version': 'index_py_s', 'phrases_links': "".join(phrases_links_py_s), 'book_title': dir_name}, file=out)
            
        # print()

    with open(LOCAL_ROOT + "public_html/index.html", 'w', encoding="utf-8") as out:
        print(index_template % {'version': 'Gwoyeu Romatzyh, Traditional characters', 'book_links': "".join(book_links)}, file=out)

    with open(LOCAL_ROOT + "public_html/index_py.html", 'w', encoding="utf-8") as out:
        print(index_template % {'version': 'Pinyin, Traditional characters', 'book_links': "".join(book_links_py)}, file=out)

    with open(LOCAL_ROOT + "public_html/index_py_s.html", 'w', encoding="utf-8") as out:
        print(index_template % {'version': 'Pinyin, Simplified characters', 'book_links': "".join(book_links_py_s)}, file=out)


    # convert *_py.html to simplified
    print("  Converting existing *_py.html to simplified...")
        
    # Get book names
    for d in glob(LOCAL_ROOT + 'books/*'):
        d = d.replace('\\', '/')
        dir_name = d.split('/')[-1]

        for py_html in glob(LOCAL_ROOT + 'public_html/{}/*_py.html'.format(dir_name)):
            py_html = py_html.replace('\\', '/')
            if "index" not in py_html:
                trad2simp.convert(py_html)
