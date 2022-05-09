from flask import Flask,render_template,request,jsonify
import os
import joblib
import yaml 
import numpy as np
from prediction_service.prediction import predict,api_response
webapp_root="webapp"


static_dir=os.path.join(webapp_root,"static")
template_dir=os.path.join(webapp_root,"templates")
print("File location",template_dir)
app=Flask(__name__,static_folder=static_dir,template_folder=template_dir)


@app.route("/",methods=['POST','GET'])
def index():
    if request.method == "POST":
        try:
            if request.form:
                data = dict(request.form).values()
                data = [list(map(float,data))]
                response=predict(data)
                return render_template("index.html", response=response)

            elif request.json:
                response = api_response(request)
                return jsonify(response)

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}

        return render_template("404.html", error=error)
    else:
        return render_template("index.html")

if  __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)