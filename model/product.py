# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:07:17 2019

@author: Lenovo
"""

class Product:
    def __init__(self, id_product, name, brand, category, price, weight, batch): #_init_ define el constructor
        self.id_product = id_product
        self.name = name
        self.brand = brand
        self.category = category
        self.price = price
        self.weight = weight
        self.batch = batch
        