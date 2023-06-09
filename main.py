from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<html><body><h2>Hello World!</h2></body></html>"

@app.route("/<name>")
def hello(name):
    return f"<html><body><h2>Hello {name}!</h2></body></html>"
app.run()