#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:23:31 2022

@author: arturo
"""

def calcular_calorias_en_reposo(peso,altura, edad, valor_genero:float)->float:
    """esta funcion calcula la tasa metabolica basal en estado de reposo"""
    tmb=round((10*peso)+(6.25*(altura*100))-(5*edad)+valor_genero,2)
    return tmb

peso=float(input("PESO EN Kg: ")) #da entrada al peso de la persona en kilogramos
altura=float(input("ALTURA EN m: "))#da entrada al valor de la altura en metros, cuando sea requerido, la función hara la conversión a cm
genero=int(input("indique con un '0' para sexo femenino o con '1'para sexo masculino: "))#define un valor para el genero, dado por el usuario. la función asigna los valores 10.8 en caso de que la opción ingresada sea 1(masculino) o 0 para la opción 0(femenino)
edad= int(input("EDAD EN AÑOS: "))#da entrada a la edad en años
tmb=calcular_calorias_en_reposo(peso, altura, edad, genero)

print("Su tasa metabolica basal en reposo es de "+str(tmb)+"cal")