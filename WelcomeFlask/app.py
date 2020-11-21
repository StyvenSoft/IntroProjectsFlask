from flask import Flask

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index():
    return "Welcome Flask!"

if __name__ == "__main__":
    app.run(debug=True)