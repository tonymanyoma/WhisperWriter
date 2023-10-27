from flask import Flask
from flask_cors import CORS
from config import config

# Routes
from routes import WhisperRoutes

app = Flask(__name__)

CORS(app, resources={"*":{"origins":"http://localhost:8080"}})

def page_not_found(error):
    return "<h1>Not Found page</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    
    # Blueprints
    app.register_blueprint(WhisperRoutes.main, url_prefix='/api/whisper')
    
    # Error handler
    app.register_error_handler(404, page_not_found)
    app.run()