from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/calculation")
def calculation():
    return render_template("calculation.html")


@app.route("/names")
def home():
    names = ["Jonas", "Antanas", "Petras"]
    return render_template("names.html", names=names)


@app.route("/say_hello/<name>")
def user(name):
    return {"name": name}


# from flask import Flask, request, render_template

# app = Flask(__name__)


@app.route("/login", methods=["GET", "POST"])
def login():
    print(request.form)
    if request.method == "POST":
        vardas = request.form["vardas"]
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run()
