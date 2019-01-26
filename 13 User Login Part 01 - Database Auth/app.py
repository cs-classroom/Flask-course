from flask import Flask, session, render_template, request, redirect
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.csclassroom

app = Flask(__name__)
app.secret_key = "dwhdiu2h2903e"


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/<string:name>")
def hello(name):
    flag = 0
    return render_template("hello.html",**locals())


@app.route("/movies", methods=['POST','GET'])
def movies():
    if request.method=='POST':
        movie_name = request.form['movie_name']
        movie_record = db.movies.find_one({'name': movie_name})
        if movie_record is None:
            print("Error")
            return "Error"
        movie_rating = movie_record['rating']
        return str(movie_rating)
    elif request.method=='GET':
        return render_template("movies.html", **locals())


@app.route("/register", methods=['POST','GET'])
def register():
    if request.method=='GET':
        return render_template('register.html',**locals())
    else:
        record = request.form
        found = db.users.find_one({'username': record['username']})
        if found is not None:
            return redirect('/register')
        db.users.insert_one(dict(record))
        for item in db.users.find():
            print(item)
        return "data recieved"


@app.route("/login", methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html',**locals())
    else:
        record = request.form
        found = db.users.find_one({'username': record['username']})
        if found is None:
            return "Error"
        if found['password']!= record['password']:
            return "error password"
        return ""

if __name__ == "__main__":
    app.run()
