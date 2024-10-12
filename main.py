from flask import Flask, render_template

app = Flask(__name__)

CONTACT = "+380677843232"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html', contact=CONTACT)

if __name__ == '__main__':
    app.run(debug=True)
