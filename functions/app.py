import os
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola desde Flask en Netlify!'

def handler(event, context):
    # Aquí usas la función Flask dentro de un "handler" para Netlify
    return app(event, context)
