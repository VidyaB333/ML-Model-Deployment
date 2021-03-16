from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)
#Unpickling the ML model to use for prediction
with open(r"C:\Users\vidya\OneDrive\Desktop\Python_coding_practice_Datasets\PythonDataSets\Logistic_Regression\purchased.pkl", 'rb') as file:
    model = pickle.load(file)
    print(model)


@app.route('/')
def home():
    return render_template('predict.html')

@app.route("/info")
def info():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    prediction = round(prediction[0], 2)
    output= 'NO'
    if prediction == 1:
        output = 'YES'
    else:
        output = 'NO'
    print('Output is : ', output)
    return render_template('predict.html', prediction_text= f'Person can take car : {output}')


if __name__ == '__main__':
    app.run(debug=True)
