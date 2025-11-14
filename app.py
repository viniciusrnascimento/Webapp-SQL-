from flask import Flask, render_template
from db import get_date_from_db

app = Flask(__name__)

@app.route("/")
def home():
    data = get_date_from_db()
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()
