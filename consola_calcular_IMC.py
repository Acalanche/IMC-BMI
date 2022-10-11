#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:26:25 2022

@author: arturo
"""

def calcular_IMC(peso,altura:float)->float:
    """Esta función calcula el indice de masa corporal de una persona."""
    imc=round((peso/((altura)**2)),2)
    return imc

peso=float(input("PESO EN Kg: ")) #da entrada al peso de la persona en kilogramos
altura=float(input("ALTURA EN m: "))#da entrada al valor de la altura en metros
IMC=calcular_IMC(peso,altura)

print("Su IMC es de = "+str(IMC))