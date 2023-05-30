from flask import render_template, redirect, url_for, Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)




@app.route('/')
def load_main_page():
    return render_template('Home.html')

@app.route('/StepOne')
def load_first_page():
    return render_template('StepOne.html')

@app.route('/StepTwo')
def load_second_page():
    return render_template('StepTwo.html')

@app.route('/StepThree')
def load_third_page():
    return render_template('StepThree.html')

@app.route('/StepFour')
def load_fourth_page():
    return render_template('StepFour.html')

@app.route('/StepFive')
def load_five_page():
    return render_template('StepFive.html')

@app.route('/StepSix')
def load_six_page():
    return render_template('StepSix.html')

@app.route('/StepSeven')
def load_seven_page():
    return render_template('StepSeven.html')


if __name__ == '__main__':
    app.run(debug=True)
