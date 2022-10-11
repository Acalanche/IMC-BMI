#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:02:33 2022

@author: arturo
"""


def calcular_IMC(peso,altura:float)->float:
    """Esta función calcula el indice de masa corporal de una persona."""
    imc=round((peso/((altura)**2)),2)
    return imc