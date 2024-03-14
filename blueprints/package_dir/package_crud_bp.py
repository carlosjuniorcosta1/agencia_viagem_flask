from models.package import Package 
from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from flask import Blueprint, request, jsonify
from datetime import datetime

package_crud_bp = Blueprint('package_crud_bp', __name__)

@package_crud_bp.route('/pacotes', methods= ["GET"])
def get_all_packages():
    packages = Package.query.all()
    packages_json = [x.to_json() for x in packages]
    print(packages)
    return jsonify(data=packages_json, message="All packages"), 200

@package_crud_bp.route('/pacote/<int:package_id>', methods=['GET'])
def get_package(package_id):
    package = Package.query.get(package_id)
    if not package:
        return(jsonify(message="Package not found")), 404
    package_json = package.to_json()
    return jsonify(data=package_json, message="Requested package"), 200

@package_crud_bp.route('/pacote', methods=["POST"])
def add_package():
    package_data = request.get_json()
    client_id = package_data.get('client_id')
    origin = package_data.get('origin')
    destination = package_data.get('destination')
    departure_date = package_data.get('departure_date')    
    return_date = package_data.get('return_date')
    price = package_data.get('price')
    meals = package_data.get('meals')
    accomodation = package_data.get('accomodation')
    mandatory_fields = ["client_id", "origin", "destination", "departure_date", "return_date", "accomodation"]
    missing_fields = [x for x in mandatory_fields if x not in package_data]
    if missing_fields:
        return jsonify(message=f"You should provide {", ".join(missing_fields)}")
    if return_date < departure_date:
        return jsonify(message="The return date must be after the departure date")
    if meals and meals not in ["A", "C", "J", "ALL"]:
        return jsonify(message="Invalid value for meals. It should be 'C' (breakfast), 'A', (lunch), 'J' (dinner) or 'ALL' (all inclusve)")
        
    new_package = Package(client_id=client_id, origin=origin, 
                          destination=destination, departure_date=departure_date,
                         return_date=return_date, price=price, meals=meals,
                         accomodation=accomodation)
    if new_package:
        db.session.add(new_package)
        db.session.commit()
        new_package_json = new_package.to_json()
        return jsonify(data=new_package_json, message="New package added"), 201

@package_crud_bp.route('/pacote', methods=["PUT"])
def update_package():
    data_package = request.get_json()
    if "package_id"  not in data_package:
        return jsonify(message="You must provide a package_id in order to update a package")
    else:
        package_id = data_package.get('package_id')
        updated_package = Package.query.get(package_id)
    for key, value in data_package.items():
        if key != "package_id" and key != "departure_date" and key != "return_date":
            setattr(updated_package, key, value)
    if "departure_date" or "return_date" in data_package:
        new_departure_date = data_package.get('departure_date')
        new_return_date = data_package.get('return_date')
        new_departure_date_form = datetime.strptime(new_departure_date, "%d/%m/%Y")
        new_return_date_form = datetime.strptime(new_return_date, "%d/%m/%Y")
        if new_return_date_form < new_departure_date_form:
            return jsonify(message="The return date must be after than the departure date "), 400
        updated_package.departure_date = new_departure_date_form.strftime('%Y/%m/%d')
        updated_package.return_date = new_return_date_form.strftime("%Y/%m/%d")      

    db.session.commit()
    return jsonify(message="Package updated successfully"), 200

@package_crud_bp.route('/pacote', methods= ["DELETE"])
def delete_package():
    data_package = request.get_json()
    if "package_id" not in data_package:
        return jsonify(message="You should provide a package_id to delete a package"), 400
    else:
        package_id = data_package.get('package_id')
    package_to_delete = Package.query.get(package_id)
    if not package_to_delete:
        return jsonify(message="Package not found"), 404
    else:
        package_to_delete_json = package_to_delete.to_json()
    db.session.delete(package_to_delete)
    db.session.commit()
    return jsonify(data = package_to_delete_json, message = "Package successfully deleted"), 200
     


    

    

    

    
    

    
        
        
    





