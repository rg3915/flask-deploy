from flask import Flask, render_template


app = Flask(__name__)
app.config["ENV"] = "production"


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
