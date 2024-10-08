import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the regression model and scaler
regmodel = pickle.load(open('regression.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))  # Make sure the scaler file is present

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    data_array = np.array(list(data.values())).reshape(1, -1)
    new_data = scaler.transform(data_array)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

#@app.route('/predict', methods=['POST'])
##def predict():
    ##data = [float(x) for x in request.form.values()]
    #final_input = scaler.transform(np.array(data).reshape(1, -1))
    #print(final_input)
    #output = regmodel.predict(final_input)[0]
    #return render_template("home.html", prediction_text=f"The Predicted Price is {output}")

if __name__ == "__main__":
    app.run(debug=True)
