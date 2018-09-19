<?php

// $page_title appears on top and as the browser title

// generateQuizJS("QUIZ INSTRUCTIONS",

// each line in the array is
//
// ["", [""], []],
// ["PROMPT IN MAIN LANGUAGE", ["ANSWER 1", "ANSWER 2", ...], []],
// 
// the last array contains "partial (incorrect)" responses

// Load "emacs-write-quiz.el" and call meleto-loop-questions

$page_title = "Expressando-se";

$quiz_js = generateQuizJS("",
                          [
                            // ["", [""], []],
                            // insert questions here
                            ["eu gostaria ...", ["θα ήθελα"], []],
["nós gostaríamos", ["θα θέλαμε"], []],
["você quer ...?", ["θέλεις"], []],
["o senhor tem ...?", ["έχετε"], []],
["tem um ...?", ["υπάρχει ένα"], []],
["tem alguns ...?", ["υπάρχουν καθόλου"], []],
["como ...?", ["πώς"], []],
["por que ...?", ["γιατί"], []],
["quando ...?", ["πότε"], []],
["o que ...?", ["τι"], []],
["onde fica ...?", ["πού είναι"], []],
["onde ficam ...?", ["πού είναι"], []],
["quanto custa isto?", ["πόσο κάνει αυτό"], []],
["o que é isto?", ["τι είναι αυτό"], []],
["o senhor fala inglês?", ["μιλάτε αγγλικά"], []],
["onde ficam os toaletes, por favor?", ["πού είναι οι τουαλέτες, παρακαλώ"], []],
["como vai?", ["πώς είσαι"], []],
["bem, obrigado", ["καλά, ευχαριςτώ"], []],
["muito obrigado", ["ευχαριστώ πολύ"], []],
["não, obrigado", ["όχι, ευχαριστώ"], []],
["sim, por favor", ["ναι, παρακαλώ"], []],
["de nada", ["παρακαλώ"], []],
["até mais tarde", ["θα σε δω αργότερα"], []],
["sinto muito", ["λυπάμαι"], []],

                          ]);
