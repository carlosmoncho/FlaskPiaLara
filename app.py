from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template('login.html')

@app.route("/users",  methods = ["GET", "POST"])
def users():
    # if request.method == 'POST':
    #    password = request.form.get("password")
    #    user = request.form.get("user")
    return render_template('users.html')


@app.route("/frases")
def frases():
    return render_template('frases.html')

@app.route("/sesion")
def sesion():
    return render_template('sesion.html')

@app.route("/sesiones")
def sesiones():
    return render_template('sesiones.html')

if __name__ == '__main__':
    app.run(debug = True)