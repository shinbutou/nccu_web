from flask import Flask, redirect, url_for, render_template, request, session
import json
import pandas as pd
import datetime
from datetime import timedelta
import random

app = Flask(__name__)

@app.route("/")
def init():
    return render_template("login.html")


@app.route("/login.html", methods=["GET", "POST"])
def register():
    #login functions
    if request.method == "GET":
        lusr = request.values['usr']
        lpwd = request.values['pwd']

        user_db =  open("./schema/user.json", "r",encoding="utf-8")
        src = json.load(user_db)
        for entry in src:
            if lusr == entry['username']:
                ref = entry['password']
                pid = entry['nickname']
                if str(lpwd) == str(ref):
                    db_file =  open("./schema/data.json", "r", encoding="utf-8")
                    db_array = json.load(db_file)
                    return render_template("main.html", data = db_array)
                else:
                    return render_template("login.html")

    #register functions
    if request.method == "POST":
        user = request.values['rusr']
        pwd = request.values['rpwd']
        cnf = request.values['rpwd2']
        nckn = request.values['rnckn']

        if str(pwd) == str(cnf):
            user_list =  open("./schema/user.json", "r",encoding="utf-8")
            user_data = json.load(user_list)

            n = len(user_data)
            nstr = str(n)
            idstr = "p"+nstr
            
            nentry = {
                "username":user,
                "password":pwd,
                "nickname":nckn
            }

            user_data.append(nentry)

            with open(f'./schema/user.json', 'w') as json_file:
                json.dump(user_data, json_file)
                json_file.close()

            return render_template("login.html")
    else:
        return render_template("login.html")


@app.route("/main.html", methods=["POST", "GET"])
def rsubmit():
    if request.method == "GET":

        con = request.values['con']     
        des = request.values['des']
        dis = request.values['dis']
        lat = request.values['lat']
        lon = request.values['lon']
        x = datetime.datetime.now()
        mth = x.month
        dat = x.day
        hr = x.hour
        sv = random.randint(0,1) 
        
        read_file =  open("./schema/data.json", "r",encoding="utf-8")
        json_array = json.load(read_file)
        
        n = len(json_array)
        nstr = str(n)
        idstr = "n"+nstr

        newData = {
            "id":idstr,
            "Condition":con,
            "Description":des,
            "dis":dis,
            "lat":lat,
            "lon":lon, 
            "mth":mth,
            "dat":dat,
            "hr":hr,
            "sv":sv
        }
              
        json_array.append(newData)
        
        input_file =  open("./schema/data.json", "w",encoding="utf-8")
        json.dump(json_array,input_file,ensure_ascii=False) 
   
        return render_template("main.html", data = json_array)
 

if __name__ == "__main__":
    app.run()