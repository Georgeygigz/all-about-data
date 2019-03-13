
from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello():
    data = request.get_json(force=True)
    name = ['name']
    return 'Hello {}'.format(name)

if __name__ == '__main__':
    app.run(port=10001,debug=True)
