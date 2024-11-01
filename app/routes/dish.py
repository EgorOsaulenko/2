from flask import Blueprint, render_template, request, redirect
from app.db.models.dish import Dish
from app.db import Session

dish_route = Blueprint("dishes", __name__, url_prefix="/dishes")

@dish_route.route("/add", methods=["GET", "POST"])
def add_dish():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        price = request.form.get("price")
        with Session() as session:
            dish = Dish(name=name, description=description, price=price)
            session.add(dish)
            session.commit()
        return redirect("/dishes")
    return render_template("add_dish.html")
