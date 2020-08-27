from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import Flask, render_template, jsonify, request
from bson import json_util
app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

#체크박스 체크하면 저장 CREATE
@app.route('/check', methods=['POST'])
def post_checkBox():
    isChecked = request.form['isChecked']
    _id = request.form['_id']
    weekNum = request.form['weekNum']

    if(isChecked == 'true') :
        checkBool = bool('true')
    else:
        checkBool = bool()

    db.newInputList.update_one({'_id' :  ObjectId(_id)}, {'$set' : {weekNum : checkBool}})

    return jsonify({'result':'success','msg':' post 확인!'})

# #완료된 체크박스 보여주기 READ
@app.route('/check', methods=['GET'])
def get_checkBox():
    result = list(db.checkList.find({},{'_id':False}))

    return jsonify({'result':'success','lists':result})



#리스트 새로 추가 CREATE
@app.route('/input',methods=['POST'])
def add_input():
    inputSubject = request.form['inputSubject']
    categoryList = request.form['categoryList']

    list = {
        'inputSubject' : inputSubject,
        'categoryList' : categoryList,
        'week1' : False,
        'week2' : False,
        'week3' : False,
        'week4' : False,
        'week5' : False,
        'week6' : False,
        'week7' : False,
        'week8' : False,
        'week9' : False,
        'week10' : False,
        'week11' : False,
        'week12' : False,
        'week13' : False,
        'week14' : False,
        'week15' : False,
        'week16' : False
    }

    db.newInputList.insert_one(list)

    return jsonify({'result' : 'success', 'msg' : 'POST 연결되었습니다!'})

#추가한 리스트 보여주는 GET
@app.route('/input',methods=['GET'])
def show_tables() :
    result = list(db.newInputList.find({}))

    return json_util.dumps({'result':'success','lists':result})












#체크 다 지워버리기 DELETE

#강의 전체 지워버리기 DELETE

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)