<?php

$page_title = "Outras palavras";

$quiz_js = generateQuizJS("Traduza para grego.<br>Para substantivos, inclua o artigo definido (ο, η, το...).",
                          [
                            ["a saúde", ["η υγεία"], []],
                            ["inglês (a língua)", ["τα αγγλικά"], []],
                            ["o basquete", ["το μπάσκετ-μπωλ", "το μπάσκετμπολ"], []],
                            ["o amanhã", ["το αύριο"]],
                            ["o milagre", ["το θαύμα"]],
                            ["(eu) trabalho", ["δουλέυω"]],
                            ["o Euro (moeda)", ["το Ευρώ"]],
                            ["a palavra", ["η λέξη"]],
                            ["a terra", ["η γη"]],
                            ["a hora", ["η ώρα"]],
                            ["a imagem", ["η εικόνα"]],
                          ]);
