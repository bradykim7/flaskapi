from flask import Flask
from setproctitle import setproctitle
from routes import crawl

app = Flask(__name__)
setproctitle("flaskapi")


app.register_blueprint(crawl.routes)

if __name__ == "__main__":
    app.run(debug=True)
