from flask import Flask, render_template
app = Flask (__name__)

@app.route('/test')
def hello_world():
  return "hello that"

@app.route('/')
def main():
  return render_template('main.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')