Python script specs: Given a list of VOCABLISTS files, compile them into a dictionary of single characters and associated Gwoyeu Romatzyh pronunciations (may be more than one, for example, .le and leau)

INPUT: list_of_lists.txt

Run ls -w 1

/home/heitor/chinese/gwoyeu-romatzyh-studies/vocablists/chinese-made-easy/0004_change_of_tones.txt
/home/heitor/chinese/gwoyeu-romatzyh-studies/vocablists/chinese-made-easy/001_intro_useful_conversation.txt

...

VOCABLISTS format

你好;nii hao;How are you?
小姐;sheau jiee;Ms.


OUTPUT: JSON

{ "了": [".le", "leau"],
"你": ["nii"] }
