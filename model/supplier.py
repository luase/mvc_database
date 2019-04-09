# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:07:17 2019

@author: Lenovo
"""

class Supplier:
    def __init__(self, id_supplier, name, email, address, telephone, rfc): #_init_ define el constructor
        self.id_supplier = id_supplier
        self.name = name
        self.email = email
        self.address = address
        self.telephone = telephone
        self.rfc = rfc