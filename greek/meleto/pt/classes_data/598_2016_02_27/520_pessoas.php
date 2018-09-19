<?php

$page_title = "Pessoas";

$quiz_js = generateQuizJS("Traduza para grego.<br>Para substantivos, inclua o artigo definido (ο, η, το...).",
                          [
                            ["o alemão (pessoa)", ["ο Γερμανός"], []],
                            ["a senhorita", ["η δεσποινίς", "η δεσποινίδα"]],
                            ["o(a) empregado(a)", ["ο ηπάλληλος", "η ηπάλληλος"]],
                            ["o carregador (de malas)", ["ο αχθοφόρος"]],
                            ["o André", ["ο Ανδρέας"]],
                            ["o Pandelis", ["ο Παντελής"]],
                          ]);
