#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 13:50:16 2022

@author: arturo
"""
import  consola_calcular_IMC as imc #modulo de INDICE DE MASA CORPORAL
def calcular_porcentaje_grasa(imc,edad,valor_genero:float)->float:
    """esta función calcula el % de grasa corporal"""
    gc = round((1.2*imc+0.23*edad-5.4-valor_genero),2)
    return gc
peso=float(input("PESO EN Kg: ")) #da entrada al peso de la persona en kilogramos
altura=float(input("ALTURA EN m: "))#da entrada al valor de la altura en metros, cuando sea requerido, la función hara la conversión a cm
edad= int(input("EDAD EN AÑOS: "))#da entrada a la edad en años
genero=float(input("indique  '0' para sexo femenino: \n '10.8'para sexo masculino: \n"))#define un valor para el genero dado por el usuario. 10.8 para masculino, 0 para femenino
IMC=imc.calcular_IMC(peso,altura)
gc=calcular_porcentaje_grasa(IMC,edad,genero)
print("Sus valores de % de grasa corporal es de "+str(gc)+"%")