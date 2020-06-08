from flask import Flask, redirect, url_for, render_template, request
import json
import pandas as pd

app = Flask(__name__)

@app.route("/")
def main():
   db_file =  open("./schema/Data.json", "r", encoding="utf-8")
   db_array = json.load(db_file)
   db2_file =  open("./schema/data2.json", "r", encoding="utf-8")
   db2_array = json.load(db2_file)
   return render_template("main.html", data = db_array , data2 = db2_array)

@app.route("/main.html", methods=["POST", "GET"])
def rsubmit():
    if request.method == "GET":

        con = request.values['con']     
        des = request.values['des']
        loc = request.values['loc']
        lat = request.values['lat']
        lon = request.values['lon']

        newData = {
            "Condition":con,
            "Description":des,
            "Location":loc,
            "lat":lat,
            "lon":lon
        }
        
        read_file =  open("./schema/Data.json", "r",encoding="utf-8")
        json_array = json.load(read_file)
         
        json_array.append(newData)
        
        input_file =  open("./schema/Data.json", "w",encoding="utf-8")
        json.dump(json_array,input_file,ensure_ascii=False) 
   
        db2_file =  open("./schema/data2.json", "r", encoding="utf-8")
        db2_array = json.load(db2_file)

        return render_template("main.html", data = json_array, data2 = db2_array)
 

if __name__ == "__main__":
    app.run()