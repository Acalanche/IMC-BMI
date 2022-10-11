#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 11:32:55 2022

@author: arturo
"""

def calcular_calorias_en_actividad(peso,altura, edad, valor_genero,valor_actividad:float)->float:
    """esta funcion calcula la tasa metabolica basal en actividad fisica"""
   
    tmb_a=round(((10*peso)+(6.25*(altura*100))-(5*edad)+valor_genero)*valor_actividad,2)
    return tmb_a
peso=float(input("PESO EN Kg: ")) #da entrada al peso de la persona en kilogramos
altura=float(input("ALTURA EN m: "))#da entrada al valor de la altura en metros, cuando sea requerido, la función hara la conversión a cm
genero=int(input("indique con un '-161' para sexo femenino o con '5'para sexo masculino: "))
#en esta opción se le pide al usuario asignar un valor para el genero donde
#         masculino=5
#        femenino=(-161)
#define un valor para el genero, dado por el usuario. la función asigna los valores 10.8 en caso de que la opción ingresada sea 1(masculino) o 0 para la opción 0(femenino)
edad= int(input("EDAD EN AÑOS: "))#da entrada a la edad en años
ejercicio=float(input("escoja un valor para los siguientes niveles de actividad física que realiza la persona \n 1.2: poco o ningún ejercicio \n 1.375: ejercicio ligero(1 a 3 días a la semana) \n 1.55: ejercicio moderado(3 a 5 días a la semana)\n 1.725: deportista (se ejercita de 6 a 7 días a la semana)\n 1.9: atleta (realiza entrenamientos diarios por la mañana y por la tarde)\n"))
#en esta opción, se le pide al usuario que de un valor determinado para la actividad física
#        poco o nula actividad física=1.375
#        de 2 a 3 días de actividad física=1.55
#        de 5 a 7 dias=1.725
#        valor_actividad=1.9
tmb_a=calcular_calorias_en_actividad(peso, altura, edad, genero,ejercicio)
print("Su tasa metabolica basal en activdad es de "+str(tmb_a)+"cal")