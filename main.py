from flask import Flask

from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/business')
def business():
    return render_template('business.html')

@app.route('/goFundme')
def goFUndMe():
    return render_template('goFundMe.html')

@app.route('/help')
def help():
    return render_template('help.html')


if __name__ == '__main__':
    app.run()
