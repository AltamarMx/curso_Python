#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Persona:
    """Clase persona"""
    def __init__(self, nombre, nota):
        """Incialización de variables nombre y libro"""
        self.nombre = nombre #variable de objeto
        self.libro = nombre #variable de objeto
        
    def leer(self, libro):
        """Método para obtener el nombre y libro de lectura: self.nombre, self.libro :return"""
        return(self.nombre, self.libro)

