from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "<h1>Co</h1>"

def run():
  app.run(host='0.0.0.0',port=8080)

def forever():  
    t = Thread(target=run)
