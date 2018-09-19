<?php

// $page_title appears on top and as the browser title

// generateQuizJS("QUIZ INSTRUCTIONS",

// each line in the array is
//
// ["", [""], []],
// ["PROMPT IN MAIN LANGUAGE", ["ANSWER 1", "ANSWER 2", ...], []],
// 
// the last array contains "partial (incorrect)" responses

// Run "interactively-write-quiz.scm" in Guile and call (write-quiz)

$page_title = "Dias da semana";

$quiz_js = generateQuizJS("Traduza para grego. Inclua o artigo (ο, η, το)",
                          [
                            // ["", [""], []],
                            // insert contents-of-quiz.txt here
                            ["domingo", ["η Κυριακή"], []],
                            ["segunda-feira", ["η Δευτέρα"], []],
                            ["terça-feira", ["η Τρίτη"], []],
                            ["quarta-feira", ["η Τετάρτη"], []],
                            ["quinta-feira", ["η Πέμπτη"], []],
                            ["sexta-feira", ["η Παρασκευή"], []],
                            ["sábado", ["το Σάββατο"], []],

                          ]);
