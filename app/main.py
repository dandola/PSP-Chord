import node
import ring
import config
import distance
import hashkey
import finger_table
import random
import json
import pickle
import sys
rings=[]
nodes=[]
sys.setrecursionlimit(25000)
def create_ring(ring_id,cost=0):
	# if(rings != []):
	# 	return False
	new_ring= ring.Ring(ring_id)
	mean= new_ring.create(nodes)
	rings.append(new_ring)
	str ='tao ring thanh cong!!!'
	print str
	print 'chi phi tao ring la: ', mean
	return mean

def join(NodeID,NodeID_old):
	node_joined= None
	for nod in nodes:
		if NodeID_old == nod.NodeID:
			if nod.status == False:
				a='Node ',str(nod.NodeID),' khong hoat dong'
				print a
				return a
			else:
				node_joined = nod
				break
	if node_joined is None:
		print 'khong ton tai node joined: ', NodeID_old
		a= 'khong ton tai node joined: ' + str(NodeID_old)
		return a
	new_node = node.Node(NodeID)
	cost = new_node.join(node_joined)
	if cost == False:
		# return json.dumps("join khong thanh cong",indent=3)
		return 0
	nodes.append(new_node)
	# rings[0].nodes.append(new_node)
	# return infor_nodes(new_node.NodeID)
	return cost

def remove(NodeID):
	node=None
	for i in nodes:
		if NodeID == i.NodeID:
			if i.status==False:
				a='Node ',str(i.NodeID),' khong hoat dong'
				print a
				return a
			else:
				node = i
				break
	if node is None:
		print 'khong ton tai node co NodeID la: ', NodeID
		result= 'khong ton tai node co NodeID la: ' + str(NodeID)
		return result
	if node.remove():
		nodes.remove(node)
		# rings[0].nodes.remove(node)
		return 'remove thanh cong'


def lookup(NodeID,keyID=None,data=None):
	duongdi=[]
	node_joined=None
	for node in nodes:
		if NodeID==node.NodeID:
			if node.status==False:
				a='Node ',str(node.NodeID),' khong hoat dong'
				print a
				return a
			node_joined= node
			break
	if node_joined is None:
		kq= 'khong co Node nao co ID: ' +  str(NodeID)
		return kq
	if keyID is None:
		keyID=hashkey.hashkey(data)
	value= node_joined.lookup(keyID,duongdi)
	if value==False:
		return json.dumps('lookup khong thanh cong',indent=3)
	return value
	# if node_joined.lookup(keyID,duongdi)==False:
	# 	return json.dumps("lookup khong thanh cong", indent=3)
	# return json.dumps("lookup thanh cong", indent=3)



def SaveToPickle():
	filename= "ringObject.dat"
	with open(filename,'w') as writeData:
		pickle.dump(rings[0],writeData)
		writeData.close()
	return json.dumps("Done")

def SaveToPickle2():
	a = "4096/set_4096_nodes_ring.txt"
	datas=[]
	i=0
	with open(a,'r') as filedata:
		datas=json.load(filedata)
	for data in datas:
		load(data)
		filename= "4096/ringObject_4096_nodes_and_"+ str(i)+ "%_nodes_fault.dat"
		with open(filename,'w') as writeData:
			pickle.dump(rings[0],writeData)
			writeData.close()
		i+=10
		reset()
	return json.dumps("Done")

def LoadFromPickle(filename=None):
	global nodes
	if filename==None:
		filename= "ringObject_90%_nodes_fault.dat"
	with open(filename,'r') as writeData:
		ring = pickle.load(writeData)
		rings.append(ring)
		print"ringID: ",rings[0].Id_Ring
		nodes=rings[0].nodes
		writeData.close()
	return json.dumps("Done")



def insert(NodeID,data):
	duongdi=[]
	node_old=None
	for nod in nodes:
		if nod.NodeID==NodeID:
			if nod.status==False:
				a='Node ',str(nod.NodeID),' khong hoat dong'
				print a
				return a
			node_old=nod
			break
	if node_old is None:
		print 'khong ton tai node da tham gia co NodeID la: ', NodeID
		a= 'khong ton tai node da tham gia co NodeID la: ' + str(NodeID)
		return a
	if node_old.insert(data):
		return json.dumps("them du lieu thanh cong", indent=3)

def infor_nodes(node_id):
	if node_id==-1:
		list1=[] 
		i=0
		nod=nodes[0]
		while 1:
			a= {i:{'NodeID': nod.NodeID,'status: ':nod.status,'keyID': nod.keyID,'NodeID sucessor': nod.successor.NodeID,'NodeID predecessor': nod.predecessor.NodeID,'key-value': nod.managekey_value}}
			list1.append(a)
			i+=1
			nod= nod.successor
			if nod==nodes[0]:
				return json.dumps(list1,indent=4)
	for nod in nodes:
		if nod.NodeID==node_id:
			return nod.get_infor()
	print 'khong tim thay node co gia tri NodeID la: ', node_id
	return 'False'


def save():
	arr=[]
	arr_fail=[]
	for nod in nodes:
		if nod.managekey_value:
			for key_value in nod.managekey_value:
				if not(distance.distance(nod.m,nod.predecessor.keyID,key_value['key'],nod.keyID)):
					continue
				else :
					data= {'NodeID': nod.NodeID, 'data': key_value['value']}
					arr.append(data)
		if nod.status==False:
			arr_fail.append(nod.NodeID)

	data={
		'id_ring': rings[0].Id_Ring,
		'Nodes': [x.NodeID for x in nodes],
		'data': arr,
		'Node_false': arr_fail
		}
	a = 'data_' + str(config.NODES) + '.txt'
	with open(a,'w') as filedata:
		print data
		json.dump(data,filedata)
		return True

def load(filedata):
	if rings ==[]:
		data=filedata
		# data=json.dumps(data)
		id_ring=data['id_ring']
		Nodes= data['Nodes']
		key_value=data['data']
		Node_false=data['Node_false']
		# tao ring
		new_ring= ring.Ring(id_ring)
		mean= new_ring.create(Nodes)
		rings.append(new_ring)
		print 'chi phi khoi tao ring la: ', mean
		# khoi tao key_value
		if key_value!=[]:
			for i in key_value:
				print i['data']
				print insert(i['NodeID'],i['data'])
		for nod in Node_false:
			failure(nod)
		return True
	else: 
		print('da ton tai ring')
		return False


# moi mot node insert 5 data
def insert_data():
	for nod in nodes:
		if nod.status==True:
			for i in range(5):
				data=random.randint(1,2**20)
				insert(nod.NodeID,data)
	return 'hoan thanh insert'


	
def failure(NodeID):
	node=None
	for nod in nodes:
		if nod.NodeID==NodeID:
			node=nod
			break
	if node is None:
		a= "khong co node nao co NodeID = " + str(NodeID)
		return a
	if node.status== False:
		return "hoan thanh"
	else:
		node.status=False
		return "hoan thanh"

def reset():
	rings[:]=[]
	nodes[:]=[]
	return 'finished'


def count_fail_nodes():
	count=0
	for node in nodes:
		if node.status== False:
			count+=1
	str= "so luong node fail la: ", count
	return json.dumps(str, indent=3)

