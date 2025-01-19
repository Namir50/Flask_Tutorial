from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    name = "Namir"
    l1 = ["Namir","Ibaad","Armaan"]
    return render_template('index.html',name = name,l1 = l1)
    
@app.route("/friend")
def friend():
    return "This is friends page"

@app.route("/friends/<name>")
def friends(name):
    return render_template('index2.html',name = name)

if __name__ == '__main__':
    app.run(debug=True)
    