from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def default():
    try:
        code = int(request.headers['X-Code'])
        return render_template(f"{code}.html"), code
    except Exception:
        return render_template("404.html"), 404
