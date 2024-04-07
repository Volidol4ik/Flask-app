from flask import Flask, render_template, request
import os
from OpenSSL import SSL


img = os.path.join('static', 'img')
app = Flask(__name__)

@app.route('/')
def start():
    return render_template("Home.html")


@app.route('/ppt/1411100.jpg')
def a():
    path = f'../static/img/{0}.png'
    return render_template("index.html", image = path)


@app.route('/амкодор/то18б0603000.jpg')
def b():
    path = f'../static/img/{1}.png'
    return render_template("index.html", image = path)


@app.route('/bondioli&pavesi/bm028703.jpg')
def c():
    path = f'../static/img/{2}.png'
    return render_template("index.html", image = path)


@app.route('/салео/a1562504.jpg')
def d():
    path = f'../static/img/{3}.png'
    return render_template("index.html", image = path)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')