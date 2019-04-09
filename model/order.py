# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:07:17 2019

@author: Lenovo
"""

class Order:
    def __init__(self, id_order, id_product, cost): #_init_ define el constructor
        self.id_order = id_order
        self.id_product = id_product
        self.cost = cost