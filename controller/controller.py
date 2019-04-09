# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:19:02 2019

@author: Lenovo
"""
from mysql.connector import errorcode
from mvc_database.model.model import Model
from mvc_database.view.view import View
from mvc_database.model import mvc_exceptions as m_e

class Controller:
    def __init__(self):
        #Instantiate a view
        self.view = View()
        #Instantiate a model
        try:
            self.model = Model('store')
        except m_e.error_with_db as e:
            print(str(e))

    def create_a_client(self, id_client, name, email, address, telephone, RFC):
        try: # LO QUE QUEREMOS QUE HAGA
            self.model.create_a_client(id_client, name, email, address, telephone, RFC)
        except m_e.person_already_stored as e: # SI SUCEDE UN ERROR
            self.view.person_already_stored_error(e)
    
    def show_all_clients(self):
        people_in_db = self.model.read_all_clients()
        self.view.show_all_clients(people_in_db)
        
    def show_a_client(self, name):
        try:
            client = self.model.read_a_client(name)
            self.view.show_a_client(client)
        except m_e.person_not_stored as e:
            self.view.person_not_stored_error(e)
         
    def update_a_client(self, old_name, new_id_client, new_name, new_email, new_address, new_telephone, new_RFC):
        try:
            self.model.update_a_client(old_name, new_id_client, new_name, new_email, new_address, new_telephone, new_RFC)
        except m_e.person_not_stored as e:
            self.view.person_not_stored_error(e)
            
    def delete_a_client(self, name):
        try:
            self.model.delete_a_client(name)
        except m_e.person_not_stored as e:
            self.view.person_not_stored_error(e)
            
    def consult_by_category(self, category):
        try:
            list_products_by_category = self.model.consult_by_category(category)
            self.view.consult_by_category(category)
            self.view.show_all_products(list_products_by_category)
        except m_e.category_not_found as e:
            self.view.category_not_found_error(e)
            
    """ FOR PRODUCT """
    
    def create_a_product(self, name, brand, category, price, weight, batch):
        try: # LO QUE QUEREMOS QUE HAGA
            self.model.create_a_product(self, name, brand, category, price, weight, batch)
        except m_e.product_already_stored as e: # SI SUCEDE UN ERROR
            self.view.product_already_stored_error(e)
    
    def show_all_products(self):
        products_in_db = self.model.read_all_products()
        self.view.show_all_products(products_in_db)
        
    def show_a_product(self, name):
        try:
            product = self.model.read_a_product(name)
            self.view.show_a_product(product)
        except m_e.product_not_stored as e:
            self.view.product_not_stored_error(e)
         
    def update_a_product(self, old_name, new_id_product, new_name, new_category, new_price, new_weight, new_lot, new_brand, new_provider):
        try:
            self.model.update_a_product(old_name, new_id_product, new_name, new_category, new_price, new_weight, new_lot, new_brand, new_provider)
        except m_e.product_not_stored as e:
            self.view.product_not_stored_error(e)
            
    def delete_a_product(self, name):
        try:
            self.model.delete_a_product(name)
        except m_e.product_not_stored as e:
            self.view.product_not_stored_error(e)
    
    def start(self):
        # Instantiate a model
        self.model = Model()
        # Instantiate a view
        self.view = View()
        # Display a welcome message
        self.view.start_view()
        
        #INSERT DATA
        """
        self.create_a_client('JP123','juan perez','juanitop@ugto.mx','Calle Bugambilia No. 123 Fracc. Las camelinas','4621687654','JUAM921345')
        self.create_a_client('AC534','ana contreras','anita_huerfanita@gugto.mx','Blvd. Alameda No. 1233 Zona centr','4627894561','ANCO857489')
        self.create_a_client('PO862','pedro orozco','pepeo_12@ugto.mx','Calle Games No. 543 Fracc. Orquidea','4621558874','PEOR847596')
        self.create_a_client('LM123','luis medrano','lu_me@ugto.mx','Dirección total 123','4615879586','LUME684578')
        self.show_all_clients()
        """
        
        self.create_a_product(5, 'jabon zote', 'limpieza', 18, 0.1, '1AB', 'brand1', 'proveedor1')
        self.create_a_product(12,'crayones','papeleria',45,0.76,'F23','brand6','proveedor6')
        self.create_a_product(6, 'jabonpet', 'mascotas', 30, 1, '1AB', 'brand2', 'proveedor2')
        self.create_a_product(9, 'tijeras', 'papeleria', 42, 0.2, '1AB', 'brand3', 'proveedor3')
        self.create_a_product(11, 'shampoo', 'limpieza', 21, 0.56, '1AB', 'brand4', 'proveedor4')
        self.create_a_product(3, 'cloro', 'limpieza', 5, 0.1, '1AB', 'brand5', 'proveedor5')
        self.show_all_products()
        #self.create_a_product( id_product, 'name', 'category', price, weight, 'lot', 'brand', 'provider')
        opcion = 'X'
        while opcion != 'Y' :
            # Display menu message
            self.view.menu()
            opcion = input()
            
            if opcion == 'A':
                # Consular pot categoría
                self.view.consult_category()
                categ = input()
                self.consult_by_category(categ)
                
            if opcion == 'C':
                # Mostrar un producto
                self.view.consult_product()
                product_name = input()
                self.show_a_product(product_name)
            
            if opcion == 'D':
                # Mostrar un cliente
                self.view.consult_client()
                name_client = input()
                self.show_a_client(name_client)
            
            if opcion == 'E':
                # Crear un nuevo cliente
                print('ID: ')
                id_client = input()
                print('NAME "Firstname Lastname": ')
                name = input()
                print('EMAIL: ')
                email = input()
                print('ADDRESS: ')
                address = input()
                print('TELEPHONE: ')
                telephone = input()
                print('RFC: ' )
                RFC = input() 
                self.create_a_client(id_client, name, email, address, telephone, RFC)
                self.show_all_clients
                
        # DELETE A PERSON
        self.delete_a_client('juan lopez')
        self.update_a_client('juan perez', 'new_id_client', 'new_first_name', 'new_last_name', 'new_email', 'new_address', 'new_telephone', 'new_RFC')
        # SHOW ALL PERSONS
        self.show_all_clients()
        # SHOW A PERSON IN DB
        self.show_a_client('luis zapata')
        self.view.end_view()