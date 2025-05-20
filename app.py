from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Cargar el modelo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
        age = int(request.form['age'])
        sex = int(request.form['sex'])  # 0: mujer, 1: hombre
        education_level = int(request.form['education_level'])  # codificado
        occupation = int(request.form['occupation'])  # codificado
        hours_worked = float(request.form['hours_worked'])

        features = np.array([[age, sex, education_level, occupation, hours_worked]])

        return f"Error en la predicción"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
