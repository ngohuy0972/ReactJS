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

#ConnectionString = 'database=northwind user=postgres password=postgres host=10.0.2.15 port=5432'

@app.route('/')
def hello():    
    #return 'this is backend'
    c1 = bo.Customers(1, 'XinChao', 'Peter', '566 Nui Thanh', 'Danang', '50000', 'Vietnam')
    return c1.CustomerName

# CUSTOMERS SECTION
#insert customer
@app.route('/customer_insert')
def test_insert():
    c2 = do.Customers(ConnectionData)
    c1 = bo.Customers(1, 'Van Huy', 'Ngo', 'K7/2A Pasteur', 'Danang', '50000', 'Vietnam')
    s1 = c2.insert(c1)
    return s1

#Show all Customers
@app.route('/customer/all_Customer')
def get_all_user():
    result = do.Customers(ConnectionData).get_all()
    return jsonify(result), 200

# Delete customer
@app.route('/customer/delete/<int:customer_id>' , methods=['DELETE'])
def delete_user_by_id(customer_id):
    c = bo.Customers(CustomerID = customer_id)
    result = do.Customers(ConnectionData).delete(c)
    return jsonify({'message': result[0]}),result[1]

#  Update customer
@app.route('/customer/update/<int:customer_id>' , methods=['PUT'])
def update_coustomer(customer_id):
    data = request.json
    c = bo.Customers(CustomerID =  customer_id , CustomerName=data['CustomerName'], ContactName=data['ContactName'], Address=data['Address'], City = data['City'],  PostalCode=data['PostalCode'], Country=data['Country'])
    result = do.Customers(ConnectionData).update(c)
    return jsonify({'message': result[0]}),result[1]
    
#Show customer by ID
@app.route('/customer/get/<int:user_id>')
def get_user_by_id(user_id):
    c = bo.Customers(CustomerID = user_id)
    result = do.Customers(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}) , result[0]
    return jsonify(result[0].to_json()) , 200


# CATEGORIES
# insert categories
@app.route('/categories_insert')
def test_insertca():
    c2 = do.Categories(ConnectionData)
    c1 = bo.Categories(1 , 'categories' , 'descriptions')
    s1 = c2.insert(c1)
    return s1

# get all categories
@app.route('/categories/all_Categories')
def get_all_ca():
    result = do.Categories(ConnectionData).get_all()
    return jsonify(result), 200

# get categories by ID
@app.route('/categories/get/<int:user_id>')
def get_ca_by_id(user_id):
    c = bo.Customers(CustomerID = user_id)
    result = do.Customers(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}) , result[0]
    return jsonify(result[0].to_json()) , 200

# EMPLOYEES
# insert employees
@app.route('/employee/insert', methods=['POST'])
def employee_insert():
    data = request.json
    c1 = bo.Employee(last_name=data['last_name'], first_name=data['first_name'], birth_date=data['birth_date'], photo=data['photo'], notes=data['notes'])
    c2 = do.Employee(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

# get all employees
@app.route('/employee/all')
def get_all_employee():
    result = do.Employee(ConnectionData).get_all()
    return jsonify(result), 200

# edit employees
@app.route('/employee/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_employee(employee_id):
    if request.method == 'GET':
        # Get an employee by ID
        c = bo.Employee(employee_id=employee_id)
        result = do.Employee(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update an employee
        data = request.json
        c = bo.Employee(employee_id=employee_id, last_name=data['last_name'], first_name=data['first_name'], birth_date=data['birth_date'], photo=data['photo'], notes=data['notes'])
        result = do.Employee(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete an employee
        c = bo.Employee(employee_id=employee_id)
        result = do.Employee(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]
    
#ORDER
# insert order 
@app.route('/order/insert', methods=['POST'])
def order_insert():
    data = request.json
    c1 = bo.Order(customer_id=data['customer_id'], employee_id=data['employee_id'], order_date=data['order_date'], shipper_id=data['shipper_id'])
    c2 = do.Order(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

# get all order
@app.route('/order/all')
def get_all_order():
    result = do.Order(ConnectionData).get_all()
    return jsonify(result), 200

# edit order
@app.route('/order/<int:order_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_order(order_id):
    if request.method == 'GET':
        # Get an order by ID
        c = bo.Order(order_id=order_id)
        result = do.Order(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update an order
        data = request.json
        c = bo.Order(order_id=order_id, customer_id=data['customer_id'], employee_id=data['employee_id'], order_date=data['order_date'], shipper_id=data['shipper_id'])
        result = do.Order(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete an order
        c = bo.Order(order_id=order_id)
        result = do.Order(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]

# ORDER DETAIL
# insert order detail
@app.route('/order_detail/insert', methods=['POST'])
def order_detail_insert():
    data = request.json
    c1 = bo.OrderDetail(order_id=data['order_id'], product_id=data['product_id'], quantity=data['quantity'])
    c2 = do.OrderDetail(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

# get all order detail
@app.route('/order_detail/all')
def get_all_order_detail():
    result = do.OrderDetail(ConnectionData).get_all()
    return jsonify(result), 200

# edit order detail
@app.route('/order_detail/<int:order_detail_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_order_detail(order_detail_id):
    if request.method == 'GET':
        # Get an order detail
        c = bo.OrderDetail(order_detail_id=order_detail_id)
        result = do.OrderDetail(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update an order detail
        data = request.json
        c = bo.OrderDetail(order_detail_id=order_detail_id, order_id=data['order_id'], product_id=data['product_id'], quantity=data['quantity'])
        result = do.OrderDetail(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete an order detail
        c = bo.OrderDetail(order_detail_id=order_detail_id)
        result = do.OrderDetail(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]

# PRODUCTS:
# insert products
@app.route('/product/insert', methods=['POST'])
def product_insert():
    data = request.json
    c1 = bo.Products(product_name=data['product_name'], unit=data['Unit'], price=data['price'], supplier_id=data['supplier_id'], category_id=data['category_id'])
    c2 = do.Products(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

# get all products
@app.route('/product/all')
def get_all_product():
    result = do.Products(ConnectionData).get_all()
    return jsonify(result), 200

# edit products
@app.route('/product/<int:product_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_product(product_id):
    if request.method == 'GET':
        # Get a product by ID
        c = bo.Products(product_id=product_id)
        result = do.Products(ConnectionData).get_by_id(c)
        if result[1] != 200:
            return jsonify({'message': result[0]}), result[1]
        return jsonify(result[0].to_json()), 200
    elif request.method == 'PUT':
        # Update a product
        data = request.json
        c = bo.Products(product_id=product_id, product_name=data['product_name'], unit=data['unit'], price=data['price'], supplier_id=data['supplier_id'], category_id=data['category_id'])
        result = do.Products(ConnectionData).update(c)
        return jsonify({'message': result[0]}), result[1]
    elif request.method == 'DELETE':
        # Delete a product
        c = bo.Products(product_id=product_id)
        result = do.Products(ConnectionData).delete(c)
        return jsonify({'message': result[0]}), result[1]

# SHIPPERS
# insert shippers
@app.route('/shipper/insert', methods=['POST'])
def insert_shipper():
    data = request.json
    shipper = bo.Shippers(shipper_name=data['shipper_name'], phone=data['phone'])
    result = do.Shippers(ConnectionData).insert(shipper)
    return jsonify({'message': result}), 200

# get all shippers
@app.route('/shipper/all')
def get_all_shipper():
    c = do.Shippers(ConnectionData).get_all()
    return jsonify(c), 200

# get shippers by ID
@app.route('/shipper/get/<int:shipper_id>')
def get_shipper_by_id(shipper_id):
    shipper = bo.Shippers(shipper_id=shipper_id)
    result = do.Shippers(ConnectionData).get_by_id(shipper)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

# update shippers
@app.route('/shipper/update/<int:shipper_id>', methods=['PUT'])
def update_shipper_by_id(shipper_id):
    data = request.json
    shipper = bo.Shippers(shipper_id=shipper_id, shipper_name=data['shipper_name'], phone=data['phone'])
    result = do.Shippers(ConnectionData).update(shipper)
    return jsonify({'message': result[0]}), result[1]

# delete shippers
@app.route('/shipper/delete/<int:shipper_id>', methods=['DELETE'])
def delete_shipper_by_id(shipper_id):
    c = bo.Shipper(shipper_id=shipper_id)
    result = do.Shippers(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]

# SUPPLIERS
# insert suppliers
@app.route('/supplier/insert', methods=['POST'])
def supplier_insert():
    data = request.json
    c1 = bo.Suppliers(SupplierName=data['SupplierName'], ContactName=data['ContactName'], Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'], Phone=data['Phone'])
    c2 = do.Suppliers(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

# get all suppliers
@app.route('/supplier/all')
def get_all_supplier():
    result = do.Suppliers(ConnectionData).get_all()
    return jsonify(result), 200

# get suppliers by ID
@app.route('/supplier/get/<int:supplier_id>')
def get_supplier_by_id(supplier_id):
    c = bo.Suppliers(SupplierID=supplier_id)
    result = do.Suppliers(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

# update suppliers
@app.route('/supplier/update/<int:supplier_id>', methods=['PUT'])
def update_supplier_by_id(supplier_id):
    data = request.json
    c = bo.Suppliers(SupplierID=supplier_id, SupplierName=data['SupplierName'], ContactName=data['ContactName'], Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'], Phone=data['Phone'])
    result = do.Suppliers(ConnectionData).update(c)
    return jsonify({'message': result[0]}), result[1]

# delete suppliers
@app.route('/supplier/delete/<int:supplier_id>', methods=['DELETE'])
def delete_supplier_by_id(supplier_id):
    c = bo.Suppliers(SupplierID=supplier_id)
    result = do.Suppliers(ConnectionData).delete(c)
    return jsonify({'message': result[0]}), result[1]

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
    