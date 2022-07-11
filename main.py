from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return 'Hello World! <h5>HELLO<h5>'

@app.route("/<name>")
def user(name):
    return f'Hello {name}'

@app.route('/admin')
def admin():
    return redirect(url_for("user", name = 'admin '))

if __name__ == '__main__':
    app.run()