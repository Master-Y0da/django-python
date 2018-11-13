from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    return render_template('hrllo.html',name=name)

@app.route('/chango')
def chango():
    return 'changolandia!'

if __name__ == "__main__":
    app.debug = True
    app.run()