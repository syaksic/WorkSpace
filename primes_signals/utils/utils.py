#print('utils.py')

def doTik(Tok):
	from Wheel import doNoise
	Tok=doNoise(Tok)
	import time
	time.sleep(1)
	Tok['Tik']+=1
	return Tok

def load_tok(filename):
	import pickle
	import os
	if os.path.isfile(filename):
		with open(filename, 'rb') as f:
			return pickle.load(f)
	else:
		return {}

def save_Tok(Tok,filename):
	import pickle
	with open(filename, 'w') as f: 
		pickle.dump(Tok, f)

def printTok(Tok):
	import pprint
	pprint.pprint(Tok)

def check(Core):
	import os.path
	if os.path.isfile(Core)==False:
		from Universe import U
	else:
		U=load_tok(Core)
	tik=0
	for hist in U['Hist'].values():
		tik+=hist
	if not(U['Tik']==tik):
		print('ERROR en el Universo')
		print(U['Tik'],tik)
		raw_input('presione una tecla para observar el Universo')
		U['Tik']=tik
	Tok=doTik(U)
	return Tok

