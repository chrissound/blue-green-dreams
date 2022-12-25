from flask import Flask
import datetime

def create_app():
    """
    Create a Flask Good Weather application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__)

    @app.route('/')
    def index():
        """
        Render a Hello World response.

        :return: Flask response
        """
        return f"Hello World! + {datetime.datetime.now()}"

    return app
