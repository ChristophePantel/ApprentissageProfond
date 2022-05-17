import os

def format_str(nb):
	return "0" * (4 - len(str(nb))) + str(nb)

for i in range(1039, 1047):
	name_pre = 'stopmot_'+ format_str(i) + '.jpg' 
	name_post = 'a_stopmot_'+ format_str(i) + '.jpg' 
	os.rename(name_pre, name_post)