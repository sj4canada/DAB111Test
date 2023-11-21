from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<center><font face=\"Shruti\"><h1>હેલો, ફ્લાસ્ક!</h1></font></center>"

@app.route("/about")
def about():
    return "<center><font face=\"Calibri\"><h1>This is about page</h1></font></center>"

if __name__ == "__main__":
    app.run(debug=True)