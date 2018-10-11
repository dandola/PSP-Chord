from flask import Flask,request
import node
import distance
import main
import ring
import config
import json
import test
import finger_table
import finger_test
app=Flask(__name__)
@app.route('/create',methods=['POST'])
def create():
	if request.method=='POST':
		id_ring= int(request.form['id_ring'])
		if(main.create_ring(id_ring)!= False):
			return "tao ring thanh cong!"
		else:
    			return "tao ring loi"
		

@app.route('/join', methods=['POST'])
def join():
	if request.method=='POST':
		NodeID= int(request.form['NodeID'])	
		id_node_joinded=int(request.form['NodeID_joined'])
		print'----------------------------tien hanh join---------------------------'
		cost= main.join(NodeID,id_node_joinded)
		return json.dumps("join thanh cong",indent=3)
		

@app.route('/lookupkey',methods=['POST'])
def lookupkey():
	if request.method=='POST':
		id_node_joinded= int(request.form['NodeID'])	
		keyID= int(request.form['keyID'])
		data=None
		print'----------------------------tien hanh lookup---------------------------'
		cost= main.lookup(id_node_joinded,keyID,data)
		if cost==False:
			return "lookup khong thanh cong"
		else:
			return json.dumps({'chi phi: ':cost}, indent=3)

@app.route('/lookupdata',methods=['POST'])
def lookupdata():
	if request.method=='POST':
		id_node_joinded= int(request.form['NodeID'])	
		data= int(request.form['data'])
		keyID=None
		print'----------------------------tien hanh lookup---------------------------'
		cost= main.lookup(id_node_joinded,keyID,data)
		if cost==False:
			return "lookup khong thanh cong"
		else:
			return json.dumps({'chi phi: ':cost}, indent=3)
			

@app.route('/insert', methods=['POST'])
def insert():
	if request.method=='POST':
		id_node_joinded= int(request.form['NodeID'])
		data= int(request.form['data'])
		print'----------------------------tien hanh insert---------------------------'
		return main.insert(id_node_joinded,data)


@app.route('/remove',methods=['POST'])
def remove():
	if request.method == 'POST':
		NodeID=int(request.form['NodeID'])
		print'----------------------------tien hanh remove---------------------------'
		return main.remove(NodeID)


@app.route('/infor', methods=['POST'])
def infor():
	if request.method=='POST':
		node_id= int(request.form['NodeID'])
		if node_id==-1:
			print'----------------------------------------------'
			print 'in tat ca cac thong tin co trong ring'
			return main.infor_nodes(node_id)
		else:
			return main.infor_nodes(node_id)



@app.route('/save')
def save():
	if main.save():
		return 'save thanh cong!!!'
	return 'false'


@app.route('/load')
def load():
	result= main.load()
	if result:
		return 'load ring thanh cong'
	else:
		return 'da ton tai ring'


@app.route('/insert_data')
def insert_data():
	return main.insert_data()


@app.route('/reset')
def reset():
	return main.reset()

@app.route('/fault')
def fault():
	test.fault()
	return "hoanh thanh!!!"

@app.route('/test1')
def test1():
	return test.test1()

@app.route('/test_insert')
def test_insert():
	return test.test_insert()


@app.route('/failure', methods=['POST'])
def fauilure():
	if request.method=='POST':
		Node= int(request.form['NodeID'])
		return main.failure(Node)

@app.route('/count_fail_nodes')
def count_fail_nodes():
	return main.count_fail_nodes()


@app.route('/test_join')
def test_join():
    	return test.test_join()

app.route('/save_to_pickle')
def save_to_pickle():
	return main.SaveToPickle()

@app.route('/load_from_pickle')
def load_from_pickle():
	return main.LoadFromPickle()


@app.route('/save_to_pickle2')
def save_to_pickle2():
	return main.SaveToPickle2()


@app.route('/load_from_pickle2')
def load_from_pickle2():
	return main.LoadFromPickle2()


@app.route('/test_finger')
def test_finger():
	return finger_test.test_finger()


if __name__=='__main__':
	app.run(host='0.0.0.0',port=4000,debug=True)
