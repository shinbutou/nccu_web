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
def report():
   print(db_array[0])
def manage():
   print(db_array[1])

if __name__ == "__main__":
    app.run()