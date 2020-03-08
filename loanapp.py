## Loan Repayment Calculator ##
##  Author : Parthiban NS  ####
###############################
from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, StringField, IntegerField, SubmitField, TextAreaField, validators
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.validators import Required, DataRequired
from calc import calc

# Configuration details
app = Flask(__name__)
#DEBUG = True
app.config['SECRET_KEY'] = 'secretkey@#)(*&^nomess/'

class MyForm(FlaskForm):
    loan_amount = IntegerField('Loan Amount', [validators.DataRequired(message=("Field cannot be empty"))])
    rate = IntegerField('Rate of Interest', [validators.DataRequired(message=("Field cannot be empty"))])
    loan_period = IntegerField('Loan Period (months)', [validators.DataRequired(message=("Field cannot be empty"))])
    submit = SubmitField('Calculate')

@app.route("/", methods=['GET', 'POST'])
def calculator():
    form = MyForm()
    #data = request.get_data()
    #print(request.data)
    table = []

    if form.validate_on_submit():
        return redirect('/')

    if request.method == 'POST':
        loan_amount = int(request.form.get('loan_amount'))
        rate = int(request.form.get('rate'))
        loan_period = int(request.form.get('loan_period'))
        table = calc(loan_amount, rate, loan_period)
    return render_template('table.html', table=table, form=form)


if __name__ == "__main__":
    app.run(debug=True)