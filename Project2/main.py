from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Prevents warning

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

# 🟢 CREATE & READ Users
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        if name and password:
            new_user = User(name=name)
            new_user.set_password(password)  # Hash password
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('home'))  # Avoid resubmission on refresh

    users = User.query.all()  # Retrieve all users from database
    return render_template('index.html', users=users)

# 🔵 FRIENDS PAGE
@app.route("/friends")
def friends():
    return render_template('index2.html')

# 🔴 ABOUT PAGE
@app.route('/about', methods=['GET', 'POST'])
def about():
    name, password = None, None
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

    return render_template('index3.html', name=name, password="(hidden for security)")

if __name__ == '__main__':
    with app.app_context():  # ✅ Creates the application context
        db.create_all()  # ✅ Ensures database tables are created

    app.run(debug=True)
