#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:02:56 2022

@author: arturo
"""


def calcular_calorias_en_reposo(peso,altura, edad, valor_genero:float)->float:
    """esta funcion calcula la tasa metabolica basal en estado de reposo"""
    if valor_genero==1:
        valor_genero=5
    if valor_genero==0:
        valor_genero=(-161)
    tmb=round((10*peso)+(6.25*(altura*100))-(5*edad)+valor_genero,2)
    return tmb
def calcular_calorias_en_actividad(tmb,valor_actividad:float)->float:
    """esta funcion calcula la tasa metabolica basal en actividad fisica"""
    if valor_actividad==1:
        valor_actividad=1.2
    if valor_actividad==2:
        valor_actividad=1.375
    if valor_actividad==3:
        valor_actividad=1.55
    if valor_actividad==4:
        valor_actividad=1.725
    if valor_actividad==5:
        valor_actividad=1.9
    tmb_a=round(tmb*valor_actividad,2)
    return tmb_a

def consumo_calorias_minimo_para_adelgazar(tmb:float)->float:
    consumo_min=round((tmb*(80/100)),2)
    return consumo_min
def consumo_calorias_max_para_adelgazar(tmb:float)->float:
    consumo_max=round((tmb*(85/100)),2)
    return consumo_max