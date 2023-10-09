from flask_cors import CORS
from api import app, db

from api.api import api_bp

from model.api import init_api

app.register_blueprint(api_bp)

@app.before_first_request
def init_db():
    with app.app_context():
        db.create_all()
        
        init_api()

if __name__ == "__main__":
    cors = CORS(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./volumes/sqlite.db"
    app.run(debug=True, host="0.0.0.0", port="8199")