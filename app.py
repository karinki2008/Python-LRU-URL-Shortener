import random
import string
from flask import Flask, render_template,request,redirect,url_for
from database import save_url, get_url, code_exists,get_all_urls
from url_service import shorten_url,get_original_url
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/shorten", methods=["POST"])
def shorten():

    original_url = request.form.get("original_url")

    if not original_url:
        return render_template(
            "index.html",
            error="Please enter a URL!"
        )

    code, suspicious = shorten_url(original_url)

    if code is None:
        return render_template(
            "index.html",
            error="Please enter a valid URL starting with http:// or https://"
        )

    short_url = url_for(
        "redirect_url",
        code=code,
        _external=True
    )

    return render_template(
        "index.html",
        short_url=short_url,
        suspicious=suspicious
    )

@app.route("/<code>")
def redirect_url(code):

    original_url = get_original_url(code)

    if original_url is None:
        return "Short URL not found!", 404

    return render_template(
        "preview.html",
        original_url=original_url
    )

@app.route("/history")
def history():
    urls = get_all_urls()

    return render_template(
        "history.html",
        urls=urls
    )

if __name__ == "__main__":
    app.run(debug=True)