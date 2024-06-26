from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)


@app.route("/")
def hello_world():
    return "<p>Hallo haiii :3</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
