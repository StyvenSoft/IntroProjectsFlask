from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def index():
    framework= "Flask"
    return render_template("index.html", framework=framework)

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    return render_template("contact.html", name=name)

@app.route("/welcome/<string:name>")
def welcome(name):
    return f"""
    <h1>Welcome {name}</h1>
    """

@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
    return f'''
    <h2>Reporter {reporter_id} Bio</h2>
    <a href="/">Return to home page</a>
    '''

if __name__ == "__main__":
    app.run(debug=True)