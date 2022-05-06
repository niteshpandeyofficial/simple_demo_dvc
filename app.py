from flask import Flask,render_template,request,jsonify
import os
import joblib
import yaml 
import numpy as np


params_path="params.yaml"
webapp_root="webapp"

static_dir=os.path.join(webapp_root,"static")
template_dir=os.path.join(webapp_root,"templates")

app=Flask(__name__,static_folder=static_dir,template_folder=template_dir)

if  __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)