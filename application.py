import numpy as np
from flask import Flask, render_template, request
import pickle

application = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

#default page of our web-app
@application.route('/')
def homey():
    return render_template('home.html')

@application.route('/jartest')
def jartest():
    return render_template('jartest.html')

@application.route('/predict', methods=['POST'])
def predict():
    # for rendering results on HTML GUI
    int_features = [float(x) for x in request.form.values()]
    forms = slice(1, 4)
    final_features = [np.array(int_features[forms])]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('jartest.html', prediction_text='Optimal Coagulant Dosage: {} mg/l'.format(output))
