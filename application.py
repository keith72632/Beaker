import numpy as np
from flask import Flask, app, render_template, request
import pickle
import sys

application = Flask(__name__)
model = pickle.load(open('model/watermodel.pkl', 'rb'))

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
    solidsremoved = 0.90
    int_features.append(solidsremoved)
    for x in int_features:
        print(x, file=sys.stderr)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('jartest.html', prediction_text='Optimal Coagulant Dosage: {} mg/l'.format(output))

@application.route('/contact')
def contacts():
    return render_template('contact.html')