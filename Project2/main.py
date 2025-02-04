from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

class DBhandler(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    password = db.Column(db.Integer)
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/friends")
def friends():
    return render_template('index2.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
    return render_template('index3.html',name = name, password = password)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
