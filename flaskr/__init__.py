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
# Route pour servir main.py depuis le dossier projects
@app.route('/projects/<path:filename>')
def serve_projects_files(filename):
    return send_from_directory('projects', filename)

@app.route('/pyscript.json')
def serve_pyscript_config():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'pyscript.json')

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/hello')
def hello():
    return render_template('home/hello.html')
    
