from flask import Flask, render_template, requests

posts = [
    {'author': 'Rajasekar', 'data_posted': 'March 19, 2021', 'Title': 'AI for medicine'},
    {'author':'Raja sekar', 'data_posted': 'March 20, 2021', 'Title': 'Machine learning for prognosis'}
]

app = Flask(__name__)

@app.route('/')
def home(): 
    return render_template('home.html', posts = posts, title='Machine_learning')

@app.route('/displayResult', methoda = ['GET', 'POST'])
def displayResult():   
    return render_template('predection.html')

if __name__=="__main__":
    app.run(debug=True)