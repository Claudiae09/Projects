import requests
from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return "Hello Panthers! :)"

@app.route('/about')
def about():
    return ("We are learning about Web Services and web apps")

@app.route('/contact')
def contact():
    return ("You can contact us at panthers@fiu.edu")

@app.route('/learningFlask')
def learningFlask():
    return ("<h1>Flask Framework</h1> <h2>Web Services</h2> <p>Flask is a Python web framework for building web apps and web applications.</p>")

@app.route('/getQuote')
def getQuote():
    url = "http://api.quotable.io/random"
    response = requests.get(url).json()
    quote = response['content']
    author = response['author']
    message = f"""<h2> {quote} By {author}</h2>"""
    return message


if __name__ == '__main__':
    app.run()
