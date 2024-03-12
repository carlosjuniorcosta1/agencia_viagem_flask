from flask import Flask
from config.config import Config, db
from models.client import Client
from models.package import Package
from models.user import User
from blueprints.client_dir.client_bp import clients_bp
from flask_migrate import Migrate 


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(clients_bp)

Migrate(app, db)
if __name__ == "__main__":
    pacote1 = Package(1, 'Rio de Janeiro', "Belo Horizonte", "02/02/2024", "12/03/2024", 1200, "C,A,J")
    # cliente1 = Client('Gustavo', 'gustavo@gmail.com')
    with app.app_context():
        db.session.add(pacote1)
        db.session.commit()       
    app.run()





