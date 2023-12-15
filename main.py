import json, os
from flask import Flask
from flask import render_template, make_response,request, abort, send_file

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return '<h1 style="text-align:center">Welcome to C2HTTPServer</h1>'

#serve files from within th dropper folder
#-> please put files you want to receive into the "dropper" folder
@app.route('/dropper/<path:filename>', methods=['GET'])
def serveFiles(filename):
	print(f'{filename} was requested...')
	if(filename in os.listdir(os.path.join(os.getcwd(), 'dropper'))):
		filePath = os.path.join(os.getcwd(), f'dropper/{filename}')
		return send_file(filePath) #-> this is unsafe and should be exchanged
	print(f'{filename} is not present -> maybe you mispelled the filename ?')
	return abort(404)
	#return send_from_directory('dropper', filename, as_attachment=True)

#accepting and presenting incoming request data   
@app.route('/honeypot', methods=['GET', 'POST'])
def honeypot():
	#fData = json.dumps(request.get_json(force=True), indent=2)
	print(f'incoming Data...\n {request}')
	return abort(403)

'''
-> there needs to be an authentication system implemented.
	this should preferely base on JWT
'''

if __name__ == '__main__':
	print(

"""
    _/                  _/        _/  
   _/          _/_/    _/  _/         
  _/        _/    _/  _/_/      _/    
 _/        _/    _/  _/  _/    _/     
_/_/_/_/    _/_/    _/    _/  _/      
"""

)
	app.run()