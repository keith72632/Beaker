import re
import numpy as np
from flask import Flask, app, render_template, request, send_file
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

@application.route('/login')
def login():
    return render_template('login.html')

@application.route('/login', methods=['POST'])
def login_from():
    if request.method == "POST":
        text = request.form['name']
        passwd = request.form['passwd']

@application.route('/contribute', methods=['GET', 'POST'])
def contribute():
    finvalues = []
    values = request.form.values()
    for value in values:
        if type(value) == str:
            value == 0
            finvalues.append(value)
        else:
            finvalues.append(value)
    for value in finvalues:
        if value:
            print(value, file=sys.stderr)
    return render_template('contribute.html')


@application.route('/contact')
def contacts():
    return render_template('contact.html')

@application.route('/api/file_download')
def download():
    return send_file('files/template.csv')

if __name__ == "__main__":
    application.debug(True)