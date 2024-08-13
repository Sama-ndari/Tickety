from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vafankuloTiquetX1425536377237272'

Bootstrap(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template('register.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
