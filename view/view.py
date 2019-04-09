# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:21:12 2019

@author: Lenovo
"""

class View:
    def show_all_clients(self,lista):
        print("\nIn my db I have %i clients, here they are:\n" % len(lista))
        for client in lista:
            print(client.name+' '+client.email)
    
    def show_all_products(self,lista):
        print("\nProducts:\n")
        for product in lista:
            print(product.name+': $'+str(product.price))   
        
    def show_a_client(self, client):
        print('********** DETAILS FOR ***********')
        print('* Id Client: '+client.id_client)
        print('* Name: '+client.name)
        print('* Email: '+client.email)
        print('* Address: '+client.address)
        print('* Telephone: '+client.telephone)
        print('* RFC: '+client.RFC)
        print('**********************************')
        
    def show_a_product(self, product):
        print('********** DETAILS FOR ***********')
        print('* Id Product: '+product.id_product)
        print('* Name: '+product.name)
        print('* Category: '+product.category)
        print('* Price: $'+product.price)
        print('* Weight: '+product.weight)
        print('* Lot: '+product.lot)
        print('* Brand: '+product.brand)
        print('* Provider: '+product.provider)
        print('**********************************')
        
    def start_view(self):
        print('\tA VERY SIMPLE EXAMPLE\n')
        print('\n\t ¡¡Bienvenido!! ')
        
    def menu(self):
        print('\n\t ¿Qué desea hacer?: \n')
        print('\n[A]: Consultar productos por categoría.')
        print('\n[B]: Consultar productos por rango de precio.')
        print('\n[C]: Mostrar un producto.')
        print('\n[D]: Mostrar un cliente.')
        print('\n[E]: Crear un nuevo cliente.')
        print('\n[F]: Crear un nuevo producto.')
        print('\n[G]: Mostrar todos los clientes.')
        print('\n[H]: Mostrar todos los productos.')
        print('\n[I]: Actualizar un cliente.')
        print('\n[J]: Actualizar un producto')
        print('\n[K]: Eliminar un cliente.')
        print('\n[L]: Eliminar un producto.')
        print('\n[E]: Salir.')
    
    def consult_product(self):
        print('Ingrese el producto a buscar: \n')
        
    def consult_client(self):
        print('Ingrese el cliente a mostrar: \n')
        
    def create_client(self):
        print('Ingrese los datos del nuevo cliente: \n')
        
    def consult_category(self):
        print('Ingrese la categoría para la consulta: \n')
        
    def consult_by_category(self, category):
        print('The products in the "{}" category are:\n'.format(category.upper()))
        
    def end_view(self):
        print('\n\t\tSee you later!')
    
    def person_not_stored_error(self, e):
        print('************ ERROR! **************')
        print(e.args[0])
    
    def person_already_stored_error(self, e):
        print('************ ERROR! **************')
        print(e.args[0])
        
    def product_not_stored_error(self, e):
        print('************ ERROR! **************')
        print(e.args[0])
        
    def product_already_stored_error(self, e):
        print('************ ERROR! **************')
        print(e.args[0])
        
    def category_not_found_error(self, e):
        print('************ ERROR! **************')
        print(e.args[0])