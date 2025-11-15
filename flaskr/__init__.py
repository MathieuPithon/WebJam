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
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Page d'accueil</title>
        <link rel="apple-touch-icon" sizes="180x180" href="{{ url_for('static', filename='favicon/apple-touch-icon.png') }}">
        <link rel="icon" type="image/png" sizes="32x32" href="{{ url_for('static', filename='favicon/favicon-32x32.png') }}">
        <link rel="icon" type="image/png" sizes="16x16" href="{{ url_for('static', filename='favicon/favicon-16x16.png') }}">
        <link rel="manifest" href="{{ url_for('static', filename='favicon/site.webmanifest') }}">
        <link rel="mask-icon" href="{{ url_for('static', filename='favicon/safari-pinned-tab.svg') }}" color="#5bbad5">
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                margin: 10px;
                background-color: #007bff;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }
            .button:hover {
                background-color: #0056b3;
            }
        </style>
    </head>
    <body>
        <h1>Bienvenue sur ma page d'accueil!</h1>
        <a href="/hello" class="button">Aller à Hello</a>
    </body>
    </html>
    '''

@app.route('/hello')
def hello():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Page Hello</title>
        <link rel="apple-touch-icon" sizes="180x180" href="{{ url_for('static', filename='favicon/apple-touch-icon.png') }}">
        <link rel="icon" type="image/png" sizes="32x32" href="{{ url_for('static', filename='favicon/favicon-32x32.png') }}">
        <link rel="icon" type="image/png" sizes="16x16" href="{{ url_for('static', filename='favicon/favicon-16x16.png') }}">
        <link rel="manifest" href="{{ url_for('static', filename='favicon/site.webmanifest') }}">
        <link rel="mask-icon" href="{{ url_for('static', filename='favicon/safari-pinned-tab.svg') }}" color="#5bbad5">
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            .button {
                display: inline-block;
                padding: 10px 20px;
                margin: 10px;
                background-color: #28a745;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                cursor: pointer;
            }
            .button:hover {
                background-color: #1e7e34;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <a href="/" class="button">Retour à l'accueil</a>
    </body>
    </html>
    '''