from main15 import db, Message, app
from flask import request, render_template


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        email_check = Message.query.filter_by(email=email).first()
        if email_check:
            return render_template("login.html", email_taken=True)
        else:
            query = Message(name, email, message)
            db.session.add(query)
            db.session.commit()
            return render_template("greetings.html", vardas=name)
    elif request.method == "GET":
        return render_template("login.html", email_taken=False)


@app.route("/all", methods=["GET"])
def get_all():
    messages = Message.query.all()
    return render_template("all.html", messages=messages)


@app.route("/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        email = request.form["email"]
        message = Message.query.filter_by(email=email).first()
        db.session.delete(message)
        db.session.commit()
    all_messages = Message.query.all()
    return render_template("delete.html", users=all_messages)


if __name__ == "__main__":
    app.run(debug=True)
