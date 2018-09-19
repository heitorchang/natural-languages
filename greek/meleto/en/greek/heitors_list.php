<?php

$page_title = "Heitor's personal list";

$quiz_js = generateQuizJS("Heitor\\'s personal list",
                          [
                            ["One, has partials", ["ένα", "μία"], ["ενα", "μια"]],
                            ["no partials, but with empty array", ["δύο"], []],
                            ["excluded partials", ["τρία"]],
                            ["last one, regular", ["τέσσερα"], ["τεσσερα"]],
                          ]);
