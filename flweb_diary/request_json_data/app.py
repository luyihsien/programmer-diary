from flask import Flask, jsonify, request
#http://docs.jinkan.org/docs/flask/quickstart.html
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/h', methods=['POST', 'GET'], defaults={'name' : 'Default'})#改成hom 然後url輸入hom也行
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>Hello {}, you are on the home page!</h1>'.format(name)

@app.route('/json')
def json():
    return jsonify({'key' : 'value', 'listkey' : [1,2,3]})

@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}. You are on the query page!</h1>'.format(name, location)

@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">
                  <input type="text" name="name">
                  <input type="text" name="location">
                  <input type="submit" value="Submit">
              </form>'''

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']

    return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(name, location)

@app.route('/processjson', methods=['POST'])
def processjson():

    data = request.get_json()

    name = data['name']
    location = data['location']

    randomlist = data['randomlist']

    return jsonify({'result' : 'Success!', 'name' : name, 'location' : location, 'randomkeyinlist' : randomlist[1]})

if __name__ == '__main__':
    app.run(debug=True)