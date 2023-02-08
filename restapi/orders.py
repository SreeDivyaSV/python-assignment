from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
import os

app = Flask(__name__)


# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Dhanya2001*@localhost/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize db
db = SQLAlchemy(app)
app.app_context().push()
ma = Marshmallow(app)
class orders(db.Model):

    OrderID = db.Column(db.Integer,primary_key=True)
    CustomerID = db.Column(db.String(100))
    EmployeeID = db.Column(db.Integer)
    OrderDate = db.Column(db.String(100))
    RequiredDate = db.Column(db.String(100))
    ShippedDate = db.Column(db.String(100))
    ShipVia = db.Column(db.Integer)
    Freight = db.Column(db.Float)
    ShipName = db.Column(db.String(100))
    ShipAddress = db.Column(db.String(100))
    ShipCity = db.Column(db.String(100))
    ShipRegion = db.Column(db.String(100))
    ShipPostalCode = db.Column(db.String(100))
    ShipCountry = db.Column(db.String(100))

    def __init__(self,OrderID,CustomerID,EmployeeID,OrderDate,RequiredDate,ShippedDate,ShipVia,Freight,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.EmployeeID = EmployeeID
        self.OrderDate = OrderDate
        self.RequiredDate = RequiredDate
        self.ShippedDate = ShippedDate
        self.ShipVia = ShipVia
        self.Freight = Freight
        self.ShipName = ShipName
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipRegion = ShipRegion
        self.ShipPostalCode = ShipPostalCode
        self.ShipCountry = ShipCountry

class OrdersSchema(ma.Schema):

    class Meta:

      fields = ('OrderID','CustomerID','EmployeeID','OrderDate','RequiredDate','ShippedDate','ShipVia','Freight','ShipName','ShipAddress','ShipCity','ShipRegion','ShipPostalCode','ShipCountry')

Order_schema = OrdersSchema()
Orders_schema = OrdersSchema(many=True)

@app.route('/order', methods=['POST'])
def add_order():
    OrderID = request.json['OrderID']
    CustomerID = request.json['CustomerID']
    EmployeeID = request.json['EmployeeID']
    OrderDate = request.json['OrderDate']
    RequiredDate = request.json['RequiredDate']
    ShippedDate = request.json['ShippedDate']
    ShipVia = request.json['ShipVia']
    Freight = request.json['Freight']
    ShipName = request.json['ShipName']
    ShipAddress = request.json['ShipAddress']
    ShipCity = request.json['ShipCity']
    ShipRegion = request.json['ShipRegion']
    ShipPostalCode = request.json['ShipPostalCode']
    ShipCountry = request.json['ShipCountry']

    new_order = orders(OrderID,CustomerID,EmployeeID,OrderDate,RequiredDate,ShippedDate,ShipVia,Freight,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry)
    db.session.add(new_order)
    db.session.commit()

    return Order_schema.jsonify(new_order)

@app.route('/order', methods=['GET'])
def get_orders():
  all_orders = orders.query.all()
  result = Orders_schema.dump(all_orders)
  return jsonify(result)

@app.route('/order/<OrderID>', methods=['GET'])
def get_order(OrderID):
  order = orders.query.get(OrderID)
  return Order_schema.jsonify(order)

@app.route('/order/<OrderID>', methods=['PUT'])
def update_customer(OrderID):
  order = orders.query.get(OrderID)
  OrderID = request.json['OrderID']
  CustomerID = request.json['CustomerID']
  EmployeeID = request.json['EmployeeID']
  OrderDate = request.json['OrderDate']
  RequiredDate = request.json['RequiredDate']
  ShippedDate = request.json['ShippedDate']
  ShipVia = request.json['ShipVia']
  Freight = request.json['Freight']
  ShipName = request.json['ShipName']
  ShipAddress = request.json['ShipAddress']
  ShipCity = request.json['ShipCity']
  ShipRegion = request.json['ShipRegion']
  ShipPostalCode = request.json['ShipPostalCode']
  ShipCountry = request.json['ShipCountry']

  order.OrderID = OrderID
  order.CustomerID = CustomerID
  order.EmployeeID = EmployeeID
  order.OrderDate = OrderDate
  order.RequiredDate = RequiredDate
  order.ShippedDate = ShippedDate
  order.ShipVia = ShipVia
  order.Freight = Freight
  order.ShipName = ShipName
  order.ShipAddress = ShipAddress
  order.ShipCity = ShipCity
  order.ShipRegion = ShipRegion
  order.ShipPostalCode = ShipPostalCode
  order.ShipCountry = ShipCountry

  db.session.commit()

  return Order_schema.jsonify(order)
@app.route('/orderfilter/<CustomerID>', methods=['GET'])
def get_orderhistory(CustomerID):
    order = orders.query.filter_by(CustomerID = CustomerID)
    return Orders_schema.jsonify(order)
if __name__ == '__main__':
    app.run(port=5002)