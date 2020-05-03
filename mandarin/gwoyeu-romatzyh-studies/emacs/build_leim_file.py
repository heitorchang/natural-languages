# Script to parse cedict_ts.u8 and generate Emacs .el file

# See cedict_filter.py

HEADER = """
;; Quail package chinese

(require 'quail)
(quail-define-package "chinese-gwoyeu-romatzyh-simplified" "Chinese" "GRS"
t
"Gwoyeu Romatzyh input with simplified characters."

'(("\C-?" . quail-delete-last-char)

(" " . quail-select-current)
([return] . quail-select-current))

;; ("." . quail-next-translation)
;; (">" . quail-next-translation)
;;("," . quail-prev-translation)
;;("<" . quail-prev-translation))

nil nil nil nil)

(quail-define-rules
 
;; Punct-b5..el
("!" "！")

("," "，")
("." "。")
(":" "︰")
(";" "；")
("?" "？")
"""

FOOTER = """
)

(provide 'grsimp)
"""

# ;; Single characters
# ("hwa" "华划滑") 


# ;; CC-CEDICT words
# ("shiehshieh" ["泄瀉" "洩瀉"])

CEDICT = "cedict_ts.u8"


