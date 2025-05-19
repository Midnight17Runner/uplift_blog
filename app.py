from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def index():
    articles = os.listdir("templates/articles")
    articles = [a.replace(".html", "") for a in articles]
    return render_template("index.html", articles=articles)

@app.route("/article/<name>")
def article(name):
    try:
        return render_template(f"articles/{name}.html")
    except:
        return "Article not found", 404

import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
