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

$page_title = "Línguas (Ε. Ε. Μάθημα 5)";

$quiz_js = generateQuizJS("Traduza para grego, sem o artigo (ο, η, το)",
                          [
                            // ["", [""], []],
                            // insert contents-of-quiz.txt here
                            ["grego", ["ελληνικά"], []],
["inglês", ["αγγλικά"], []],
["francês", ["γαλλικά"], []],
["russo", ["ρωσικά"], []],
["alemão", ["γερμανικά"], []],
["espanhol", ["ισπανικά"], []],
["italiano", ["ιταλικά"], []],
["árabe", ["αραβικά"], []],
["albanês", ["αλβανικά"], []],
["português", ["πορτογαλικά"], []],

                          ]);
