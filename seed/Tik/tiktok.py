
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
				code+='
'+Tik['generate'][i]
			with open('Tik/SPREAD.py', 'w') as f: 
				f.write(code)					
		with open('Tok', 'rb') as f:
			Tok=pickle.load(f)
		return Tok
	
	Tok=doTok(Tik)
	Tik=doTok(Tok)
	return Tik
