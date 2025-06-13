from flask import Flask
from routes.instructor import bp as instructor
from routes.admin import bp as admin

app = Flask(__name__)

app.register_blueprint(instructor)
app.register_blueprint(admin)

if __name__ == "__main__":
    app.run(debug = True)
