import psycopg2
from BusinessObjects import Customer as CustomerEntity

# Customer Start
class Customer:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData

    # def get_all_customer(self, customer):
    #     con = None
    #     try:
    #         con = psycopg2.connect(user=self.ConnectionData['user'],
    #                               password=self.ConnectionData['password'],
    #                               host=self.ConnectionData['host'],
    #                               port=self.ConnectionData['port'],
    #                               database=self.ConnectionData['database'])
    #         cur = con.cursor()
    #         sql = "SELECT * FROM Customers"
    #         cur.execute(sql)
    #         con.commit()
    #         con.close()
    #         return sql.text
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         return str(error)
    #     finally:
    #         if con is not None:
    #             con.close()

    def insert_customer(self, customer):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "INSERT INTO Customers(CustomerName, ContactName, Address, City, PostalCode, Country) VALUES (%s, %s, %s, %s, %s, %s)"
            record_to_insert = (customer.CustomerName, customer.ContactName, customer.Address, customer.City, customer.PostalCode, customer.Country)
            cur.execute(sql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert Customer successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def delete_customer(self, customer):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "DELETE FROM customers WHERE CustomerID = '2'"
            cur.execute(sql)
            con.commit()
            con.close()
            return 'Delete Customer successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()

    def update_customer(self, customer):
        con = None
        try:
            con = psycopg2.connect(user=self.ConnectionData['user'],
                                  password=self.ConnectionData['password'],
                                  host=self.ConnectionData['host'],
                                  port=self.ConnectionData['port'],
                                  database=self.ConnectionData['database'])
            cur = con.cursor()
            sql = "UPDATE Customers SET CustomerName = 'HuyVanNgo' WHERE CustomerID = '6'"
            cur.execute(sql)
            con.commit()
            con.close()
            return 'Update Customer successfully'
        except (Exception, psycopg2.DatabaseError) as error:
            return str(error)
        finally:
            if con is not None:
                con.close()


if __name__ == "__main__":
    print('this is data object package')