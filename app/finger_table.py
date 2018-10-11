import config
class Finger(object):
	"""docstring for Finger"""
	def __init__(self,keyID, index,node=None,successor=None, predecessor=None):
		self.index=index
		start=keyID + 2**index
		if start > config.MAX_NODES:
			self.start = start - config.MAX_NODES
		else: self.start= start
		self.node= node
		self.successor=successor
		self.predecessor=predecessor
		
	def get_info():
		print('Start: ',self.start)
		print('Node manage: ', self.node.get_info())