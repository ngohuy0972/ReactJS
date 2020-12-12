# Tên image:tag
FROM node:10

#App Directory 
WORKDIR /usr/src/app

# Copy tất cả các package*.json vào cái WORKDIR directory 
COPY package* ./

# Vì đây đang sử dụng thư viện express chứ ko phải project trống nên để chạy nên phải install express lên
RUN npm install 

# Copy tất cả các những cái trong Foler ReactJs lên trên Workdir directory 
COPY . .

# EXPOSE 8080 là cái port trên docker chứ không phải trên cái máy của mình
EXPOSE 8080


CMD [ "node", "index.js"]