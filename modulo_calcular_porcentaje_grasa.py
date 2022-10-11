#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:02:31 2022

@author: arturo
"""


def calcular_porcentaje_grasa(imc,edad,valor_genero:float)->float:
    """esta función calcula el % de grasa corporal"""

    if valor_genero==1:#esta cindición asegura que si el valor introducido por el usuario sea "1", se le asignara el valor "10.8" dentro de la función.
        valor_genero=10.8
    if valor_genero==0:#esta condicíon asegura que si el valor introducido por el usuario sea "0", se le asigna el valor "0" dentro de la función.
        valor_genero=0
    gc = round((1.2*imc+0.23*edad-5.4-valor_genero),2)
    return gc