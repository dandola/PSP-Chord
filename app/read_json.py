import json


list_mean=[]
list_max=[]
list_min=[]
list_success=[]
list_request=[]


with open('test-faultolerance-chord/topo_128_nodes_1000_keys_lookup_70%_fault.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])
list_success.append(len(a['costs']))
list_request.append(a['so luong request'])


with open('test-faultolerance-chord/topo_256_nodes_1000_keys_lookup_70%_fault.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])
list_success.append(len(a['costs']))
list_request.append(a['so luong request'])

with open('test-faultolerance-chord/topo_512_nodes_1000_keys_lookup_70%_fault.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])
list_success.append(len(a['costs']))
list_request.append(a['so luong request'])

with open('test-faultolerance-chord/topo_1024_nodes_1000_keys_lookup_70%_fault.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])
list_success.append(len(a['costs']))
list_request.append(a['so luong request'])

with open('test-faultolerance-chord/topo_2048_nodes_1000_keys_lookup_70%_fault.json') as file_json:
	a= json.load(file_json)
list_mean.append(a['mean'])
list_max.append(a['max'])
list_min.append(a['min'])
list_success.append(len(a['costs']))
list_request.append(a['so luong request'])

list_mean1=[]
list_max1=[]
list_min1=[]
list_success1=[]
list_request1=[]

with open('test-faultolerance/topo_128_nodes_1000_keys_lookup_70%_fault_1.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])
list_success1.append(len(a['costs']))
list_request1.append(a['so luong request'])

with open('test-faultolerance/topo_256_nodes_1000_keys_lookup_70%_fault_1.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])
list_success1.append(len(a['costs']))
list_request1.append(a['so luong request'])

with open('test-faultolerance/topo_512_nodes_1000_keys_lookup_70%_fault_1.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])
list_success1.append(len(a['costs']))
list_request1.append(a['so luong request'])

with open('test-faultolerance/topo_1024_nodes_1000_keys_lookup_70%_fault_1.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])
list_success1.append(len(a['costs']))
list_request1.append(a['so luong request'])

with open('test-faultolerance/topo_2048_nodes_1000_keys_lookup_70%_fault_1.json') as file_json:
	a= json.load(file_json)
list_mean1.append(a['mean'])
list_max1.append(a['max'])
list_min1.append(a['min'])
list_success1.append(len(a['costs']))
list_request1.append(a['so luong request'])

print(list_mean1)
print(list_max1)
print(list_min1)
print(list_success1)
print(list_request1)


print(list_mean)
print(list_max)
print(list_min)
print(list_success)
print(list_request)