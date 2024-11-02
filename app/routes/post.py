from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.db import Session
from app.db.models import User, Post
from app.data.password import ADMIN_PASS

post_route = Blueprint("posts", __name__)

@post_route.route("/posts/", methods=["GET", "POST"])
def add_post():
    with Session() as session:
        users = session.query(User).all() 

        if request.method == "POST":
            title = request.form.get("title")
            text = request.form.get("text")
            user_id = request.form.get("user_id")
            password = request.form.get("password")

            if password == ADMIN_PASS:
                post = Post(title=title, text=text, user_id=user_id)
                session.add(post)
                session.commit()
                flash("Статтю успішно додано")
                return redirect(url_for("posts.index"))
            else:
                flash("Невірний пароль. Доступ заблоковано")

    return render_template("add_post.html", users=users)
