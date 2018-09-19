<?php

$page_title = "Saudações e frases (Ε. Ε. Μάθημα 2)";

$quiz_js = generateQuizJS("Traduza para grego. Complete o espaço em branco.",
                          [
                            ["'O que fazem?' (Como estão?)<br>Τι _____;", ["κάνετε"], []],
                            ["'Como estão?'<br>Πώς _____;", ["είστε", "είσαστε"], []],
                            ["'O que faz?' (Como está?)<br>Τι _____;", ["κάνεις"], []],
                            ["'Como está?'<br>Πώς _____;", ["είσαι"], []],
                            ["muito bem", ["πολύ καλά"]],
                            ["'uma alegria'", ["μια χαρά"]],
                            ["bem", ["καλά"]],
                            ["mais ou menos", ["έτσι κι έτσι"]],
                            ["não muito bem", ["όχι πολύ καλά", "όχι και πολύ καλα"]],
                          ]);
