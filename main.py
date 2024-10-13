from flask import Flask, render_template

app = Flask(__name__)

pizzas = [
    {"name": "Пеппероні", "ingredients": "Тісто, томатний соус, моцарела та ковбаса пепероні", "price": 350},
    {"name": "Моцарела", "ingredients": "Томатний соус, сир моцарела, базилік", "price": 280},
    {"name": "4 сири", "ingredients": "Пармезан, Адигейський, Моцарела та Дорблю", "price": 320}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)