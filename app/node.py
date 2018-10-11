import ring
import config
import distance
import hashkey
import finger_table
import random
import ring
import json
manage_key=[]
class Node(object):
	"""Node"""
	def __init__(self,NodeID):
		self.NodeID=NodeID
		self.keyID = NodeID
		self.m=config.M
		self.successor= None
		self.predecessor= None
		self.managekey_value=[]
		self.finger=[]
		self.status=True


	"""tim kiem closets"""
	def closest_preceding_node(self,keyID):
		for i in range(self.m-1,-1,-1):
			if distance.distance(self.m, self.keyID, self.finger[i].successor.keyID,keyID) and self.finger[i].successor.status==True:
				return self.finger[i].successor
			elif distance.distance(self.m,self.keyID,self.finger[i].node.keyID, keyID) and self.finger[i].node.status==True:
				return self.finger[i].node
			elif distance.distance(self.m,self.keyID,self.finger[i].predecessor.keyID, keyID) and self.finger[i].predecessor.status==True:
				return self.finger[i].predecessor
			else:
				continue
		return self



	"""tim predecessor cua id"""
	def find_predecessor(self, keyID,duongdi=[]):
		begin,node = self,self
		# print "keyID: ", keyID
		while not(distance.distance(node.m,node.keyID,keyID,node.successor.keyID) or keyID == node.successor.keyID):
			start=node
			node =node.closest_preceding_node(keyID)
			if start.keyID == node.keyID:
				return start
			duongdi.append(node.NodeID)
		return node

	def find_successor(self,keyID,duongdi=[]):
		n=self.find_predecessor(keyID,duongdi)
		if n.successor.status == True and (distance.distance(config.M, n.keyID, keyID, n.successor.keyID) or n.successor.keyID==keyID):
			duongdi.append(n.successor.NodeID)
			return n.successor
		elif n.finger[0].successor.status==True and n.finger[0].successor.keyID >= keyID:
			duongdi.append(n.finger[0].successor.NodeID)
			return n.finger[0].successor
		else:
			return False

	"""khoi tao bang finger table cua node"""
	def init_finger_table(self,n):
		path,max,t=[],0,0
		for i in range(self.m):
			node_finger=finger_table.Finger(self.keyID, i)
			self.finger.append(node_finger)
		a=n.find_successor(self.finger[0].start,path)
		t+=1
		max=len(path)
		del path
		if a!=False:
			self.finger[0].node= a
		else:
			return False
		self.successor= self.finger[0].node  
		self.predecessor= self.successor.predecessor
		self.predecessor.successor=self
		self.successor.predecessor= self
		self.finger[0].successor=self.finger[0].node.successor
		self.finger[0].predecessor=self.finger[0].node.predecessor
		for i in range(self.m-1):
			# print 'khoi tao finger thu ',i 
			path=[]
			if(distance.distance(self.m,self.keyID,self.finger[i+1].start,self.finger[i].node.keyID) or self.finger[i+1].start==self.finger[i].node.keyID):
				# print "th1"
				# print "node"
				self.finger[i+1].node = self.finger[i].node
				self.finger[i+1].successor=self.finger[i].node.successor
				self.finger[i+1].predecessor=self.finger[i].node.predecessor
			else:
				a = n.find_successor(self.finger[i+1].start,path)
				if a == False:
    					return False	
				else:
					# print 'duong di: ', path
					# print 'chi phi tai finger thu ', i+1, 'la: ', len(path)
					if(len(path) >= max):
						max=len(path)
					del path
					t+=1
					self.finger[i+1].node= a
					self.finger[i+1].successor=self.finger[i+1].node.successor
					self.finger[i+1].predecessor=self.finger[i+1].node.predecessor
		cost= max*t
		# print 'chi phi join la: ', cost
		return cost


	""" cap nhat node n vao cac finger table khac"""
	def update_others(self):
		max,t,p=0,0,self
		for i in range(self.m):
			# print "tai chi so i= ", i
			path=[] 
			if(not distance.distance(config.M, p.keyID,((self.keyID-2**i)%(2**config.M)),p.successor.keyID) or not(((self.keyID-2**i)%(2**config.M))==p.keyID)):		
				p = self.find_predecessor((self.keyID-2**i)%(config.MAX_NODES),path)
				if(p.successor.keyID==(self.keyID-2**i)%(config.MAX_NODES)):
					p=p.successor
				t+=1
				# print 'duong di: ',path
				# print 'chi phi: ', len(path)
				if p.keyID == self.keyID:
					p.update_finger_table(self,i)
					continue
				if(len(path) >= max):
					max = len(path)
				del path
			p.update_finger_table(self,i)
		cost= max*t
		# print 'chi phi update la: ', cost
		return cost

	

	"""update bang table"""
	def update_finger_table(self,n,i):
		if(distance.distance(self.m, self.keyID, n.keyID, self.finger[i].node.keyID) or n.keyID==self.finger[i].start):
			if(not distance.distance(self.m,self.keyID,n.keyID,self.finger[i].start)):
				# print 'update finger node: ', self.NodeID,' tai vi tri thu: ',i,' voi node finger la:',n.keyID
				self.finger[i].node=n
				self.finger[i].successor=n.successor
				self.finger[i].predecessor=n.predecessor
			p=self.predecessor
			if p.keyID == n.keyID:
				return True
			p.update_finger_table(n,i)
		elif self.keyID==n.keyID:
			p=self.predecessor
			if p.keyID == self.keyID:
				return True
			p.update_finger_table(n,i)


	def update_update(self,duongdi=[]):
		for i in range(self.m):
			if(self.finger[i].node.keyID==self.keyID):
				self.finger[i].successor=self.successor
				self.finger[i].predecessor=self.predecessor
		for i in range(self.m):
			duongdi=[] 
			p=self.find_predecessor((self.keyID - 2**i)%(config.MAX_NODES),duongdi)
			if(p.successor.keyID==(self.keyID-2**i)%(config.MAX_NODES)):
					p=p.successor
			if p.keyID==self.keyID:
				continue
			p.update_table(self,i,duongdi)
			del duongdi

	def update_table(self,n,i,duongdi=[]):
		if self.finger[i].node.keyID == n.keyID:
			self.finger[i].node = n
			self.finger[i].successor=n.successor
			self.finger[i].predecessor=n.predecessor
			p = self.predecessor
			if p.keyID == n.keyID or p.status==False:
				return True
			duongdi.append(p.NodeID)
			p.update_table(n,i,duongdi)


	"""gan key-value cho new node"""
	def set_key_value(self):  
		node_successor=self.successor
		if node_successor.managekey_value:
			for i in range(len(node_successor.managekey_value)):
				if distance.distance(self.m, node_successor.managekey_value[i]['key'],self.keyID,node_successor.keyID) or node_successor.managekey_value[i]['key']==self.keyID:
					obj= node_successor.managekey_value[i]
					self.managekey_value.append(obj)
					node_successor.managekey_value.remove(obj)
					return True
		else:
			return True


	def join(self,n=None):
		cost=0
		if(n!=None):
			# print("+++++++++++++++++thuc hien init table+++++++++++++++")
			cost=self.init_finger_table(n)
			if cost == False:
				print "loi qua trinh khoi tao bang finger table"
				return False
			# print ' chi phi init finger table la: ', cost, '\n\n\n'
			# print'--------------- thuc hien set_key_value-------------'
			self.set_key_value() 
			# print'---------------NEXT-------------'
			# print("++++++++++++++++++++thuc hien update orthers Node+++++++++++++++++++++")
			cost= self.update_others()
			# print 'chi phi update_other la: ', cost , '\n\n\n'
			# print("++++++++++++++++++++++update predecessor++++++++++++++++++++")
			# print("Node predecessor co ID:", self.predecessor.NodeID)
			self.predecessor.update_update()
			# print("+++++++++++++++++++++++update successor++++++++++++++++++++++++++")
			# print("Node successor co ID:", self.successor.NodeID)
			self.successor.update_update()
			# print('\n\n\n')
			# print 'chi phi join la: ', cost
			# self.get_infor()
			# print('\n\n\n')
			return cost
		else:
			print('node_goc_id: ',self.NodeID)
			for i in range(self.m):
				node_finger= finger_table.Finger(self.keyID,i)
				node_finger.node= self
				node_finger.successor= self
				node_finger.predecessor= self
				self.finger.append(node_finger)
			self.predecessor=self
			self.successor=self
			return 1
	
	def min_key(self,keyID):
		key={'key':0, 'min': 2**160}	
		for i in range(config.N):
			jump= (keyID + i*config.partition)%(config.MAX_NODES)
			delta=jump-self.keyID
			if delta <0:
				delta=delta + 2**self.m
			if delta < key['min']:
				key['key'] = jump
				key['min']= delta
		return key['key']
	
	def insert(self,value,duongdi=[]):
		duongdi.append(self.NodeID)
		keyID= hashkey.hashkey(value)
		# print"gia tri keyID ban dau la: ", keyID
		key_value={'key':keyID,'value': value}
		key=self.min_key(keyID)
		i=0
		return self.insert_orther(key,key_value,i,duongdi)


	def insert_orther(self,keyID, key_value,i,duongdi=[]):
		if i==config.N:
			result = len(duongdi)
			return result
		if(distance.distance(self.m,self.predecessor.keyID,keyID, self.keyID) or keyID==self.keyID):
			if self.managekey_value:
				for key_values in self.managekey_value:
					if key_values['key']==key_value['key']:
						key_values['value']= key_value['value']
						i+=1
						keyID=(keyID + config.partition)%(config.MAX_NODES)
						return self.insert_orther(keyID,key_value,i,duongdi)

			self.managekey_value.append(key_value)
			# kq= {'duongdi': duongdi,'NodeID': self.NodeID,'key-value': key_value}
			i+=1
			keyID=(keyID + config.partition)%(config.MAX_NODES)
			return self.insert_orther(keyID,key_value,i,duongdi)
		else:
			node = self.find_predecessor(keyID,duongdi)
			# print "predecessor: ", node.NodeID
			if node.successor.status==True and (distance.distance(config.M, node.keyID, keyID, node.successor.keyID) or node.successor.keyID==keyID):
				# print "2"
				node=node.successor
				duongdi.append(node.NodeID)
			elif node.finger[0].successor.status==True and (distance.distance(config.M, node.finger[0].node.keyID, keyID, node.finger[0].successor.keyID) or node.finger[0].successor.keyID==keyID):
				# print "3"
				node=node.finger[0].successor
				duongdi.append(node.NodeID)
			else:
				# print "4"
				i+=1
				keyID=(keyID + config.partition)%(config.MAX_NODES)
			return node.insert_orther(keyID,key_value,i,duongdi)


	def fix_finger(self,n,i):
    		if self.finger[i].node.keyID == n.keyID:
				self.finger[i].node=n.successor
				self.finger[i].successor=self.finger[i].node.successor
				self.finger[i].predecessor=self.finger[i].node.predecessor
				p=self.predecessor
				# if p.keyID==n.keyID or p.status==False:
				if p.keyID == n.keyID:
					return True
				p.fix_finger(n,i)



	def remove(self):
		node_successor= self.successor
		node_predecessor= self.predecessor
		for key_value in self.managekey_value:
			node_successor.managekey_value.append(key_value)
		node_successor.predecessor=node_predecessor
		node_predecessor.successor= node_successor
		for i in range(self.m): 
			p=self.find_predecessor((self.keyID - 2**i)%(config.MAX_NODES))
			if p.keyID==self.keyID:
				continue
			p.fix_finger(self,i)
		node_predecessor.update_update()
		node_successor.update_update()
		return True

	def set_keys(self,keyID):
		keys=[]
		i=0
		while i < config.N:
			keys.append((keyID + i*config.partition)%(config.MAX_NODES))
			i+=1
		return keys
	def closest_key(self,keys):
		k= range(len(keys))
		for i in k:
			if(distance.distance(self.m,keys[i-1],self.keyID,keys[i])):
				return keys[i]


#fingertable for experiment
	def lookup(self, keyID,duongdi=[]):
		duongdi.append(self.NodeID)
		if(distance.distance(self.m,self.predecessor.keyID,keyID,self.keyID) or self.keyID==keyID):
			kq={'duongdi':duongdi,'key':keyID,'data': None,'thuoc_Node': self.NodeID}
			# print json.dumps(kq,indent=3)
			count=len(duongdi)-1
			return count
		else:
			node=None 
			node = self.find_predecessor(keyID,duongdi)

			if node.successor.status==True  and (distance.distance(config.M, node.keyID, keyID, node.successor.keyID) or node.successor.keyID==keyID):
				# print "th1"
				node = node.successor
			elif node.finger[0].successor.status==True  and (distance.distance(config.M, node.finger[0].node.keyID, keyID, node.finger[0].successor.keyID) or node.finger[0].successor.keyID==keyID):
				# print "th2"
				node=node.finger[0].successor
				# print "Node: ",node.NodeID
			else:
				count=str(len(duongdi)-1)
				# print "failure"
				return count
			return node.lookup(keyID,duongdi)

	# def lookup(self, keyID,duongdi=[]):
	# 	partition = 0
	# 	duongdi.append(self.NodeID)
	# 	# key=self.min_key(keyID)
	# 	keys = self.set_keys(keyID)
	# 	for key in keys:
	# 		if(distance.distance(self.m,self.predecessor.keyID,key,self.keyID) or self.keyID==key):
	# 			cost=len(duongdi) - 1
	# 			kq={'duongdi':duongdi,'key':keyID,'data': None,'thuoc Node': self.NodeID,'cost': cost}
	# 			# print json.dumps(kq,indent=3)
	# 			return cost,partition
	# 	while keys!=[]:
	# 		key = self.closest_key(keys)
	# 		partition+=1
	# 		node = self.find_predecessor(key,duongdi)
	# 		if node.successor.status==True  and (distance.distance(config.M, node.keyID, key, node.successor.keyID) or node.successor.keyID==key):
	# 			node = node.successor
	# 			duongdi.append(node.NodeID)
	# 			cost=len(duongdi) - 1
	# 			kq={'duongdi':duongdi,'key':keyID,'virtual_key': key,'data': None,'thuoc Node': node.NodeID,'cost': cost}
	# 			# print json.dumps(kq,indent=3)
	# 			return cost,partition
	# 		elif node.finger[0].successor.status==True  and (distance.distance(config.M, node.finger[0].node.keyID, key, node.finger[0].successor.keyID) or node.finger[0].successor.keyID==key):
	# 			node=node.finger[0].successor
	# 			duongdi.append(node.NodeID)
	# 			cost=len(duongdi) - 1
	# 			kq={'duongdi':duongdi,'key':keyID,'virtual_key': key,'data': None,'thuoc Node': node.NodeID,'cost': cost}
	# 			# print json.dumps(kq,indent=3)
	# 			return cost,partition
	# 		else:
	# 			keys.remove(key)
	# 	cost_fail = str(len(duongdi)-1)
	# 	return cost_fail,partition


	def get_infor(self):
		print '-----------------------------------------------------------------'
		print 'NodeID: ', self.NodeID,' keyID : ',self.keyID, 'status: ', self.status
		print 'NodeID_successor: ',self.successor.NodeID
		print 'NodeD_predecessor: ',self.predecessor.NodeID
		print 'thong tin quan ly key-value: '
		if self.managekey_value:
			print self.managekey_value
		else:
			print 'manageKey-value rong'
		print '---------------------------finger table-------------------------'
		print 'index----------------------start-------------------successor-NodeID----------successor-------predecessor'
		for fin in self.finger:
			print fin.index,'--------', fin.start,'------------',fin.node.keyID,'-----------',fin.successor.keyID,'-------',fin.predecessor.keyID
		print '---------------------------end------------------------------------'
		a={
		'NodeID': self.NodeID,
		'keyID': self.keyID,
		'status': self.status,
		'NodeID successor': self.successor.keyID,
		'NodeID predecessor': self.predecessor.keyID,
		'manage key-value': self.managekey_value,
		}
		return json.dumps(a,indent=4)


		
	


	