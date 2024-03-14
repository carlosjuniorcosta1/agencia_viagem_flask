from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from sqlalchemy import ForeignKey
from datetime import datetime
from enum import Enum
from flask import jsonify

class Package(db.Model):
    __tablename__ = "packages_table"
    package_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    client_id = db.Column(db.Integer, ForeignKey('clients_table.client_id'), nullable=False)
    origin = db.Column(db.String(150), nullable=False)
    destination = db.Column(db.String(150), nullable=False)
    departure_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    registration_date = db.Column(db.Date)
    price = db.Column(db.Float, nullable=True)
    meals = db.Column(db.String(10), nullable= True)
    accommodation = db.Column(db.Boolean, nullable = True)

    def __init__(self, client_id, origin, destination, departure_date, 
                 return_date, price, meals, accomodation):
        self.client_id = client_id
        self.origin = origin
        self.destination = destination
        self.departure_date = self.fill_dates(departure_date)
        self.return_date = self.fill_dates(return_date)
        self.registration_date = datetime.now().date()
        self.price = price
        self.meals = meals
        self.accommodation = accomodation

        self.validate_return_date()
    
    def fill_dates(self, date_dd_mm_yyyy):
        day, month, year = map(int, date_dd_mm_yyyy.split('/'))
        form_date = datetime(year, month, day)
        return form_date
     
    def validate_return_date(self):
        if self.return_date < self.departure_date:
            raise ValueError("The return date must be after the departure date") 
        elif self.return_date > self.departure_date:
            return self.return_date         
      
    
    def valid_meals(self, meals):
        if not self.meals:
            return "nao"  
        if self.meals:
            valid_meals = {"C", "A", "J", "ALL"}
            meal_set = set(meals.split(','))
            if "ALL" in meal_set:
                print("verdadeiro")
                return "ALL"
            else:
                meal_list = list(meal_set)
                meal_list.sort()
                if set(meal_list).issubset(valid_meals): 
                    return meal_list
  
    def to_json(self):
        return {
            "package_id": self.package_id,
            "client_id": self.client_id,
            "destination": self.destination,
            "departure_date": self.departure_date.strftime("%d/%m/%Y") if self.departure_date is not None else None,
            "return_date": self.return_date.strftime("%d/%m/%Y") if self.return_date is not None else None, 
            "registration_date": self.registration_date.strftime("%d/%m/%Y") if self.registration_date is not None else None,
            "price": self.price,
            "meals": self.meals if self.meals is not None else None,
            "accomodation": self.accommodation if self.accommodation is not None else None
        }

    def __repr__(self):
        return f"Pacote {self.package_id}, origem {self.origin}, destino {self.destination}, preço {self.price}"





