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

# Initialize ma
ma = Marshmallow(app)

class customers(db.Model):
    CustomerID = db.Column(db.String(100), primary_key=True)
    CompanyName = db.Column(db.String(100), unique=True)
    ContactName = db.Column(db.String(200))
    ContactTitle = db.Column(db.String(100))
    Address = db.Column(db.String(100))
    City = db.Column(db.String(100))
    Region = db.Column(db.String(100))
    PostalCode = db.Column(db.String(100))
    Country = db.Column(db.String(100))
    Phone = db.Column(db.Integer)
    Fax = db.Column(db.String(100))

    def __init__(self, CustomerID,CompanyName,ContactName,ContactTitle,Address,City,Region,PostalCode,Country,Phone,Fax):
        self.CustomerID = CustomerID
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax
class CustomerSchema(ma.Schema):

    class Meta:

      fields = ('CustomerID', 'CompanyName', 'ContactName', 'ContactTitle', 'Address', 'City', 'Region', 'PostalCode', 'Country', 'Phone', 'Fax')

Customer_schema = CustomerSchema()
Customers_schema = CustomerSchema(many=True)

# Create a Product
@app.route('/customer', methods=['POST'])
def add_customer():
  CustomerID = request.json['CustomerID']
  CompanyName = request.json['CompanyName']
  ContactName = request.json['ContactName']
  ContactTitle = request.json['ContactTitle']
  Address = request.json['Address']
  City = request.json['City']
  Region = request.json['Region']
  PostalCode = request.json['PostalCode']
  Country = request.json['Country']
  Phone = request.json['Phone']
  Fax = request.json['Fax']


  new_customer = customers(CustomerID,CompanyName,ContactName,ContactTitle,Address,City,Region,PostalCode,Country,Phone,Fax)

  db.session.add(new_customer)
  db.session.commit()

  return Customer_schema.jsonify(new_customer)

  # Get All Products
@app.route('/customer', methods=['GET'])
def get_customers():
  all_customers = customers.query.all()
  result = Customers_schema.dump(all_customers)
  return jsonify(result)

  # Get Single Products
@app.route('/customer/<CustomerID>', methods=['GET'])
def get_customer(CustomerID):
  product = customers.query.get(CustomerID)
  return Customer_schema.jsonify(product)

# Update a Product
@app.route('/customer/<CustomerID>', methods=['PUT'])
def update_customer(CustomerID):
  customer = customers.query.get(CustomerID)

  CompanyName = request.json['CompanyName']
  ContactName = request.json['ContactName']
  ContactTitle = request.json['ContactTitle']
  Address = request.json['Address']
  City = request.json['City']
  Region = request.json['Region']
  PostalCode = request.json['PostalCode']
  Country = request.json['Country']
  Phone = request.json['Phone']
  Fax = request.json['Fax']

  customer.CompanyName = CompanyName
  customer.ContactName = ContactName
  customer.ContactTitle = ContactTitle
  customer.Address = Address
  customer.City = City
  customer.Region = Region
  customer.PostalCode = PostalCode
  customer.Country = Country
  customer.Phone = Phone
  customer.Fax = Fax


  

  db.session.commit()

  return Customer_schema.jsonify(customer)

#for products table
class ProductSchema(ma.Schema):

    class Meta:

      fields = ('ProductID','ProductName','SupplierID','CategoryID','QuantityPerUnit','UnitPrice','UnitsInStock','UnitsOnOrder','ReorderLevel','Discontinued')

Product_schema = ProductSchema()
Products_schema = ProductSchema(many=True)

if __name__ == '__main__':
    app.run(port=5000)