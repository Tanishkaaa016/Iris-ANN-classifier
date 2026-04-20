from flask import Flask, render_template, request, jsonify
import numpy as np
import joblib
import tensorflow as tf

app = Flask(__name__)

model = None
scaler = None

def load_model_once():
    global model, scaler
    if model is None:
        model = tf.keras.models.load_model("iris_model.h5")
        scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    load_model_once()

    data = request.json["features"]
    data = np.array(data).reshape(1, -1)

    data = scaler.transform(data)
    prediction = model.predict(data)[0]

    return jsonify({
        "probabilities": prediction.tolist(),
        "predicted_class": int(np.argmax(prediction))
    })

if __name__ == "__main__":
    app.run(debug=True)