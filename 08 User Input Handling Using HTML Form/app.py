from flask import Flask, session, render_template, request

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
        movies = {"Thor: Ragnarok": 7.9,"Wonder Woman": 7.5, "Logan": 8.1, "Despicable Me 3": 6.3}
        if movie_name in movies.keys():
            return str(movies[movie_name])
        else:
            return "ERRoR! Movie not found"
    elif request.method=='GET':
        return render_template("movies.html", **locals())


if __name__ == "__main__":
    app.run()
