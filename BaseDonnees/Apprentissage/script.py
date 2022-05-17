import os

def format_str(nb):
	return "0" * (4 - len(str(nb))) + str(nb)

for i in range(1, 26):
	name_pre = 't_anima2d_1000 ('+ str(nb) + ').jpg' 
	name_post = 't_anima2d_'+ format_str(1000 + i) + '.jpg' 
	os.rename(name_pre, name_post)