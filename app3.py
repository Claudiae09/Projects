from flask import Flask, render_template, request
import os
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, RadioField, SelectField, SubmitField


app =  Flask(__name__)
app.secret_key=os.urandom(24)

class SignUp(FlaskForm):
    First_Name = StringField('Enter your first name')
    Last_Name = StringField('Enter your last name')
    Email = StringField('Enter your email')
    PID = IntegerField('Enter your Panther ID')
    Campus = RadioField('Select your campus', choices=[
        ('MMC', 'Modesto Madique'),
        ('BBC', 'Biscayne Bay'),
        ('DC', 'FIU in DC'),
        ('EC', 'Engineering Center')
    ])
    Major = SelectField('Select your major', choices=[
        ('IT','Information Technology'),
        ('DS', 'Data Science and AI'),
        ('cs', 'Computer Science'),
        ('cys','CyberSecurity'),
    ])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    myForm = SignUp(request.form)
    if request.method == 'POST':
        firstName = request.form["First_Name"]
        return render_template("Success.html", firstName=firstName)

    else:
        return render_template("signup.html", form=myForm)

if __name__ == '__main__':
    app.run(debug=True, port = 7070)