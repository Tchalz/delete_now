from Flask import Flask, render_template

server = Flask(__name__)


@server.route("/")
def home():
    return render_template("data.html")


if __name__ == "__main__":
    server.run()
