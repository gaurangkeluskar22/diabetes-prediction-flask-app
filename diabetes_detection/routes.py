from flask import jsonify,request,render_template

from diabetes_detection import app,model
from diabetes_detection.utils import *


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/detect',methods=["POST"])
def detect():
    try:
    #     data = request.json
    #     X_test = json2Xtest(data)
    #     diabetes_chance = model.predict_proba(X_test)[0][1] * 100
    #     return jsonify({'diabetes_chance': diabetes_chance})
        data=request.form
        X_test = json2Xtest(data)
        diabetes_chance = model.predict_proba(X_test)[0][1] * 100
        predection_text='NULL'
        #return jsonify({'diabetes_chance': diabetes_chance})
        return render_template('index.html',predection_text='diabetes chance:{}'.format(diabetes_chance))
    except:
        # return jsonify({'error': "Please provide valid data"})
        return render_template('index.html',predection_text='Please provide valid data')
