from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Esse é o comando que diz ao Python para mostrar o seu site
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)