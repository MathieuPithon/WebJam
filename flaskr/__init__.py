import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

# Creation du dossier instance
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

@app.route('/pyscript.json')
def pyscript_config():
    return send_from_directory('.', 'pyscript.json')

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/hello')
def hello():
    return render_template('home/hello.html')
    
