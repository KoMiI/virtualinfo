from flask import Flask, session, Response, request, jsonify
from flask_cors import CORS
import json
from base import Model
from auth import check_login

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:8080"])
app.secret_key = b'2L"Fsf3GWSE#4Q8z]fxghsd/'

app.config["SESSION_COOKIE_SAMESITE"] = "None"
app.config["SESSION_COOKIE_SECURE"] = "True"


@app.route('/api/login', methods=['GET'])
def get_is_logged_in():
    return jsonify({
        "loggedin": session.get('loggedin', False),
        "login": session.get('login', ""),
    })

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    if check_login(data.get('login', ""), data.get('password', "")):
        session['loggedin'] = True
        session['login'] = data.get('login', "")
        return jsonify({
            "loggedin": session.get('loggedin', False),
            "login": session.get('login', ""),
        })
    else:
        return Response(status=403)

@app.route('/api/login', methods=['DELETE'])
def unlogin():
    session['loggedin'] = False
    session['login'] = ""
    return Response(status=200)


@app.route('/api/keys', methods=['GET'])
def get_keys():
    if not session.get('loggedin', False):
        return Response(status=403)
    model = Model()
    return jsonify({"data": model.keys_get()})

@app.route('/api/keys', methods=['POST'])
def add_key():
    if not session.get('loggedin', False):
        return Response(status=403)
    model = Model()
    data = request.get_json()
    model.keys_add(data["name"], data["key"], data["pub_key"])
    return Response(status=200)


@app.route('/api/keys', methods=['DELETE'])
def delete_keys():
    if not session.get('loggedin', False):
        return Response(status=403)
    model = Model()
    data = request.get_json()
    model.keys_delete(data["id"])
    return Response(status=200)


@app.route('/api/scripts', methods=['GET'])
def get_scripts():
    if not session.get('loggedin', False):
        return Response(status=403)
    model = Model()
    return jsonify({"data": model.scripts_get()})

@app.route('/api/scripts', methods=['POST'])
def add_scripts():
    if not session.get('loggedin', False):
        return Response(status=403)
    model = Model()
    data = request.get_json()
    model.scripts_add(data["name"], data["script"], session.get("login", ""))
    return Response(status=200)

@app.route('/api/scripts', methods=['DELETE'])
def delete_scripts():
    if not session.get('loggedin', False):
        return Response(status=403)
    model = Model()
    data = request.get_json()
    model.scripts_delete(data["id"])
    return Response(status=200)


@app.route('/api/servers', methods=['GET'])
def get_servers():
    if not session.get('loggedin', False):
        return Response(status=403)
    model = Model()
    return jsonify({"data": model.servers_get()})

@app.route('/api/servers', methods=['POST'])
def add_servers():
    if not session.get('loggedin', False):
        return Response(status=403)
    model = Model()
    data = request.get_json()
    model.servers_add(data["name"], data["host"], data["port"], session.get("login", ""), data["key_id"], data["script_id"])
    return Response(status=200)

@app.route('/api/servers', methods=['DELETE'])
def delete_servers():
    if not session.get('loggedin', False):
        return Response(status=403)
    model = Model()
    data = request.get_json()
    model.servers_delete(data["id"])
    return Response(status=200)


@app.route('/api/vm_reserve', methods=['GET'])
def get_vm_reserve():
    if not session.get('loggedin', False):
        return Response(status=403)
    pass

@app.route('/api/vm_reserve', methods=['POST'])
def add_vm_reserve():
    if not session.get('loggedin', False):
        return Response(status=403)
    pass

@app.route('/api/ vm_reserve ', methods=['DELETE'])
def delete_vm_reserve():
    if not session.get('loggedin', False):
        return Response(status=403)
    pass


@app.route('/api/vm', methods=['GET'])
def get_vm():
    if not session.get('loggedin', False):
        return Response(status=403)
    pass

@app.route('/api/vm', methods=['DELETE'])
def delete_vm():
    if not session.get('loggedin', False):
        return Response(status=403)
    pass


if __name__ == '__main__':
    app.run()