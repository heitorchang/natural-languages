(use-modules (srfi srfi-9))
(use-modules (oop goops))
(use-modules (ice-9 rdelim))
(use-modules (ice-9 format))

(use-syntax (ice-9 syncase))

(define *standard-out* (current-output-port))

(define base-dir #f)

(if (equal? (substring (vector-ref (uname) 0) 0 6) "CYGWIN")
    (set! base-dir "/cygdrive/c/Users/Heitor/Desktop/emacs-24.3/bin/meleto/")
    (set! base-dir "/home/heitor/meleto/"))

(define out-filename
  "contents-of-quiz.txt")

(define (question-loop)
  (let ((formatted-question ""))
    (set! formatted-question
          (question-string))
    (if (equal? (substring formatted-question 0 4) "[\"q\"")
        (display "Questions saved to contents-of-quiz.txt.\n\n" *standard-out*)
        (begin 
          (display formatted-question)
          (question-loop)))))

(define (question-string)
  (let ((prompt "")
        (answers '())
        (partials "[]"))
    (format *standard-out* "Question prompt? ~!")
    (set! prompt (string-trim-both (read-line)))

    (format *standard-out* "Answer(s), separated by / ~!")
    (set! answers (delimited-to-array (string-trim-both (read-line))))

    (string-append "[\"" prompt "\", " answers ", " partials "],\n")))

(define (delimited-to-array raw-string)
  (string-append "[\""
                 (string-join
                  (map string-trim-both
                       (string-split (string-trim-both raw-string) #\/))
                  "\", \"")
                 "\"]"))

(define (write-quiz)
  (write-to out-filename
            (question-loop)))
