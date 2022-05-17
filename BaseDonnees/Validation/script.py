import os

def format_str(nb):
	return "0" * (4 - len(str(nb))) + str(nb)

for i in range(1, 26):
	name_pre = 'v_anima3d_10000 ('+ str(i) + ').jpg' 
	name_post = 'v_anima3d_'+ format_str(1000 + i) +'.jpg' 
	os.rename(name_pre, name_post)