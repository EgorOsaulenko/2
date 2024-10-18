from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzeria.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizzas = Pizza.query.all() 
    return render_template('menu.html', pizzas=pizzas)

@app.route('/add', methods=['GET', 'POST'])
def add_pizza():
    if request.method == 'POST':
        name = request.form['name']
        ingredients = request.form['ingredients']
        price = float(request.form['price'])

        new_pizza = Pizza(name=name, ingredients=ingredients, price=price)
        db.session.add(new_pizza)
        db.session.commit()
        return redirect(url_for('menu'))

    return render_template('add_pizza.html')

if __name__ == '__main__':
    app.run(debug=True)