from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html", name="himzei")

@app.route("/search") 
def search():
    return render_template("search.html")



if __name__ == '__main__':
    app.run()