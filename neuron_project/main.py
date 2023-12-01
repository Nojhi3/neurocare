from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new_data.db'
db = SQLAlchemy()
db.init_app(app)


class Userdata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/home')
def main_page():
    return render_template("main.html")


@app.route('/parent')
def parent_page():
    return render_template("parent.html")


@app.route('/teachers-intro')
def teacher_intro():
    return render_template("teachers-intro.html")


@app.route('/parents-intro')
def parent_intro():
    return render_template("parents-intro.html")


@app.route('/autism')
def autism_page():
    return render_template("autism.html")


@app.route('/adhd')
def adhd_page():
    return render_template("adhd.html")


@app.route('/login-parent', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return redirect(url_for('parent_intro'))
    return render_template("index.html")


@app.route('/login-teacher', methods=['GET', 'POST'])
def index2():
    if request.method == "POST":
        return redirect(url_for('teacher_intro'))
    return render_template("index2.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":

        email = request.form.get('email')
        result = db.session.execute(db.select(Userdata).where(Userdata.email == email))
        user = result.scalar()
        if user:
            flash("You've already signed up with that email, log in instead!")
            time.sleep(5)
            return redirect(url_for('index'))

        new_user = Userdata(
            email=request.form.get('email'),
            password=request.form.get('password'),
            username=request.form.get('username'),
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("read_instructions"))
    return render_template("register.html")


@app.route('/instructions')
def read_instructions():
    return render_template("instruction.html")


@app.route("/activity/1", methods=['POST', 'GET'])
def get_activity1():
    return render_template("activity1.html")


@app.route("/activity/2", methods=['POST', 'GET'])
def get_activity2():
    return render_template("activity2.html")


@app.route("/activity/3", methods=['POST', 'GET'])
def get_activity3():
    return render_template("activity3.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
