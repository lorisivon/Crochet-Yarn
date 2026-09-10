from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Crochet Yarn!</h1><p>Our crochet shop website is coming soon.</p>"

if __name__ == "__main__":
    app.run(debug=True)
