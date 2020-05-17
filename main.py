from flask import Flask, url_for
from flask import render_template
from markupsafe import escape
from flask import request

import pdb
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tinyurl',methods=['POST'])
def tinyurl():
    return render_template('index.html', long=request.form['longurl'], short="to implement")
