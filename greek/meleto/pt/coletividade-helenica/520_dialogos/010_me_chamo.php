<?php

$page_title = "Me chamo ... (Ε. Ε. Μάθημα 1)";

$quiz_js = generateQuizJS("Imagine que seu nome é Πέτρος Δήμας.<br>Complete o espaço em branco.",
                          [
                            ["Me chamo/Eu sou Petros Dimas.<br>_____ Πέτρος Δήμας.", ["Λέγομαι", "Είμαι ο"], []],
                            ["Me chamam Petros Dimas.<br>_____ Πέτρο Δήμα.", ["Με λένε"]],
                            ["Ela: Πώς σας λένε;<br>Você: Με λένε Πέτρο. _____;<br>Ela: Με λένε Κάρμεν.", ["Εσάς"]],
                            ["Ele: Πώς σε λένε;<br>Você: Με λένε Πέτρο. _____;<br>Ele: Με λένε Γιάννη.", ["Εσένα"]],
                            ["Traduza: Como o chamam?<br>Πώς _____ λένε;", ["τον"]],
                            ["Traduza: Como a chamam?<br>Πώς _____ λένε;", ["την"]],
                            
                          ]);
