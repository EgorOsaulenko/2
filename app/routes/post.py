from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db.models.post import Post
from app.db import Session
from app.data.password import ADMIN_PASS

post_route = Blueprint("posts", __name__)

@post_route.route("/", methods=["GET", "POST"])
def add_post():
    with Session() as session:
        if request.method == "POST":
            title = request.form.get("title")
            text = request.form.get("text")
            user_id = request.form.get("user_id")
            if request.form.get("password") == ADMIN_PASS:
                post = Post(title=title, text=text, user_id=user_id)
                session.add(post)
                session.commit()
                flash("Статтю успішно додано")
            else:
                flash("Невірний пароль. Доступ заблоковано")
    return render_template("add_post.html")
