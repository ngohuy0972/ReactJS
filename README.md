# ReactJS
# Ngô Văn Huy
# Lương Đức Tài
# Phan Thế Sanh

# git clone 
# git  status
# git commit -m""
# git add .
# git push

# Xem cấu trúc thư mục cơ bản trong một project React : https://viblo.asia/p/react-cau-truc-thu-muc-du-an-va-dat-ten-component-aWj53GMY56m


# Backend

## connect server 
ssh -p 4567 ubuntu@ip_of_real_machine

# docker for Windows
docker build -t backend .
docker run -d --name backend --env db_ip-IP_OF_DOCKER -p 8080:8080 backend
docker stop backend
docker rm backend
docker exec -it coredb bash

# Deploy db
docker load --input postgres_11.2-alpine.tar
docker run -d --restart unless-stopped --name coredb -e POSTGRES_PASSWORD-postgres-e POSTGRES_DB-postgres -v /northwind_db:/var/lib/postgresql/data -p 5432:5432 postgres:11.2-alpine

# postgres
psql -U postgres
\l
create database xyz;
\c xyz;