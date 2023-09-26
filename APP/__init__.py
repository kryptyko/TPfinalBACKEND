from flask import Flask
from config import Config
from .routes.chat_bp import chat_bp
#from .routes.chat_bp import actor_bp
from flask_cors import CORS
def inicializar_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    CORS(app, origins='http://127.0.0.1:5500')
    app.config.from_object(Config)
    app.register_blueprint(chat_bp)
 #   app.register_blueprint(actor_bp)
    return app