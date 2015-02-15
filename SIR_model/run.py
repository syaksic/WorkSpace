#!/usr/bin/python

from source.data import *
#import source import utils

def Calculate():
	print(SIR)
	graph=SIR['graph']
	#if not(graph['status']=='READY'):
	#	graph=utils.generate_graph(graph)
	inputs=SIR['inputs']
	if not(inputs['status']=='READY'):
		set_inputs(inputs,0.2,0.4,0.1,0.3,1.6,0.9)
	
		#Calcular Grafo
	print('Falta hacer esto')
	print(SIR)
	return 

Calculate()