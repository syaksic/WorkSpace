def ChainReaction(Prim):
	Mem=''
	Spr=''
	return {Mem:Spr}

def createYak(U,Name='',r1=None,r2=None,r3=None):
	#Genetica
	Prim=[]
	if r1==None:
		Prim.append(U['Nothing'][0])
	else:
		Prim.append(U['Silence'][r1])
	if r2==None:
		Prim.append(U['Nothing'][0])
	else:
		Prim.append(U['Silence'][r2])
	if r3==None:
		Prim.append(U['Nothing'][0])
	else:
		Prim.append(U['Silence'][r3])
	React=[]
	React.append(ChainReaction(Prim))
	NewYak={'Prim':Prim,'React':React}
	return NewYak

def createYaks(U,Count,Ini=None):
	Yaks=[]		
	for x in range(Count):
		Luk=x%len(U['Silence'])
		if Ini==None:
			Name='Yak'+str(Ini)+str(x)
			r1=random.choice([None]+[i for i in range(Luk)])
			r2=random.choice([None]+[i for i in range(Luk)])
			r3=random.choice([None]+[i for i in range(Luk)])
		else:
			Name='Yak'+str(Ini)+':'+str(x)
			r1=random.choice([i for i in range(Luk)])
			r2=random.choice([i for i in range(Luk)])
			r3=random.choice([i for i in range(Luk)])
		Name+=str((r1,r2,r3))
		Yaks.append(createYak(Name,r1,r2,r3))
	return Yaks



