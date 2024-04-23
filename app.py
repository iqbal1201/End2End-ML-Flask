from flask import Flask, request, render_template, jsonify
import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np


# Scaler
scaler = StandardScaler()


# Create flask app
app = Flask(__name__)


# Load the pickle model
model = pickle.load(open("model_selected.pkl", "rb"))

class_cat = ['Gonen', 'Jasmine'] # Define the class of dataset


# Design the web using Flask
@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = np.array(float_features)
    features = features.reshape(1,-1)
    features = scaler.fit_transform(features)

    prediction = model.predict(features)

    return render_template("index.html", prediction_text = "The Rice Type is {}".format(class_cat[int(prediction)]))

if __name__ == "__main__":
    app.run(debug=True, port=5000)