from flask import Flask, request, jsonify, Blueprint
from flask_restful import Resource,reqparse,Api
from dao import userdao
from sqlalchemy import create_engine, text

app = Flask(__name__)
api = Api(app)

bp_user = Blueprint("user", __name__, url_prefix="/user")

#Create
@app.route('/signup', methods=['POST'])
def createUser():
    try:
        parser = request.get_json()
        userdao.createUser(parser['userid'], parser['pwd'])
        return {'createUser_result':'ok'}
    except Exception as e:
        return {'error': str(e)}

#Read
@app.route('/user', methods=['GET'])
def getAllUsers():
    return userdao.getAllUsers()

#Update
@app.route('/update', methods=['POST'])
def updateUser():
    try:
        parser = request.get_json()
        userdao.updateUser(parser['userid'], parser['pwd'])
        return {'updateUser_result': 'ok'}
    except Exception as e:
        return {'error': str(e)}

#Delete
@app.route('/delete', methods=['POST'])
def deleteUser():
    try:
        parser = request.get_json()
        userdao.deleteUser(parser['userid'])
        return {'deleteUser_result': 'ok'}
    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    app.run()
    #실제 서버에서 실행시키고, 외부에서 접속 가능하게 하려면
    #app.run(host = 0.0.0.0) 이라고 적어주면 된다.