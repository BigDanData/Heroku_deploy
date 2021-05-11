#importing libraries
import flask
import pandas as pd
import joblib
from flask import Flask, render_template, request
#creating instance of the class
app=Flask(__name__)
#to tell flask what url shoud trigger the function index()
@app.route('/')
@app.route('/index')
def index():
  return flask.render_template('index.html')
def ValuePredictor(to_predict_list):
  a = [to_predict_list]
  b = ["variable a", "variable b", "variable c"]
  to_predict = pd.DataFrame(a, columns=b)
  for col in b:
    to_predict[col] = to_predict[col].astype('float')
  loaded_model = joblib.load("modelo.pkl")
  result = loaded_model.predict_proba(to_predict)[:,1]
  return result[0]
@app.route('/result', methods = ['POST'])
def result():
  if request.method == 'POST':
    to_predict_list = request.form.to_dict()
    to_predict_list = list(to_predict_list.values())

    try:
      prediction = ValuePredictor(to_predict_list)
      #prediction = to_predict_list

    except ValueError:
      prediction="Error en el formato de los datos"
    return render_template("result.html", prediction=prediction)

if __name__=="__main__":
  app.run(debug=False, port=5000)