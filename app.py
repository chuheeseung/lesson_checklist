from pymongo import MongoClient

from flask import Flask, render_template, jsonify, request

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
    #클라이언트로부터 데이터를 받기
    target = request.form['target']
    isChecked = request.form['isChecked']

    list = {
        'target' : target,
        'isChecked' : isChecked
    }

    db.checkList.insert_one(list)

    return jsonify({'result':'success','msg':' post 확인!'})

# #완료된 체크박스 보여주기 READ
@app.route('/check', methods=['GET'])
def get_checkBox():
    result = list(db.checkList.find({},{'_id':False}))

    return jsonify({'result':'success','articles':result})

#원래 체크했는데 체크 바뀌는 경우 UPDATE

#체크 다 지워버리기 DELETE

#강의 전체 지워버리기 DELETE

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)