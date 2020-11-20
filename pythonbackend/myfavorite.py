# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 12:30:14 2020

@author: Star
"""

import pymysql
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

# 数据库连接
db = pymysql.connect("localhost", "root", "412332", "myfavorite")
cursor = db.cursor()  # 指针

# 后端服务启动
app = Flask(__name__)
CORS(app, resources=r'/*')


# 第一个为后端接口的路径
# 登录list
@app.route('/login/list', methods=['POST'])  # 获取信息
def login_list():
    if request.method == "POST":
        # username = request.form.get("username")#接受前端发来的参数

        cursor.execute("SELECT id ,username,role,ctime FROM login")
        data = cursor.fetchall()
        temp = {}
        result = []
        if (data != None):

            for i in data:
                temp["id"] = i[0]
                temp["username"] = i[1]
                temp["role"] = i[2]
                temp["ctime"] = i[3]

                # 这里如果不加.copy(),那么得到的会是相同的
                # 因为得到的是内存的引用，而不是新的内存
                result.append(temp.copy())
            print("result:", len(data))
            return jsonify(result)
        else:
            print("result:NULL")
            return jsonify([])


# login添加
@app.route('/login/add', methods=['POST'])  # 获取信息
def login_add():
    if request.method == "POST":

        # 接受表单里的数据
        username = request.form.get("username")  # 接受前端发来的参数
        password = request.form.get("password")
        role = request.form.get("role")

        # 注意增是不一定会成功的，比如空间已满，立即推 -> try
        try:
            # 注意反斜杠   这里sql语句要大写！否则报错
            cursor.execute("INSERT INTO login(username,password,role) VALUES (\"" + str(username)
                           + "\",\"" + str(password) + "\"," + str(role) + ")")
            # 增删改都需要提交操作
            db.commit()
            print("add a new user successfully")
            return "1"  # 这里要带引号，不能直接返回1
        except Exception as e:
            print("add a new user failed:", e)
            db.rollback()  # 失败则回滚操作
            return "-1"


# login登录
@app.route('/login/login', methods=['POST'])
def login_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        cursor.execute("select id,username,role,ctime from login where username=\""
                       + str(username) + "\" and password=\"" + str(password) + "\"")
        data = cursor.fetchone()
        if (data != None):
            print("result:", data)

            jsondata = {"id": str(data[0]), "username": str(data[1]),
                        "role": str(data[2]), " ctime ": str(data[3])}

            return jsonify(jsondata)

        else:
            print("result:NULL")
            jsondata = {}
            return jsonify(jsondata)


# login删除
@app.route('/login/del', methods=['POST'])  # 获取信息
def login_del():
    if request.method == "POST":

        # 对于删除，只需要对id即可
        id = request.form.get("id")

        # 注意删也是不一定会成功的
        try:
            # 注意反斜杠   这里sql语句要大写！否则报错
            cursor.execute("DELETE FROM login WHERE id=" + str(id))
            # 增删改都需要提交操作
            db.commit()
            print("DELETE a new user successfully")
            return "1"  # 这里要带引号，不能直接返回1
        except Exception as e:
            print("delete a new user failed:", e)
            db.rollback()  # 失败则回滚操作
            return "-1"


# login更新
@app.route('/login/update', methods=['POST'])  # 获取信息
def login_update():
    if request.method == "POST":

        # 对于删除，只需要对id即可
        id = request.form.get("id")
        password = request.form.get("password")

        # 注意更新也是不一定会成功的
        try:
            # 注意反斜杠   这里sql语句要大写！否则报错
            cursor.execute("UPDATE login SET password=\"" + str(password) + "\" where id=" + str(id))
            # 增删改都需要提交操作
            db.commit()
            print("updete a new user successfully")
            return "1"  # 这里要带引号，不能直接返回1
        except Exception as e:
            print("update a new user failed:", e)
            db.rollback()  # 失败则回滚操作
            return "-1"


# login更新update_role
@app.route('/login/update_role', methods=['POST'])
def login_update_role():
    if request.method == "POST":
        id = request.form.get("id")
        role = request.form.get("role")
        try:
            cursor.execute("UPDATE login SET role=\"" + str(role)
                           + "\"WHERE id =" + str(id))
            db.commit()
            print("updete role successfully")
            return "1"  # 这里要带引号，不能直接返回1
        except Exception as e:
            print("update role failed:", e)
            db.rollback()  # 失败则回滚操作


# favorite列表
@app.route('/favorite/list', methods=['POST'])
def favorite_list():
    if request.method == "POST":
        uid = request.form.get("uid")
        if (uid == 0):  # 查询所有公开的收藏数据
            cursor.execute("SELECT id,wname,wurl,uid,type,cout,ctime FROM favorite"
                           + "WHERE type=0 order by cout desc")
        else:
            cursor.execute("SELECT id,wname,wurl,uid,type,cout,ctime FROM favorite"
                           + "WHERE type=0 or uid= " + str(uid) + " order by cout desc ")
    data = cursor.fetchall()
    temp = {}
    result = []
    if (data != None):
        for i in data:
            temp["id"] = i[0]
            temp["wname"] = i[1]
            temp["wurl"] = i[2]
            temp["uid"] = i[3]
            temp["type"] = i[4]
            temp["count"] = i[5]
            temp["ctime"] = i[6]
            result.append(temp.copy())
        print("result:", len(data))
        return jsonify(result)
    else:
        print("result:NULL")
        return jsonify([])


# favorite添加
@app.route('/favorite/add', methods=['POST'])
def favorite_add():
    if request.method == "POST":
        wname = request.form.get("wname")
        wurl = request.form.get("wurl")
        uid = request.form.get("uid")
        _type = request.form.get("type")
    try:
        cursor.execute("INSERT INTO favorite(wname,wurl,uid,type) VALUES (\""
                       + str(wname) + "\",\"" + str(wurl) + "\",\"" + str(uid) + "\",\"" + str(_type) + "\")")
        db.commit()
        print("add a new favorite successfully")
        return "1"
    except Exception as e:
        print("add a new favorite failed:", e)
        db.rollback()
        return "-1"


# favorite删除
@app.route('/favorite/del', methods=['POST'])  # 获取信息
def favorite_del():
    if request.method == "POST":

        # 对于删除，只需要对id即可
        id = request.form.get("id")

        # 注意删也是不一定会成功的
        try:
            # 注意反斜杠   这里sql语句要大写！否则报错
            cursor.execute("DELETE FROM favorite WHERE id=" + str(id))
            # 增删改都需要提交操作
            db.commit()
            print("delete favorite " + str(id) + " successfully")
            return "1"  # 这里要带引号，不能直接返回1
        except Exception as e:
            print("delete the favorite failed:", e)
            db.rollback()  # 失败则回滚操作
            return "-1"


# favorite更新
@app.route('/favorite/update', methods=['POST'])  # 获取信息
def favorite_update():
    if request.method == "POST":
        id = request.form.get("id")
        wname = request.form.get("wname")
        wurl = request.form.get("wurl")
        _type = request.form.get("type")

        # 注意更新也是不一定会成功的
        try:
            # 注意反斜杠   这里sql语句要大写！否则报错
            cursor.execute("UPDATE login SET wname=\"" + str(wname) + "\" ,wurl=\"" + str(wurl) +
                           "\",type=\"" + str(_type) + "\" where id=" + str(id))
            # 增删改都需要提交操作
            db.commit()
            print("updete favorite successfully")
            return "1"  # 这里要带引号，不能直接返回1
        except Exception as e:
            print("update favorite failed:", e)
            db.rollback()  # 失败则回滚操作
            return "-1"


# 再加一个计数操作
@app.route('/favorite/count', methods=['POST'])
def favorite_count():
    if request.method == "POST":
        id = request.form.get("id")
        try:
            cursor.execute("UPDATE favorite SET count=count+1 where id=" + str(id))
            db.commit()
            print("count successfully")
            return "1"  # 这里要带引号，不能直接返回1
        except Exception as e:
            print("count failed:", e)
            db.rollback()  # 失败则回滚操作
            return "-1"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000)
    db.close()
    print("bye")
