# app.py
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the pickled model
model = pickle.load(open('dkl.pkl', 'rb'))

def predict_yield(year, avg_rainfall, pesticide_tons, avg_temp):
    predicted_yield = 2.5 * year + 1.5 * avg_rainfall - 0.5 * pesticide_tons + 10 * avg_temp
    return predicted_yield

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        item = request.form['Item']
        year = float(request.form['Year'])
        avg_rainfall = float(request.form['Avg_rain_fall_mm_per_year'])
        pesticides_tons = float(request.form['Pesticides_tons'])
        avg_temp = float(request.form['Avg_temp'])
        
        predicted_yield = predict_yield(year, avg_rainfall, pesticides_tons, avg_temp)
        
        return render_template('index.html', output='Predicted yield: {:.2f}'.format(predicted_yield))

if __name__ == '__main__':
    app.run()
