from flask import Flask
import json
from flask_cors import CORS
from flask import request, Response


app = Flask(__name__)
CORS(app)

@app.route('/api/v1/readFile', methods=['GET'])
def read_file():
    context = {}
    try:
        args = request.args.to_dict()
        if not "file_name" in args.keys():
            file_name = 'file1.txt'
        else:
            file_name = args.get('file_name')
    
        #Reading data
        with open(file_name, 'r') as fp:
            data = fp.readlines()
        if "start" and "end" in args.keys():
            start = int(args.get('start'))
            end = int(args.get('end'))
            data = data[start:end]
        context['message'] = data
    except Exception as error:
        context['message'] = error
    return Response(json.dumps(context), status=201, mimetype="application/json")
    

if __name__ == '__main__':
    app.run(port=8088, debug= True)
