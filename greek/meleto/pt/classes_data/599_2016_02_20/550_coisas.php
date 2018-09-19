<?php

$page_title = "Coisas";

$quiz_js = generateQuizJS("Traduza para grego.<br>Para substantivos, inclua o artigo definido (ο, η, το...).",
                          [
                            ["o dado (para jogar)", ["το ζάρι"], []],
                            ["o navio", ["το καράβι"]],
                            ["a bandeira", ["η σημαία"]],
                            ["as madeiras", ["τα ξύλα"]],
                            ["o barril", ["το βαρέλι"]],
                            ["a borracha", ["η γόμα"]],
                            ["a parede", ["ο τοίχος"], ["ο τοίχοσ"]],
                            ["a tesoura", ["το ψαλίδι"]],
                            ["o trem", ["το τραίνο"]],

                          ]);
                          
