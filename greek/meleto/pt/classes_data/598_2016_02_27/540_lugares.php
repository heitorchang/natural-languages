<?php

$page_title = "Lugares";

$quiz_js = generateQuizJS("Traduza para grego.<br>Para substantivos, inclua o artigo definido (ο, η, το...).",
                          [
                            ["a escola de música", ["το ωδείο"]],
                            ["o posto de gasolina", ["το βενζινάδικο"]],
                            ["o banheiro", ["το μπάνιο"]],
                            ["o quarto", ["το δωμάτιο"]],
                            ["a Inglaterra", ["η Αγγλία"]],
                            ["a Amfilochia (cidade)", ["η Αμφιλοχία"]],
                          ]);
