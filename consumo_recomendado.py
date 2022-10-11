#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 12:31:57 2022

@author: arturo
"""

def consumo_calorias_minimo_para_adelgazar(peso,altura, edad, valor_genero:float)->float:
    consumo_min=round(((10*peso)+(6.25*(altura*100))-(5*edad)+valor_genero)*(80/100),2)
    return consumo_min
def consumo_calorias_max_para_adelgazar(peso,altura, edad, valor_genero:float)->float:
    consumo_max=round(((10*peso)+(6.25*(altura*100))-(5*edad)+valor_genero)*(85/100),2)
    return consumo_max

peso=float(input("PESO EN Kg: ")) #da entrada al peso de la persona en kilogramos
altura=float(input("ALTURA EN m: "))#da entrada al valor de la altura en metros, cuando sea requerido, la función hara la conversión a cm
genero=int(input("indique con un '-161' para sexo femenino o con '5'para sexo masculino: "))
#en esta opción se le pide al usuario asignar un valor para el genero donde
#         masculino=5
#        femenino=(-161)
#define un valor para el genero, dado por el usuario. la función asigna los valores 10.8 en caso de que la opción ingresada sea 1(masculino) o 0 para la opción 0(femenino)
edad= int(input("EDAD EN AÑOS: "))#da entrada a la edad en años

c_m=consumo_calorias_minimo_para_adelgazar(peso,altura, edad, genero)
c_M=consumo_calorias_max_para_adelgazar(peso,altura, edad, genero)

print("si desea adelgazar, debera consumir entre "+str(c_m)+"cal y "+str(c_M)+"cal, siendo "+str(c_m)+"cal, lo mínimo y"+str(c_M)+"cal, lo máximo")
