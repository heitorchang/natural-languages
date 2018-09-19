;;;; C-return to define functions
;;;; then, M-x meleto-loop-questions

(defun meleto-set-input-to-greek ()
  (interactive)
  (set-input-method 'greek))

(defun meleto-set-input-to-portuguese ()
  (interactive)
  (set-input-method 'portuguese-prefix))

(defun meleto-question-prompt (arg)
  ;; (set-input-method 'greek)
  (interactive
   (list
    (read-string "Question prompt: (C-g to quit) " "" nil nil t)))
  (insert "[\"" arg "\", "))

(defun meleto-answer-prompt (arg)
  ;; (set-input-method 'portuguese-prefix)
  (interactive
   (list
    (read-string "Answers, separated by / " "" nil nil t)))
  (insert (meleto-answers-to-array arg)))

(defun chomp (str)
  "https://www.emacswiki.org/emacs/ElispCookbook#toc6"
  (replace-regexp-in-string (rx (or (: bos (* (any " \t\n")))
                                    (: (* (any " \t\n")) eos)))
                            ""
                            str))

(defun meleto-answers-to-array (raw-string)
  (concat "[\""
          (mapconcat 'identity
                     (mapcar 'chomp (split-string raw-string "/"))
                     "\", \"")
          "\"], []],\n"))

(defun meleto-loop-questions ()
  (interactive
   (loop
    (call-interactively 'meleto-set-input-to-portuguese)
    (call-interactively 'meleto-question-prompt)
    (call-interactively 'meleto-set-input-to-greek)
    (call-interactively 'meleto-answer-prompt))))

;;;; ["", [""], []],
