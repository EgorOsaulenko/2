from flask import Blueprint, render_template, request
from app.db.models.user import User
from app.db import Session
from app.data.password import ADMIN_PASS

user_route = Blueprint("users", __name__, url_prefix="/users")

@user_route.route("/", methods=["GET", "POST"])
def add_user():
    msg = ""
    block = False
    with Session() as session:
        if request.method == "POST":
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            age = request.form.get("age")
            position_id = request.form.get("position_id")
            user = User(first_name=first_name, last_name=last_name, age=age, position_id=position_id)
            if request.form.get("password") == ADMIN_PASS:
                session.add(user)
                session.commit()
                msg = "Користувача успішно додано"
            else:
                block = True
    return render_template("add_user.html", msg=msg, block=block)
