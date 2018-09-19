<?php

$page_title = "Pessoas";

$quiz_js = generateQuizJS("Traduza para grego.<br>Para substantivos, inclua o artigo definido (ο, η, το...).",
                          [
                            ["o papai", ["ο μπαμπάς"], []],
                            ["a menina", ["το κορίτσι"], []],
                            ["a criança", ["το παιδί"]],
                            ["a mulher, esposa", ["η γυναίκα"]],
                          ]);
