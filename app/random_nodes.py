import numpy as np
import json
import random
import math
import config



def random_nodes():
	for j in range(10):
		nodes = random.sample(range(2**25), config.NODES)
		arr_nodes=[]
		nodes_fail= nodes
		for i in range(90,0,-10):
			print i
			k= int(math.ceil(config.NODES*i*1.0/100))
			print k
			nodes_fail= random.sample(nodes_fail,k)
			arr_nodes.append({'id_ring': 1, 'Nodes': nodes,'Node_false': nodes_fail, 'data': []})
		arr_nodes.append({'id_ring': 1, 'Nodes': nodes,'Node_false':[], 'data': []})
		arr_nodes.reverse()
		a="data_set/data_" + str(config.NODES) + "_" + str(j+1) + ".txt"
		with open(a,'w') as filedata:
			json.dump(arr_nodes,filedata)
	return True

def set_of_key():
	keys=[]
	part= int(math.ceil((2**160)*1.0/2000))
	keys = range(0,2**160,part)
	print len(keys)
	b="set_2000_keys_lookup.txt"
	with open(b,'w') as filedata:
		json.dump({'keys': keys},filedata)
	return True

def data_insert():
	times =range(5)
	arr_nodes=[]
	for i in times:
		nodes= random.sample(range(2**25),config.NODES)
		arr_nodes.append({'id_ring': 1, 'Nodes': nodes, 'Node_false':[], 'data':[]})
	a="data_insert/insert_data_1024nodes.txt"
	with open(a,'w') as filedata:
		json.dump(arr_nodes,filedata)
	return True



def create_ring(num_nodes):
	nodes=[]
	arr_nodes=[]
	key= 14615016373309029182036848327162830196559325
	partition=int(2**160/num_nodes)
	times=range(num_nodes)
	for i in times:
		nodes.append((key+partition*i)%(2**160))
	print(len(nodes))
	keys=nodes
	times=range(0,10,1)
	count_fail = int(math.floor(num_nodes*0.1))	
	arr_node_fail=nodes
	for i in range(9,0,-1):
		fails= count_fail*i
		print "count fail: ",fails
		arr_node_fail = random.sample(arr_node_fail,fails)
		arr_nodes.append({'id_ring': 1, 'Nodes': nodes,'Node_false': arr_node_fail, 'data': [],'count_fail': len(arr_node_fail)})
	arr_nodes.append({'id_ring': 1, 'Nodes': nodes,'Node_false':[], 'data': [],'count_fail': 0})
	arr_nodes.reverse()
	b="set_"+ str(num_nodes) + "_nodes_ring.txt"
	with open(b,'w') as filedata:
		json.dump(arr_nodes,filedata)
	return True


def read_file():
	a="the_mean_cost_lookup_with_2000_keys_partition_chord/topo_1024_nodes_1000_keys_lookup_with_partition=8.json"
	datas=[]
	with open(a,'r') as filedata:
		datas= json.load(filedata)
	for data in datas:
		print"max:",data['max'],", min:",data['min'],", mean:",data['mean'],", fails:", data['fails'],", requests:", data['requests'],", successes:",data['successes'],", overall_cost:",data['overall_cost'], ", max_overall_cost:", data['max_overall_cost']
	
create_ring(512)
create_ring(1024)
create_ring(2048)
create_ring(4096)



