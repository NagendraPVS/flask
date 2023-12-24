from flask import Flask,Response,request,jsonify
from flask_cors import CORS
import mysql.connector

app=Flask(__name__)
cors=CORS(app,resources={"/*":{"origins":"*"}})

db=mysql.connector.connect(host="localhost",port="3306",user="nagendra",password="2338",database="flask")
cursor=db.cursor()
#views
@app.route('/insert',methods=['POST'])
def insert():
    data=request.get_json()
    query="insert into credentials values('"+data["id"]+"','"+data["name"]+"',"+data["marks"]+")"
    print(query)
    try:
        cursor.execute(query)
        db.commit()
        return jsonify({"status":"success"})

    except Exception as e:
        print(e)
        db.rollback()
        return jsonify({"status":"failure"})

@app.route('/update',methods=['POST'])
def update():
    data=request.get_json()
    print(data)
    query=f"update credentials set password='{data['password']}' ,marks={data['marks']} where id='{data['id']}'"
    print(query)
    try:
        cursor.execute(query)
        db.commit()
        return jsonify({"status":"success"})

    except Exception as e:
        
        db.rollback()
        return jsonify({"status":f"{e}"})
@app.route("/delete",methods=['GET'])
def delete():
    query=f'delete from credentials where id={request.args["id"]}'
    try:
        cursor.execute(query)
        db.commit()
        return jsonify({"status":"success"})
    except Exception as e:
        db.rollback()
        return jsonify({"status":e})

@app.route("/contents",methods=['POST'])
def content():
    query="select id from credentials;"
    cursor.execute(query)
    res=cursor.fetchall()
    return jsonify({"contents":res})
if(__name__=="__main__"):
    app.run(debug=True)