
from flask import Flask
from flask_cors import CORS
from controller.booking_controller import booking_bp
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(booking_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=os.getenv("FLASK_RUN_PORT", 5000))
