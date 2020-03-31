from flask import Flask
import json 

from flask import render_template
app = Flask(__name__)

with open("data/smallbusiness.json") as a:
    businesses = json.load(a)

with open("data/gofundme.json") as b:
    contributions = json.load(b)

with open("data/resources.json") as c:
    resources = json.load(c)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/relief')
def business():
    return render_template('relief.html', businesses = businesses)

@app.route('/contribute')
def goFUndMe():
    return render_template('contribute.html', contributions = contributions)

@app.route('/resources')
def help():
    return render_template('resources.html', resources = resources)
    
if __name__ == '__main__':
    app.run()
