# webappnorthwind
##connect server
ssh -p 4567 ubuntu@ip_of_real_machine

#docker 
https://docs.docker.com/v17.09/get-started/part2/#dockerfile
https://docs.docker.com/install/linux/docker-ce/ubuntu/

#backend
sudo docker build -t backend .
sudo docker run -d --name backend --env db_ip=10.0.2.15 -p 8080:8080 backend 

sudo docker run -d --name backend --env db_ip=172.17.0.1 -p 8080:8080 backend 
sudo docker stop backend
sudo docker rm backend 
sudo docker exec -it coredb bash

#deploy db
sudo docker load --input postgres_11.2-alpine.tar

sudo docker run -d --restart unless-stopped --name coredb -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -v ~/northwind_db:/var/lib/postgresql/data -p 5432:5432 postgres:11.2-alpine

#postgres
psql -U postgres
\l
create database xyz;
\c xyz;

# How to run

1. Stop and remove old container: ```docker stop flask-backend && docker rm flask-backend```
1. Build image: ```docker build -t backend .```
1. Run the container: ```docker run -d --name flask-backend -e password=postgres -p 5000:5000 backend```

# Entity
## Customer
* id: int
* customer_name: string
* contact_name: string
* address: string
* city: string
* postal_code: string
* country: string


# API
## Customer
### Get all customer
* Request
    * Method: GET
    * Endpoint: /customer/all
    * Params: None
    * Body: None
* Response: [Customer]
### Get customer by ID
* Request
    * Method: GET
    * Endpoint: /customer/get/<int:user_id>
* Response: Message
### Add a customer
* Request
    * Method: POST
    * Endpoint: /customer
    * Body:
        * customer_name: string
        * contact_name: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
* Response: Message
### Update a customer
* Request:
    * Method: PUT
    * Endpoint: /customer/:customer_id
    * Body:
        * customer_name: string
        * contact_name: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
* Response: Message

### Delete a customer
* Request:
    * Method: DELETE
    * Endpoint: /customer/:customer_id
* Response: message


# Entity
## Categories
* id: int
* categories_name: string
* description: string


## Categories
### Get all categories
* Request
    * Method: GET
    * Endpoint: /categories/all_Categories
    * Params: None
    * Body: None
* Response: [Categories]
### Add a categories
* Request
    * Method: POST
    * Endpoint: /categories_insert
    * Body:
        * catagories_name: string
        * description: string
* Response: Message
### Get categories by ID
* Request
    * Method: GET
    * Endpoint: /categories/get/<int:user_id>
* Response: Message


# Entity
## Employees
* id: int
* last_name: string
* first_name: string
* birthdate: date
* photo: string
* notes: string


## Employees
### Get all Employees
* Request
    * Method: GET
    * Endpoint: /employee/all
    * Params: None
    * Body: None
* Response: [Categories]
### Add a Employees
* Request
    * Method: POST
    * Endpoint: /employee/insert
    * Body:
        * last_name: string
        * first_name: string
        * birthdate: date
        * photo: string
        * notes: string
* Response: Message
### Get Employees by ID
* Request
    * Method: GET
    * Endpoint: /employee/<int:employee_id>
* Response: Message
### Update a employees
* Request:
    * Method: PUT
    * Endpoint: /employee/<int:employee_id>
    * Body:
        * last_name: string
        * first_name: string
        * birthdate: date
        * photo: string
        * notes: string
* Response: Message

### Delete a employees
* Request:
    * Method: DELETE
    * Endpoint: /employee/<int:employee_id>
* Response: message


# Entity
## Order
* id: int
* customer_id: int
* employee_id: int
* orderdate: date
* shipper_id: int


## Order
### Get all order
* Request
    * Method: GET
    * Endpoint: /order/all
    * Params: None
    * Body: None
* Response: [Order]
### Add a order
* Request
    * Method: POST
    * Endpoint: /order/insert
    * Body:
        * customer_id: int
        * employee_id: int
        * orderdate: date
        * shipper_id: int
* Response: Message
### Get Order by ID
* Request
    * Method: GET
    * Endpoint: /order/<int:order_id>
* Response: Message
### Update a order
* Request:
    * Method: PUT
    * Endpoint: /order/<int:order_id>
    * Body:
        * customer_id: int
        * employee_id: int
        * orderdate: date
        * shipper_id: int
* Response: Message

### Delete a order
* Request:
    * Method: DELETE
    * Endpoint: /order/<int:order_id>
* Response: message


# Entity
## Order detail
* id: int
* order_id: int
* product_id: int
* quantity: int


## Order detail
### Get all Order detail
* Request
    * Method: GET
    * Endpoint: /order_detail/all
    * Params: None
    * Body: None
* Response: [OrderDetail]
### Add a Order detail
* Request
    * Method: POST
    * Endpoint: /order_detail/insert
    * Body:
        * order_id: int
        * product_id: int
        * quantity: int
* Response: Message
### Get Order detail by ID
* Request
    * Method: GET
    * Endpoint: /order_detail/<int:order_detail_id>
* Response: Message
### Update a Order detail
* Request:
    * Method: PUT
    * Endpoint: /order_detail/<int:order_detail_id>
    * Body:
        * order_id: int
        * product_id: int
        * quantity: int
* Response: Message

### Delete a Order detail
* Request:
    * Method: DELETE
    * Endpoint: /order_detail/<int:order_detail_id>
* Response: message


# Entity
## Products
* id: int
* product_name: string
* suppliers_id: int
* categories_id: int
* unit: int
* price: int


## Products
### Get all Products
* Request
    * Method: GET
    * Endpoint: /product/all
    * Params: None
    * Body: None
* Response: [Products]
### Add a Products
* Request
    * Method: POST
    * Endpoint: /product/insert
    * Body:
        * product_name: string
        * suppliers_id: int
        * categories_id: int
        * unit: int
        * price: int
* Response: Message
### Get Products by ID
* Request
    * Method: GET
    * Endpoint: /product/<int:product_id>
* Response: Message
### Update a Products
* Request:
    * Method: PUT
    * Endpoint: /product/<int:product_id>
    * Body:
        * product_name: string
        * suppliers_id: int
        * categories_id: int
        * unit: int
        * price: int
* Response: Message

### Delete a Products
* Request:
    * Method: DELETE
    * Endpoint: /product/<int:product_id>
* Response: message


# Entity
## Suppliers
* id: int
* suppliers_name: string
* contact_name: string
* address: string
* city: string
* postal_code: string
* country: string
* phone: string


## Suppliers
### Get all Suppliers
* Request
    * Method: GET
    * Endpoint: /supplier/all
    * Params: None
    * Body: None
* Response: [Suppliers]
### Add a Suppliers
* Request
    * Method: POST
    * Endpoint: /supplier/insert
    * Body:
        * suppliers_name: string
        * contact_name: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
        * phone: string
* Response: Message
### Get Suppliers by ID
* Request
    * Method: GET
    * Endpoint: /supplier/get/<int:supplier_id>
* Response: Message
### Update a Suppliers
* Request:
    * Method: PUT
    * Endpoint: /supplier/update/<int:supplier_id>
    * Body:
        * suppliers_name: string
        * contact_name: string
        * address: string
        * city: string
        * postal_code: string
        * country: string
        * phone: string
* Response: Message

### Delete a Suppliers
* Request:
    * Method: DELETE
    * Endpoint: /supplier/delete/<int:supplier_id>
* Response: message


# Entity
## Suppliers
* id: int
* shipper_name: string
* phone: string


## Shippers
### Get all Shippers
* Request
    * Method: GET
    * Endpoint: /shipper/all
    * Params: None
    * Body: None
* Response: [Shippers]
### Add a Shippers
* Request
    * Method: POST
    * Endpoint: /shipper/insert
    * Body:
        * shipper_name: string
        * phone: string
* Response: Message
### Get Shippers by ID
* Request
    * Method: GET
    * Endpoint: /shipper/get/<int:shipper_id>
* Response: Message
### Update a Shippers
* Request:
    * Method: PUT
    * Endpoint: /shipper/update/<int:shipper_id>
    * Body:
        * shipper_name: string
        * phone: string
* Response: Message

### Delete a Shippers
* Request:
    * Method: DELETE
    * Endpoint: /shipper/delete/<int:shipper_id>
* Response: message