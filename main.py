from flask import Flask, redirect, url_for, render_template, request
import json
import pandas as pd
import datetime
import random

app = Flask(__name__)

@app.route("/")
def main():
   db_file =  open("./schema/Data.json", "r", encoding="utf-8")
   db_array = json.load(db_file)
 
   return render_template("main.html", data = db_array )

@app.route("/main.html", methods=["POST", "GET"])
def rsubmit():
    if request.method == "GET":

        con = request.values['con']     
        des = request.values['des']
        dis = request.values['dis']
        lat = request.values['lat']
        lon = request.values['lon']
        x = datetime.datetime.now() #現在時間
        mth = x.month
        dat = x.day
        hr = x.hour
        sv = random.randint(0,1) 
        
        read_file =  open("./schema/Data.json", "r",encoding="utf-8")
        json_array = json.load(read_file)
        
        n = len(json_array)+1
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
        
        input_file =  open("./schema/Data.json", "w",encoding="utf-8")
        json.dump(json_array,input_file,ensure_ascii=False) 
   


        return render_template("main.html", data = json_array)
 

if __name__ == "__main__":
    app.run()