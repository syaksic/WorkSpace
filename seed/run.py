tiktoktxt='''
def TikTok(Tik):
	def doTik(Tik):
		Noise=Tik['Signal']+Tik['Silence']+Tik['Nothing']+Tik['YaksSignals']
		sound=random.choice(Noise)
		if sound in Tik['Hist']:
			Tik['Hist'][sound]+=1
		else:
			Tik['Hist'][sound]=1
		Tik['Tik']+=1
		return Tik
	
	Tok=doTik(Tik)
	Tik=doTik(Tok)
	
	def doTok(Tik):
		if not(os.path.exists('./Tok')):
			with open('Tok', 'w') as f:
				pickle.dump(Tik, f)
		elif not(os.path.exists('Tik/')):
			print([os.makedirs('Tik/'+folder) for folder in Tik['PACK']['folders']])
			code=''
			for i in range(len(Tik['generate'])):
				code+='\n'+Tik['generate'][i]
			with open('Tik/SPREAD.py', 'w') as f: 
				f.write(code)					
		with open('Tok', 'rb') as f:
			Tok=pickle.load(f)
		return Tok
	
	Tok=doTok(Tik)
	Tik=doTok(Tok)
	return Tik
'''

Tik={'Hist': {'': 585,
          '_': 549,
          '__': 500,
          '___': 533,
          '____': 522,
          '_____': 524,
          '______': 583,
          '_______': 518,
          '________': 64,
          '_________': 54,
          'xxxxxxxxxxxxxxxxxxx': 552},
 'Nothing': [''],
 'PACK': {'files': {'': ['tiktok', 'run.py', 'Tok', 'SPREAD.py']},
          'folders': ['', 'Tik/']},
 'Signal': ['xxxxxxxxxxxxxxxxxxx'],
 'Silence': ['_',
             '__',
             '___',
             '____',
             '_____',
             '______',
             '_______',
             '________',
             '_________'],
 'Tik': 4982,
 'Yaks': [],
 'YaksSignals': [],
 'generate': {0: 'import os',
              1: 'import pickle',
              2: 'import random',
              3: 'import pprint',
              4: 'import shutil',
              5: 'import tiktok'}}



Tik['generate'][0]="import os"
raw_input('Operacion segura: '+Tik['generate'][0])
import os

Tik['generate'][1]="import pickle"
raw_input('Operacion segura: '+Tik['generate'][1])
import pickle

Tik['generate'][2]="import random"
raw_input('Operacion segura: '+Tik['generate'][2])
import random

Tik['generate'][3]="import pprint"
raw_input('Operacion segura: '+Tik['generate'][3])
import pprint

Tik['generate'][4]="import shutil"
raw_input('Operacion segura: '+Tik['generate'][4])
import shutil


def TikTok(Tik):
	def doTik(Tik):
		Noise=Tik['Signal']+Tik['Silence']+Tik['Nothing']+Tik['YaksSignals']
		sound=random.choice(Noise)
		if sound in Tik['Hist']:
			Tik['Hist'][sound]+=1
		else:
			Tik['Hist'][sound]=1
		Tik['Tik']+=1
		return Tik
	
	Tok=doTik(Tik)
	Tik=doTik(Tok)
	
	def doTok(Tik):
		
		if not(os.path.exists('./Tok')):
			with open('Tok', 'w') as f:
				pickle.dump(Tik, f)
		elif not(os.path.exists('Tik/')):
			print([os.makedirs('Tik/'+folder) for folder in Tik['PACK']['folders']])
			code=''
			for i in range(len(Tik['generate'])-1):
				code+='\n'+Tik['generate'][i]
			with open('Tik/__init__.py', 'w') as f: 
				f.write(code)		
			with open('Tik/tiktok.py', 'w') as f: 
				f.write(tiktoktxt)			
		with open('Tok', 'rb') as f:
			Tok=pickle.load(f)
		return Tok
	
	Tok=doTok(Tik)
	Tik=doTok(Tok)
	os.system("gnome-terminal -e 'bash -c \"python ./Tik/tiktok.py; exec bash\"'")
	return Tik
	
Tik['generate'][5]="import tiktok"
raw_input('Operacion segura: '+Tik['generate'][5])
while True:
	Tok=TikTok(Tik)

Absolute=0
while not(Tik['Tik']==Absolute):

	Tik['generate'][6]="Tok=TikTok(Tik)"
	raw_input('Operacion insegura: '+Tik['generate'][6])
	
	pprint.pprint(Tok)
	Absolute=Tok['Tik']
	print Absolute