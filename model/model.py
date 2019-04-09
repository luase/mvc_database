import mysql.connector
from mvc_database.view.view import View
from product import Product
from client import Client
import mvc_exceptions as m_e

#Database Methods
class Model:
    # A DATA MODEL WITH MYSQL

    def __init__(self, db_name = 'store'):
        self.db_name = db_name
        self.connect_to_db()
        self.define_tables()
        self.create_tables()

    def define_tables(self):
        self.tables = {}
        self.tables['products'] = (
            'CREATE TABLE `products` ('
            ' `id_product` int(10) NOT NULL AUTO_INCREMENT,'
            ' `name` varchar(20) NOT NULL UNIQUE,'
            ' `brand` varchar(15) NOT NULL,'
            ' `category` varchar(15)'
            ' `price` float NOT NULL,'
            ' `weight` float,'
            ' `batch` varchar(7),'
            ' PRIMARY KEY (`id_product`)'
            ')')
        self.tables['clients'] = (
            'CREATE TABLE `clients` ('
            '   `id_client` int(10) NOT NULL AUTO_INCREMENT,'
            '   `name` varchar(40) NOT NULL,'
            '   `email` varchar(30),'
            '   `address` varchar(50) NOT NULL,'
            '   `phone` varchar(11),'
            '   `rfc` varchar(13),'
            '   PRIMARY KEY (`id_client`)'
            ')')

    def create_database(self):
        self.cursor.execute(
            'CREATE DATABASE {} DEFAULT CHARACTER SET "utf8"'.format(self.db_name))
        self.cnx.database = self.db_name
        
    def connect_to_db(self):
        self.cnx = mysql.connector.connect(user = 'User1', password = 'password1')
        self.cursor = self.cnx.cursor()
        try:
            self.cursor.execute('USE {}'.format(self.db_name))
            print('Connection created.')            
        except mysql.connector.Error:
            try:
                self.create_database()
            except mysql.connector.Error:
                raise m_e.error_with_db(
                    'Failed creating database {}.'.format(self.db_name.upper()))

    def disconnect_from_db(self):
        self.cursor.close()
        self.cnx.close()

    def create_tables(self):
        for table_name in self.tables:
            table_decription = self.tables[table_name]
            try:
                self.cursor.execute(table_decription)
            except mysql.connector.Error:
                pass
                    
    # Products methods
    def search_product(self, name):
        sql = 'SELECT * FROM products WHERE name = %s'
        self.cursor.execute(sql, (name,))      
        record = self.cursor.fetchone()        
        return record

    def create_a_product(self, name, brand, category, price, weight, batch):
        record = self.search_product(name)
        if record is None:
            sql = 'INSERT INTO products(`name`, `brand`, `category`, `price`, `weight`, `batch`) VALUES (%s, %s, %s, %s, %s, %s)'
            self.cursor.execute(sql,(name, brand, category, price, weight, batch))
            self.cnx.commit()
        else:
            self.cnx.rollback()
            raise m_e.item_already_stored('Product "{}" already stored.'.format(name.upper()))

    def read_all_products(self):
        sql = 'SELECT * FROM products'
        self.cursor.execute(sql)
        records = self.cursor.fetchall()
        products = []
        for record in records:
            products.append(Product(record[0], record[1], record[2], record[3], record[4], record[5], record[6]))
        return products