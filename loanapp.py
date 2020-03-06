## Loan Repayment Calculator ##
##  Author : Parthiban NS  ####
###############################

from flask import Flask, render_template, request, flash
from wtforms import Form, TextField, StringField, SubmitField, TextAreaField, validators
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms.validators import Required


# Configuration details
app = Flask(__name__)
#DEBUG = True
app.config['SECRET_KEY'] = 'secretkey@#)(*&^nomess/'

# class MyForm(Form):
#     name = TextField('Name:', validators=[validators.required()])

'''''edit >>'''
@app.route("/", methods=['GET', 'POST'])
def hello():
    name = 'Timon'
    #'''  form = MyForm() '''
    #return
     # <html>
     #     <head>
     #         <title>Home Page - Microblog</title>
     #     </head>
     #     <body>
     #         <h1>Hello, ''' + user['username'] + '''!</h1>
     #     </body>
     # </html>'''

    return render_template('hello.html', name=name)

'''''<<<edit '''


if __name__ == "__main__":
    app.run(debug=True)