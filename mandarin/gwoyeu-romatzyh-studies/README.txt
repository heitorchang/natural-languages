Chinese Studies with Gwoyeu Romatzyh

Emacs Gwoyeu Romatzyh input method, converted from chinese-py-b5

Note: Pinyin was translated halfway by a script and finished manually.
There may be some errors.

Copy the expressions from add-to-dot-emacs.txt to your ~/.emacs file,
replacing the directory with the path where you have saved this
repository.

Restart Emacs and type C-x RET \ to switch input methods

Type 'chinese-gwoyeu-romatzyh'

Enjoy 國語羅馬字輸入!


CC-CEDICT Gwoyeu Romatzyh Simplified Characters version

emacs/ directory contains an input method that uses CC-CEDICT as a
source of words. Words are limited to two characters and top 1500
most frequent characters

Installation:

byte-compile-file grsimp.el

Copy grsimp.elc to the emacs-VERSION/leim/quail/ directory

add to emacs-VERSION/leim/leim-list.el :

(register-input-method
 "chinese-gwoyeu-romatzyh-simplified" "Chinese" 'quail-use-package
 "GRS" "Gwoyeu Romatzyh"
 "quail/grsimp")

Type C-x RET C-\ chinese-gwoyeu-romatzyh-simplified


Alternative method (if the above doesn't work)

Add to .emacs:

(add-to-list 'load-path "/PATH/TO/emacs-25.3/lisp/leim/quail")

in the *scratch* buffer, evaluate
(require 'grsimp)

and wait for a while
