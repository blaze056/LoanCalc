## Loan Repayment Calculator ##
##  Author : Parthiban NS  ####
###############################

from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, StringField, IntegerField, SubmitField, TextAreaField, validators
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.validators import Required, DataRequired


# Configuration details
app = Flask(__name__)
#DEBUG = True
app.config['SECRET_KEY'] = 'secretkey@#)(*&^nomess/'

class MyForm(Form):
    loan_amount = IntegerField('Loan Amount', validators=[DataRequired()])
    rate = IntegerField('Rate of Interest', validators=[DataRequired()])
    loan_period = IntegerField('Loan Period (months)', validators=[DataRequired()])
    submit = SubmitField('Calculate')

'''''edit >>'''
@app.route("/", methods=['GET', 'POST'])
def calculator():
    name = 'Timon'
    form = MyForm()
    #data = request.get_data()
    #print(request.data)
    if request.method == 'POST':
        print(request.form.get('loan_amount'))
        print(request.form.get('rate'))
        print(request.form.get('loan_period'))

    return render_template('table.html', table="text", form=form)


'''''<<<edit '''


if __name__ == "__main__":
    app.run(debug=True)