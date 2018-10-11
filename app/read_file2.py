import json
import numpy as np


with open('topo_1024_nodes_4096_keys_lookup_with_partition=12.json') as file_json:
	a= json.load(file_json)

for data in a:
	print "max:",data['max'],", min:",data['min'],", mean:",data['mean'],", fails:", data['fails'],", requests:", data['requests'],", successes:",data['successes'],", overall_cost:",data['overall_cost'], ", max_overall_cost:", data['max_overall_cost']
