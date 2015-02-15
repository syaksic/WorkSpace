def set_inputs(inputs,v_alpha,v_beta,v_eta,v_lambda,v_delta,v_xi):
	probs=inputs['probabilities']
	probs['alpha']=v_alpha
	probs['beta']=v_beta
	probs['eta']=v_eta
	rates=inputs['rates']
	rates['lambda']=v_lambda
	rates['delta']=v_delta
	rates['xi']=v_xi
	inputs['status']='READY'

def set_graph(graph):
	from graph_utils import *
	if graph['status']=='INIT':
		graph['savefile']=generate_graph('demo0',10)
	graph['status']='READY'

SIR={
	'graph':{
		'status':'INIT',
		'size':0,
		'name':'None',
		'savefile':'',		
		
		'degree':{
			'k_mean':0,
			'Teo':{
				'degree_dist':{
					'k':[],
					'value':[],
					},
				'uncorr_func':{
					'k':[],
					'value':[],
					}
			},
			'BF':{
				'degree_dist':{
					'k':[],
					'value':[],
					},
				'uncorr_func':{
					'k':[],
					'value':[],
					}
			},
			'Exp':{
				'degree_dist':{
					'k':[],
					'value':[],
					},
				'corr_func':{
					'k':[],
					'x':[],
					'value':[],
					},
				'uncorr_func':{
					'k':[],
					'value':[],
					}
			},
		},
	},
	'inputs':{
		'status':'INIT',	
		'probabilities':{
			'alpha':0,
			'beta':0,
			'eta':0},
		'rates':{
			'lambda':0,
			'delta':0,
			'xi':0},
	},
	'results':{
		't_t':[],
		'i_t':[],
		's_t':[],
		'r_t':[]},

}

SIR_demo={
	'probabilities':{
		'alpha':0,
		'beta':0,
		'eta':0},
	'rates':{
		'lambda':0,
		'delta':0,
		'xi':0},
	'graph':{
		'k_mean':0,
		'degree_dist':{
			'index':[],
			'value':[],
			},
	},
	'results':{
		't_t':[],
		'i_t':[],
		's_t':[],
		'r_t':[]},

}
