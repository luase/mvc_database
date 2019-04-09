# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 11:07:17 2019

@author: Lenovo
"""

class Client:
    def __init__(self, id_client, first_name, last_name, email, address, telephone, rfc): #_init_ define el constructor
        self.id_client = id_client
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.telephone = telephone
        self.rfc = rfc
