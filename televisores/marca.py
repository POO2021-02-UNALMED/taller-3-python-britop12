# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 19:08:07 2021

@author: esteb
"""


class Marca:
    def __init__(self, nombre):
        self._nombre = nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre 

    def getNombre(self):
        return self._nombre 