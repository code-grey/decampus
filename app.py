# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return 'decampus'


# # if __name__ == '__main__':
# app.run(host='0.0.0.0', port=81, debug=True)


from flask import Flask
from models import User, Book  # Import your models once they're defined
# from routes import *  # Import all routes from the routes file

app = Flask(__name__)

# Import other modules here

if __name__ == "__app__":
    app.run(host='0.0.0.0', port=81, debug=True)
from routes import *  # Import all routes from the routes file


