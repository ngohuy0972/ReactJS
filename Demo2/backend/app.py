from flask import Flask, jsonify, request
import os
import BusinessObjects as bo 
import DataObjects as do

app = Flask(__name__)

db_ip = os.getenv('db_ip') #'10.0.2.15'
ConnectionData = {}
ConnectionData['user'] = 'postgres'
ConnectionData['password'] = 'postgres'
ConnectionData['host'] = str(db_ip)
ConnectionData['port'] = '5432'
ConnectionData['database'] = 'northwind'

@app.route('/')
def hello():    
    return 'this is backend'

@app.route('/customer/all')
def get_all_customer():
    c = do.Customer(ConnectionData)
    result = c.get_all()
    return jsonify({
        'data': result
    })

@app.route('/insert_customer', methods=['POST'])
def insert_customer():
    data = request.json
    customer = CustomerEntity(CustomerName=data['CustomerName'],
                                ContactName=data['ContactName'],
                                Address=data['Address'],
                                City=data['City'],
                                PostalCode=data['PostalCode'],
                                Country=data['Country'])
    c = Customer(connection_data)
    message = c.insert(customer)
    if message is None:
        return jsonify({
            'message': 'Cannot insert data'
        }), 500
    return jsonify({
        'message': message
    })

@app.route('/customer/<int:id>', methods=['DELETE', 'PUT'])
def delete_customer_by_id(id):
    if request.method == 'DELETE':
        # Delete user by id
        customer = CustomerEntity(CustomerID=id)
        c = Customer(ConnectionData)
        result = c.delete_customer_by_id(customer)
        return jsonify({
            'message': result[0]
        }), result[1]
    else:
        # Update user by id
        data = request.json
        customer = CustomerEntity(CustomerID=id,
                                    CustomerName=data['CustomerName'],
                                    ContactName=data['ContactName'],
                                    Address=data['Address'],
                                    City=data['City'],
                                    PostalCode=data['PostalCode'],
                                    Country=data['Country'])
        c = Customer(ConnectionData)
        result = c.update_customer(customer)
        return jsonify({
            'message': result[0]
        }), result[1]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)