# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:38:31 2019

@author: Lenovo
"""
class error_with_db(Exception):
    pass

class item_already_stored(Exception):
    pass

class item_not_stored(Exception):
    pass

##############################################
class person_already_stored(Exception):
    pass

class person_not_stored(Exception):
    pass

class product_already_stored(Exception):
    pass

class product_not_stored(Exception):
    pass

class category_not_found(Exception):
    pass