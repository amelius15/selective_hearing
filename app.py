from flask import Flask, request, send_from_directory, jsonify
import json
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route('/state', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        content = request.json
        allow_things = content['allow']
        with open('connection.txt', 'w') as fs:
            for i in allow_things:
                fs.write(i + '\n')
        return jsonify({"allow":allow_things}) 
    else:
        allow_things = []
        with open('connection.txt', 'r') as fs:
            allow_things = [i.strip() for i in fs.readlines()]
        return jsonify({"allow":allow_things}) 

if __name__ == "__main__":
    app.run()