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
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon/favicon.ico')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Page d'accueil</title>
        <link rel="icon" type="image/png" href="{{ url_for('static', filename='favicon/favicon-96x96.png') }}" sizes="96x96" />
        <link rel="icon" type="image/svg+xml" href="{{ url_for('static', filename='favicon/favicon.svg') }}" />
        <link rel="shortcut icon" href="{{ url_for('static', filename='favicon/favicon.ico') }}" />
        <link rel="apple-touch-icon" sizes="180x180" href="{{ url_for('static', filename='favicon/apple-touch-icon.png') }}" />
        <link rel="manifest" href="{{ url_for('static', filename='favicon/site.webmanifest') }}" />
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
        <link rel="icon" href="{{ url_for('static', filename='favicon/favicon.ico') }}" />
        <link rel="apple-touch-icon" href="{{ url_for('static', filename='favicon/apple-touch-icon.png') }}" />
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
    
