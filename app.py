from flask import Flask
from config.config import Config, db
from models.client import Client
from models.package import Package
from models.user import User
from blueprints.client_dir.client_crud_bp import clients_bp
from blueprints.client_dir.client_filter_bp import clients_filter_bp
from flask_migrate import Migrate 

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(clients_bp)
app.register_blueprint(clients_filter_bp)

Migrate(app, db)
if __name__ == "__main__":

        
    app.run()





