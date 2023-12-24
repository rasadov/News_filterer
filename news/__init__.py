from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main_page():
    return "<h1>hello world!</h1>"