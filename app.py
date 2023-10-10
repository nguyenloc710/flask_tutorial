from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from os import path

app = Flask(__name__)
app.config["SECRET_KEY"] = "locdz"
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///user.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.permanent_session_lifetime = timedelta(minutes=10)

db = SQLAlchemy(app)


class Use(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __int__(self, name, email):
        self.name = name
        self.email = email


@app.route('/home')
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/user')
def user():
    if "user" in session:
        name = session["user"]
        return render_template("user.html", user=user)
    flash("You not login", "info")
    return redirect(url_for("login"))


@app.route('/blog/<int:blog_id>')
def blog(blog_id):
    return f"<H2>Block {blog_id}<H2>"


@app.route('/admin')
def hello_admin():
    return f"<H2>Hello Admin<H2>"


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user_name = request.form["name"]
        session.permanent = True
        if user_name:
            session["user"] = user_name
            flash("You logged in successfully!", "info")
            return redirect(url_for('user', user=user_name))
    if "user" in session:
        name = session["user"]
        flash("You logged in!", "info")
        return redirect(url_for('user', user=name))

    return render_template("login.html")


@app.route('/logout')
def log_out():
    flash("You log out!", "info")
    session.pop("user", None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    if not path.exists("user.db"):
        db.create_all(app=app)
        print("Created database")
    app.run(debug=True)
