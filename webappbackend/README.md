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