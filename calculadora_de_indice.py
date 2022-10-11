#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:18:55 2022

@author: arturo
"""
#se importan las funciones de los modulos
import modulo_calcular_IMC as imc #modulo de INDICE DE MASA CORPORAL
import modulo_calcular_porcentaje_grasa as GC #modulo de PORCENTAJE DE GRASA CORPORAL
import modulo_calcular_TMB as TMB # modulo de  TASA METABOLICA BASAL
#EN  EL MODULO DE TASA METABOLICA BASAL SE ENCUENTRAN LAS 3 FUNCIONES RELACIONADAS AL TMB: EL TMB EN REPOSO, EL TMB EN ACTIVIDAD FÍSICA Y LOS CALCULOS PARA CONSUMOS MÍNIMO Y MÁXIMO DE CALORIAS


peso=float(input("PESO EN Kg: ")) #da entrada al peso de la persona en kilogramos
altura=float(input("ALTURA EN m: "))#da entrada al valor de la altura en metros, cuando sea requerido, la función hara la conversión a cm
genero=int(input("indique con un '0' para sexo femenino o con '1'para sexo masculino: "))#define un valor para el genero, dado por el usuario. la función asigna los valores 10.8 en caso de que la opción ingresada sea 1(masculino) o 0 para la opción 0(femenino)
edad= int(input("EDAD EN AÑOS: "))#da entrada a la edad en años
ejercicio=int(input("indique el nivel de actividad física que realiza \n 1: poco o ningún ejercicio \n 2: ejercicio ligero(1 a 3 días a la semana) \n 3: ejercicio moderado(3 a 5 días a la semana)\n 4: deportista (se ejercita de 6 a 7 días a la semana)\n 5: atleta (realiza entrenamientos diarios por la mañana y por la tarde)\n"))#en esta opción, se le pide al usuario que seleccione una categoria entre el 1 y 5, la función se encargará de asignar un valor determinado para cada opción.
IMC=imc.calcular_IMC(peso,altura)
gc=GC.calcular_porcentaje_grasa(IMC,edad,genero)
tmb=TMB.calcular_calorias_en_reposo(peso, altura, edad, genero)
tmb_a=TMB.calcular_calorias_en_actividad(tmb,ejercicio)
c_m=TMB.consumo_calorias_minimo_para_adelgazar(tmb)
c_M=TMB.consumo_calorias_max_para_adelgazar(tmb)
#SE HAN AÑADIDO LAS OPCIONES PARA IMPRIMIR DIRECTAMENTE LOS VALORES DEL IMC, %GC, EL TMB Y EL TMB EN ACTIVIDAD, CASO SEA REQUERIDO PARA MODIFICACIONES FUTURAS

print("Su IMC es de = "+str(IMC))
print("Sus valores de % de grasa corporal es de "+str(gc)+"%")
print("Su tasa metabolica basal en reposo es de "+str(tmb)+"cal")
print("Su tasa metabolica basal en actividad es de "+str(tmb_a)+"cal")
print("si desea adelgazar, debera consumir entre "+str(c_m)+"cal y "+str(c_M)+"cal, siendo "+str(c_m)+"cal, lo mínimo y"+str(c_M)+"cal, lo máximo")
