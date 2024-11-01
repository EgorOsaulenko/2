from flask import Blueprint, render_template, request, redirect
from app.db.models.base import Session
from app.db.models.dish import Dish
from app.db.models.ingredient import Ingredient
from app.data.wheather import get_wheather

pizza_route = Blueprint("pizzas", __name__)

