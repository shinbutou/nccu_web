from flask import Flask, redirect, url_for, render_template, request
import json
import pandas as pd

app = Flask(__name__)

@app.route("/")
def main():
   db_file =  open("./schema/Data.json", "r", encoding="utf-8")
   db_array = json.load(db_file)
   return render_template("main.html", data=db_array)


@app.route("/main.html", methods=["POST", "GET"])
def rsubmit():
    if request.method == "GET":

        Con = request.values['con']     
        Des = request.values['des']
        Loc = request.values['loc']
        Lat = request.values['lat']
        Lon = request.values['lon']

        newData = {
            "Condition":Con,
            "Description":Des,
            "Location":Loc,
            "lat":Lat,
            "lon":Lon
        }
        
        read_file =  open("./schema/Data.json","r",encoding="utf-8")
        json_array = json.load(read_file)
         
        json_array.append(newData)
        
        input_file =  open("./schema/Data.json","w",encoding="utf-8")
        json.dump(json_array,input_file,ensure_ascii=False) 

        return render_template("main.html", data = json_array)    
        

if __name__ == "__main__":
    app.run()