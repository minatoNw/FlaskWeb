from flask import Flask, Response, request
import requests
import hashlib

app = Flask(__name__)
salt = "UNIQUE_SALT"
default_name = "myname"


@app.route("/", methods=["GET", "POST"])
def main():
    name = default_name
    if request.method == "POST":
        name = request.form["name"]
        post = requests.get("http://172.100.0.3:8080/monster/")


    header = "<html><html><title>minato web </title></head><body>"
    body = """<form method="POST">
                Hello <input type="text" name="name" value="">
                <input type="submit" value="submit">
                </form>
                <p>You looks like a:
                <img src="/monster/
            """
    body += name + "/>"
    footer = "</body></html>"

    return header + body + footer


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
    