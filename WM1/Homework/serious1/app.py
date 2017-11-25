from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to BMI calculator"

@app.route('/bmi/<int:weight>/<int:height>')
def BMI(weight, height):
    meter = height * 0.01
    BMI = height /(meter ** 2 )
    # print(BMI)
    if BMI < 16:
        condition = 'Severely underweight'
    elif BMI < 18.5:
        condition = 'Underweight'
    elif BMI < 25:
        condition = 'Normal'
    elif BMI < 30:
        condition = 'Overweight'
    else:
        condition = 'Obese'
    return "BMI=" + str(BMI) + ': '+ condition
if __name__ == '__main__':
  app.run(debug=True)
