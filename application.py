import numpy as np
import pandas as pd
from flask import Flask, app, render_template, request, send_file, redirect
# from flask_mysqldb import MySQL
from flask.helpers import url_for
import pickle
import sys
import traceback


application = Flask(__name__)
model = pickle.load(open('model/watermodel.pkl', 'rb'))

application.config['MYSQL_HOST'] = "beaker.cmgczbvm6udl.us-east-2.rds.amazonaws.com"
application.config['MYSQL_USER'] = 'admin'
application.config['MYSQL_PASSWORD'] = 'thinmint'
application.config['MYSQL_DB'] = 'beakerusers'

# mysql = MySQL(application)
# # HOST = os.environ.get('HOST')
# USER = os.environ.get('USER')
# PASSWD = os.environ.get('PASSWD')
# DB = os.environ.get('DB')

#default page of our web-app
@application.route('/')
def homey():
    # print(os.environ.get('USER'))
    df = pd.read_csv('model/WaterData.csv')
    print(df.describe())
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
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = round(prediction[0], 2)

    return render_template('jartest.html', prediction_text='Optimal Coagulant Dosage: {} mg/l'.format(output))

@application.route('/login', methods=['GET', 'POST'])
def login():
 
    error = None
    if request.method == "POST":
        text = request.form['name']
        passwd = request.form['passwd']
        if text != 'keith' or passwd != 'thinmint':
            error = 'Invalid credentials'
        else:
            # try:
            #     cur = mysql.connection.cursor()
            #     print('Connection to db made')
            #     # cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
            #     mysql.connection.commit()
            #     cur.close()
            # except:
            #     traceback.print_exc()
            return redirect(url_for('contribute'))
    
    return render_template('login.html', error=error)



@application.route('/contribute', methods=['GET', 'POST'])
def contribute():
    if request.method == "POST":
        jarOne = request.form.getlist('jarOne[]')
        jarTwo = request.form.getlist('jarTwo[]')
        jarThree = request.form.getlist('jarThree[]')
        jarFour = request.form.getlist('jarFour[]')
        jarFive = request.form.getlist('jarFive[]')
        jarSix = request.form.getlist('jarSix[]')

    return render_template('contribute.html')


@application.route('/contact')
def contacts():
    return render_template('contact.html')

@application.route('/api/file_download')
def download():
    return send_file('files/template.csv')

@application.route('/data')
def data():
    return render_template('data.html')

if __name__ == "__main__":
    application.run(debug=True)