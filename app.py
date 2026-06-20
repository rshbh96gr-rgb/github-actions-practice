#in this app hashtags added.
#FLASK APP
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    return None

if nnE:
NE


@app.route('/health')
def health():
    return 'Server is up and running'
