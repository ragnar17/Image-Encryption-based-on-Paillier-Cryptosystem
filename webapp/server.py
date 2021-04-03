from flask import Flask
import pickle
import requests
from flask import request

import ImageOperations

app = Flask(__name__)

@app.route('/')
def hello_world():
    return """Hello nerds!!"""

@app.route('/brightness_control', methods=['POST'])
def brightness_control():
	"""
	args = {
		enc_img = , 
		v = ,
		pb = 
	}
	"""
	args = pickle.loads(request.get_data())

	enc_img = args['enc_img']
	v = args['v']
	pb = args['pb']

	res = ImageOperations.Secure_Image_Adjustment_Brightness_Control(enc_img, v, pb)

	return pickle.dumps(res,protocol=2)




@app.route('/image_negation', methods=['POST'])
def image_negation():
	"""
	args = {
		enc_img = , 
		v = ,
		pb = 
	}
	"""
	args = pickle.loads(request.get_data())

	enc_img = args['enc_img']
	v = args['v']
	pb = args['pb']

	res = ImageOperations.Secure_Image_Adjustment_Image_negation(enc_img, v, pb)

	return pickle.dumps(res,protocol=2)

@app.route('/noise_reduction', methods=['POST'])
def noise_reduction():
	"""
	args = {
		enc_img = , 
		px = ,
		py = ,
		pb = 
	}
	"""
	args = pickle.loads(request.get_data())

	enc_img = args['enc_img']
	px = args['px']
	py = args['py']
	pb = args['pb']

	res = ImageOperations.Secure_Noise_Reduction_LPF(enc_img, px, py, pb)

	return pickle.dumps(res,protocol=2)


@app.route('/sobel_operator', methods=['POST'])
def sobel_operator():
	"""
	args = {
		enc_img = , 
		ker = ,
		pb = 
	}
	"""
	args = pickle.loads(request.get_data())

	enc_img = args['enc_img']
	ker = args['ker']
	pb = args['pb']

	res = ImageOperations.sobelOperator(enc_img, ker, pb)

	return pickle.dumps(res,protocol=2)



app.run()