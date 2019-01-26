from flask import Flask, session, render_template

app = Flask(__name__)
app.secret_key = "dwhdiu2h2903e"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<string:name>")
def hello(name):
    flag = 0
    return render_template("hello.html",**locals())


if __name__ == "__main__":
    app.run()
