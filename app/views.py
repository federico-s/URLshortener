from flask import flash

from app import app, db
from flask import render_template, request, session, redirect

from app.models.loginForm import loginForm
from app.models.registerForm import registerForm
from app.models.urlForm import urlForm
from app.models.url import Url
from app.models.user import User

@app.route("/")
@app.route("/index")
def home():
    if 'username' in session:
        return redirect("/shorten")
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = loginForm(request.form)
    if request.method == "POST":
        if form.validate():
            usrnm = form.username.data
            pwd = User.hashPassword(form.password.data)

            chk = User.query.filter_by(username=usrnm, password = pwd).first()
            if chk is not None:
                session["username"] = usrnm
                return redirect("/shorten")
        else:
            flash(form.errors, category='error')
        return redirect("/login")

    else:
        if 'username' in session:
            return redirect("/shorten")
        return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = registerForm(request.form)
    if request.method == "GET":
        if 'username' in session:
            return redirect("/")
        return render_template("register.html", form = form)
    else:
        if form.validate():
            user = User()
            user.name = form.name.data
            user.username = form.username.data
            user.password = User.hashPassword(form.password.data)
            user.email = form.email.data

            db.session.add(user)
            db.session.commit()
        else:
            flash(form.errors, category='error')
            return redirect("/register")
        return redirect("/login")


@app.route("/shorten", methods=["GET", "POST"])
def shorten():
    form = urlForm(request.form)
    if request.method == "GET":
        author_url = Url.query.join(User).add_columns(Url.short_url, Url.long_url, User.id, User.username).filter(User.id==Url.author).all()
        author_url = author_url[::-1]
        return render_template("shorten.html", form = form, urls = author_url)
    else:
        if form.validate():
            url = Url()
            url.long_url = Url.addProtocol(form.long_url.data)
            url.code = Url.code_generator()
            url.short_url = request.url_root+url.code
            url.author = User.query.filter_by(username=session['username']).first().id

            db.session.add(url)
            db.session.commit()
            flash({"message": "URL successfully shortened!"},category='message')
        else:
            flash(form.errors, category='error')
        return redirect("/shorten")

@app.route("/init")
def init_db():
    db.create_all()
    return "DB creato"


@app.route("/<str>")
def gotolink(str):
    if str != '':
        print(str)
        url = Url.query.filter_by(code=str).first()
        if url is not None:
            return redirect(url.long_url)
        else:
            return error(None)
    else:
        redirect("/index")

@app.errorhandler(404)
def error(e):
    return "404"