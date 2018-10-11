import config
import random
import node
import main
class Ring(object):
	"""docstring for ClassName"""
	def __init__(self,Id_ring):
		self.Id_Ring= Id_ring
		self.nodes=[]
		self.Max_Nodes= config.MAX_NODES


	def create(self,nodes=[]):
		mean,cost,list_cost,list1=0,0,[],[]
		if nodes == []:
			key=14615016373309029182036848327162830196559325
			part= int(2**160/config.NODES)
			list1= range(key, 2**160, part)
			# list1.append(key)
		else:
			list1 = nodes
		for i in range(len(list1)):
			n= node.Node(list1[i])
			print("node thu ",i," node-id: ", n.NodeID,'keyID: ',n.keyID)
			if(len(self.nodes)==0):
				cost = n.join()
			else: 
				cost = n.join(self.nodes[i-1])
			list_cost.append(cost)
			self.nodes.append(n)
			main.nodes.append(n)
		return sum(list_cost)/len(list_cost)
		

	def info(self):
		print('information: ')
		
		
	
	
		