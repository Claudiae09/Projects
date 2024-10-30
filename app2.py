import os
from datetime import date

from flask import Flask, render_template

app = Flask (__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    first_name = "Claudia"
    last_name = "Espinosa"
    today = date.today()
    return render_template("index.html", fn=first_name, ln=last_name, updated = today)
#inside render_template X=Y
# X is the variable in html
#Y is the variable in python

@app.route('/courses')
def courses():
    courses=["COP 4814", "COP 5234"]
    return render_template("courses.html", courses=courses)

if __name__ == '__main__':
    app.run(debug=True)