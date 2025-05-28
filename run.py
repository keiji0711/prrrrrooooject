from flask import Flask
from routes.instructor import bp as instructor



app = Flask(__name__)


app.register_blueprint(instructor)

if __name__ == "__main__":
    app.run(debug = True)
