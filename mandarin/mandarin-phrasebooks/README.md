# Mandarin Phrasebooks

A collection of phrases in English, Mandarin characters and romanization.

## Layout

```
mandarin-phrasebooks/
 |
 +-- gr2py.py  # converts a text file in Gwoyeu Romatzyh to Pinyin with numbers
 +-- build.py  # traverses the books directory to generate entire public site
 |
 +-- templates/  # Static HTML blocks
 |    |
 |    +-- index.html
 |    +-- header.html
 |    +-- body_top.html
 |    +-- body_bottom.html
 |    
 +-- books/
 |    |
 |    +-- quick-english-conversation/
 |    |    |
 |    |    +-- contents.txt  # used to make dictionary of filenames and titles
 |    |    +-- raw/
 |    |         |
 |    |         +-- greetings.txt
 |    |         +-- goodbye.txt
 |    |         +-- other.txt
 |    |    
 |    +-- another-book/
 |         |
 |         +-- contents.txt
 |         +-- raw/
 |              |
 |              +-- phrases.txt
 |
 +-- public_html/
      |
      +-- index.html
      +-- quick-english-conversation/
      |    |
      |    +-- greetings.html  # traditional and Gwoyeu Romatzyh
      |    +-- goodbye.html
      |    |
      |    +-- greetings_py.html  # traditional and Pinyin
      |    +-- greetings_py_s.html  # simplified and Pinyin
      |
      +-- another-book/
           |
           +-- topic.html
           +-- topic_py.html
           +-- topic_py_s.html
```

## Adding content

Data should be text files placed in the `sentences/` directories inside each `books/book-name/` directory.

The format is:
```
English phrase;Gwoyeu Romatzyh;Characters
English phrase 2;Gwoyeu Romatzyh 2;Characters 2
```

Punctuation in Gwoyeu Romatzyh must be separated by spaces. Typing Gwoyeu Romatzyh first ensures the right pronunciation is used when typing characters.

`contents.txt` should be:

```
Section Title;section.txt
Section 2 Title;section2.txt
```

## Building

Run `python build.py` in the root directory.
