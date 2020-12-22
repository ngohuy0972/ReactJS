import psycopg2
from BusinessObjects import Customer as CustomerEntity

# Customer Start
class Customer:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    def get_all_customer(self):
        conn = psycopg2.connect(host = self.ConnectionData['host'],
                            port = self.ConnectionData['port'],
                            user = self.ConnectionData['user'],
                            password = self.ConnectionData['password'],
                            database = self.ConnectionData['database'])
        cursor = conn.cursor()
        sql = "SELECT * FROM Customers"
        cursor.execute(sql)
        conn.commit()
        rows = cursor.fetchall()
        result = []
        for row in rows:
            customer = CustomerEntity()
            customer.fetch_data(row)
            result.append(customer.to_json())
        return result

    def insert_customer(self, customer):
        conn = None
        try:
            conn = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = conn.cursor()
            sql = "INSERT INTO Customers(CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (%s, %s, %s, %s, %s, %s)"
            record_to_insert = (customer.CustomerName, customer.ContactName, customer.Address, customer.City, customer.PostalCode, customer.Country)
            cur.execute(sql, record_to_insert)
            conn.commit()
            conn.close()
            return 'Insert Customer successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if conn is not None:
                conn.close()

    def delete_customer_by_id(self, customer):
        conn = None
        conn = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
        cursor = conn.cursor()
        sql = "DELETE FROM Customers WHERE CustomerID = %s"
        cursor.execute(sql, (customer.CustomerID, ))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Deleted successfully', 200
        return 'Id not found', 404        

    def update_customer(self, customer):
        conn = None
        conn = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
        cursor = conn.cursor()
        sql = """UPDATE Customers SET
                    CustomerName=%s, ContactName=%s, Address=%s,
                    City=%s, PostalCode=%s, Country=%s WHERE CustomerID=%s"""
        cursor.execute(sql, (customer.CustomerName, customer.ContactName, customer.Address, customer.city, customer.PostalCode, customer.Country, customer.CustomerID))
        conn.commit()
        n = cursor.rowcount
        if n > 0:
            return 'Updated successfully', 200
        return 'Id not found', 404


if __name__ == "__main__":
    print('this is data object package')