import flask
from flask import redirect
from . import account


@account.route("/prinz")
def prinz():
    return flask.render_template("prinz.html")


@account.route("/install")
def install():
    return flask.render_template("install.html")


@account.route("/chrome")
def chrome():
    return redirect("https://chrome.google.com/webstore/detail/zeeguu/ckncjmaednfephhbpeookmknhmjjodcd?hl=en", code=302)



