from flask import Flask, redirect, url_for, render_template, request
import json
import pandas as pd

app = Flask(__name__)

@app.route("/")
def main():
   input_file =  open('./schema/Data.json', "r", encoding="utf-8")
   json_array = json.load(input_file)
   return render_template("main.html", data=json_array)

if __name__ == "__main__":
    app.run()