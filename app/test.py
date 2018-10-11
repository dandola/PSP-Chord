import ring
import config
import distance
import hashkey
import finger_table
import random
import ring
import json
import math
import main
import numpy as np

def fault(x=0.4):
	k= int(math.ceil(config.NODES*x))
	node_fail= random.sample(main.nodes,k)
	for nod in node_fail:
		nod.status=False


def test_lookup(keys=[]):
	k= config.NODES
	list_partition=[]
	partition,fail,count_request=0,0,0
	list1, all_cost=[],[]
	for node in main.nodes:
		if node.status==True:
			for key in keys:
				count_request+=1
				# print "node: ",node.keyID, " tim key: ", key
				t,partition = node.lookup(key,duongdi=[])
				if isinstance(t, basestring) == True:
					fail+=1
					all_cost.append(int(t))
				else:
					if t!=0:
						list1.append(t)
						list_partition.append(partition)
						all_cost.append(t)
						
	max_value,min_value,mean=0,0,0
	# print list1
	if(len(list1)!=0):					
		mean=sum(list1)*1.0/len(list1)
		max_value=max(list1)
		min_value=min(list1)
	if(len(all_cost)!=0):					
		all_mean=sum(all_cost)*1.0/len(all_cost)
	else:
		all_mean = 0
	min_partition,max_partition,mean_partition=0,0,0
	if len(list_partition)!=0:
		mean_partition=sum(list_partition)*1.0/len(list_partition)
		min_partition=min(list_partition)
		max_partition=max(list_partition)

	mean_cost_with_one_partition=0
	if mean_partition!=0:
		mean_cost_with_one_partition= mean*1.0/mean_partition

	result = {
		'max': max_value,
		'arr_cost':list1,
		'min': min_value,
		'min_partition': min_partition,
		'max_partition': max_partition,
		'mean_partition': mean_partition,
		'mean': mean,
		'mean_cost_with_one_partition': mean_cost_with_one_partition,
		'fails': fail,
		'requests': count_request,
		'successes': len(list1),
		'overall_cost': all_mean,
		'max_overall_cost': max(all_cost)
	}
	return result

def format_data():
	for node in main.nodes:
		del node.managekey_value[:]

def insert(values=[]):
	count_request=0
	cost=[]
	for node in main.nodes:
		if node.status==True:
			for value in values:
				duongdi=[]
				print"insert data: ",value
				count_request+=1
				t = node.insert(value,duongdi)
				print"cost: ", t
				cost.append(t)
			format_data()
	if(len(cost)!=0):
		mean=sum(cost)*1.0/len(cost)
	else:
		mean=0
	result = {'max': max(cost), 'min': min(cost),'mean': mean,'requests': count_request}	
	return result

def test_insert():
	keys=[]
	b= "set_1000_keys.txt"
	with open(b,'r') as filedata:
		keys= json.load(filedata)
	a = "data_insert/insert_data_1024nodes.txt"
	datas=[]
	with open(a,'r') as filedata:
		datas= json.load(filedata)
	result=[]
	j=1
	for data in datas:
		main.load(data)
		result_test= insert(keys['keys'])
		a = str(j)+"nd:the_cost_insertion_1000_data_with_" + str(config.NODES) + "_nodes_and_partition=" + str(config.N) + ".json"		
		with open(a,"w") as fw:
			json.dump(result_test,fw)
		main.reset()
		j+=1
	return json.dumps("ket thuc",indent=3)


def reset_true():
	for nod in main.nodes:
		if nod.status==False:
			nod.status=True
	return True


def test1():
	keys=[]
	b= "set_2000_keys_lookup.txt"
	with open(b,'r') as filedata:
		keys= json.load(filedata)
	datas=[]
	filename = "set_1024_nodes_ring.txt"
	with open(filename,'r') as filedata:
		datas= json.load(filedata)
	i=0
	for data  in datas:
		main.load(data)
		result_test= test_lookup(keys['keys'])
		name = "topo_" + str(config.NODES) + "_nodes_" + str(2000) + "_keys_lookup_with_"+ str(i)+"%_faulty_nodes_improved_chord.json"
		with open(name,"w") as fw:
			json.dump(result_test,fw)
		main.reset()
		i+=10
	return json.dumps("ket thuc",indent=3)



def test_join():
	number_nodes=200
	list_cost=[]
	for node_joined in main.nodes:
		list_new_nodes =random.sample(range(1,2**25),number_nodes)
		for node_new in list_new_nodes:
			cost_join= main.join(node_new,node_joined.NodeID)
			if cost_join != 0:
				list_cost.append(cost_join)
				main.remove(node_new)  

	mean_cost= sum(list_cost)/len(list_cost)
	result= {'cost': mean_cost}
	a= "mean_path_length_in_joining_operation_with_" + str(config.NODES) + "_in_ring.json"
	with open(a,"w") as fw:
		json.dump(result,fw)
	kq= "chi phi trung binh la: " + str(mean_cost)
	return json.dumps(kq, indent=3)






		
