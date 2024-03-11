from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, jsonify, request
from config.config import db
from models.client import Client

clients_bp = Blueprint('clients_bp', __name__)

@clients_bp.route('/clientes', methods=["GET"])
def get_all_client():
    clients = Client.query.all()
    clients_js = [x.to_json() for x in clients]
    return jsonify(data=clients_js, message = "Todos os clientes")

@clients_bp.route('/cliente', methods = ["GET", "POST"])
def add_client():
    new_client = request.get_json()
    new_client_obj = Client.from_json(new_client)
    db.session.add(new_client)
    db.session.commit()
    return jsonify(data=new_client_obj.to_json(),message=f"{new_client_obj['name']} adicionado" )
    
    
    