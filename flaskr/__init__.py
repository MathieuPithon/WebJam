import os
from flask import Flask

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

@app.route('/')
def home():
    return 'Bienvenue sur ma page d\'accueil!'

@app.route('/hello')
def hello():
    return 'Hello, World!'