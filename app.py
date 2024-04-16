from flask import Flask,  request, render_template,flash, redirect

app = Flask(__name__)
app.secret_key="Kobata"

@app.route("/")
def index():
    return render_template("index.html")






if __name__ == "__main__":
    app.run(debug=True)