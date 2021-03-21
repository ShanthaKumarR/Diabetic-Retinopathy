from flask import Flask, render_template, request
import joblib
#import pandas as pd 
import numpy as np 

posts = [
    {'author': 'Raja sekar Shantha kumar', 'data_posted': 'updated on March 19, 2021', 'Title': 'Diabetic Retinopathy classification (AI for medicine)' 
    ,'Algorithm': 'Logistic regression'}]

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('home.html', posts = posts, title='Machine_learning')

@app.route('/displayResult', methods = ['GET', 'POST'])
def displayResult():   
    if request.method == 'POST':
        try:
            Age = int(request.form['Age'])
            
            Diastolic_BP = float(request.form['Diastolic_BP'])
            Systolic_BP = float(request.form['Systolic_BP'])
            Cholestrol = float(request.form['Cholestrol'])
            test_data = [Age, Systolic_BP, Diastolic_BP, Cholestrol]
            test_data = np.array(test_data)
            test_data = test_data.reshape(1, -1)
            model = open('lr_model.sav', "rb")
            model = joblib.load(model)
            result = model.predict(test_data)
            if result ==0:
                result = "Yes, The patient is eventually get the disease Diabetic Retinopathy"
            else:
                result = "No, The patient is not eventually get the disease Diabetic Retinopathy"
        except ValueError:
            return 'please check the entered value'
    return render_template('displayResult.html', prediction = result, title='Result')


if __name__=="__main__":
    app.run(debug=True)