from flask import Flask , render_template,request
from flask_cors import CORS
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
import os
import base64
from combine import *
import json

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

CORS(app)


@app.route("/",methods=["GET","POST"])
def main():

    return render_template("index.html")


@app.route('/saveImg',methods =['POST',"GET"])
def save_Img():
    if request.method == "POST":
        list_img = os.listdir("static/images/output")
        for img in list_img:
            path = "static/images/output/" + img
            os.remove(path)
        img_1_edges = ((int(float(request.form["img1_y1"])),int(float(request.form["img1_y2"]))),(int(float(request.form["img1_x1"])),int(float(request.form["img1_x2"]))))
        img_2_edges = ((int(float(request.form["img2_y1"])),int(float(request.form["img2_y2"]))),(int(float(request.form["img2_x1"])),int(float(request.form["img2_x2"]))))
        option = request.form["option"]
        #save original images
        saveImg(base64.b64decode(request.form["original_1"].split(',')[1]),'./static/images/input/original1.png')
        saveImg(base64.b64decode(request.form["original_2"].split(',')[1]),'./static/images/input/original2.png')
        combined_img = get_combined(option,img_1_edges,img_2_edges,request.form["checkbox"],request.form["checkbox_Magnitude"])
    return json.dumps({1: f'<img src="{combined_img}"  id="comb_img" alt="" >'})

if __name__ == "__main__":
    app.run(debug=True)


