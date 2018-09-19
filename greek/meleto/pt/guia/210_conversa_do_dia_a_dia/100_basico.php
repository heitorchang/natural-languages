<?php

// $page_title appears on top and as the browser title

// generateQuizJS("QUIZ INSTRUCTIONS",

// each line in the array is
//
// ["", [""], []],
// ["PROMPT IN MAIN LANGUAGE", ["ANSWER 1", "ANSWER 2", ...], []],
// 
// the last array contains "partial (incorrect)" responses

$page_title = "O básico";

$quiz_js = generateQuizJS("",
                          [
                            // ["", [""], []],
                            ["você (formal)", ["εσείς"], []],
["você (informal)", ["εσύ"], []],
["boa noite", ["καλησπέρα"], []],
["boa noite (ao se despedir)", ["καληνύχτα"], []],
["boa tarde", ["καλό απόγευμα"], []],
["bom dia", ["καλημέρα"], []],
["com licença", ["συγνώμη"], []],
["desculpe", ["συγνώμη"], []],
["não", ["όχι"], []],
["obrigado(a)", ["ευχαριστώ", "σ' ευχαριστώ"], []],
["oi, olá", ["γεια"], []],
["por favor", ["παρακαλώ"], []],
["sim", ["ναι"], []],
["tchau, adeus", ["αντίο", "γεια"], []],
["tudo bem, ok", ["εντάξει", "ΟΚ"], []],

                            
                          ]);
