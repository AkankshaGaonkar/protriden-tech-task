from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    if (request.method == 'POST'):
        email = request.form['email']
        password = request.form['password']
        return render_template("/home")
    return render_template("index.html")

@app.route("/register", methods=['POST'])
def verify():
    messsge = ""
    if (request.method == 'POST'):
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirmPassword']
        if password == confirmPassword:
            messsge = "You successfully registered"
        return redirect("/")
    return render_template("register.html")

@app.route("/home")
def welcome():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)