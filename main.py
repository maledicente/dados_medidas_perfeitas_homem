import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import os
import csv

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 2020 

@author: Luiz Paulo Nievola
"""
class Pessoa():
   def __init__(self,n,al,pe,p,b,a,pei,ci,co,pa):
      self.nome = n
      self.altura = al
      self.peso = pe
      self.pescoco = pe
      self.biceps = b
      self.antebraco = a
      self.peito = pei
      self.cintura = ci
      self.coxas = co
      self.panturrilha = pa
   def Imc(self):
       return round(self.peso / (pow(self.altura, 2)),2)
   def Coef(self):
       return round((self.peso/self.altura)/100,3)
   def Dados(self):
      print("{} seu IMC atual é: {}".format(self.nome, self.Imc()))
      print("Coeficiente atual: ", self.Coef())

# Variaveis
Nome = input("Qual seu nome? ")
objetivo = pd.read_csv("data_med.csv", sep=',')

Altura = float(input("Qual a sua altura(0.00cm)? "))
Peso = float(input("Qual o seu peso(Kg)? "))
Pescoco = float(input("Qual a medida(cm) do pescoço? "))
Biceps = float(input("Qual a medida(cm) do biceps? "))
Antebraco = float(input("Qual a medida(cm) do antebraço? "))
Peito = float(input("Qual a medida(cm) do peito? "))
Cintura = float(input("Qual a medida(cm) da cintura? "))
Coxas = float(input("Qual a medida(cm) da coxa? "))
Panturrilha = float(input("Qual a medida(cm) da panturriha? "))

P1 = Pessoa(Nome,Altura,Peso,Pescoco,Biceps,Antebraco,Peito,Cintura,Coxas,Panturrilha)

med_atual = []
med_atual.append(P1.Coef())
med_atual.append(P1.peso)
med_atual.append(P1.pescoco)
med_atual.append(P1.biceps)
med_atual.append(P1.antebraco)
med_atual.append(P1.peito)
med_atual.append(P1.cintura)
med_atual.append(P1.coxas)
med_atual.append(P1.panturrilha)
df = pd.DataFrame(med_atual)

des = float(input("Qual peso deseja chegar(Kg)? "))
coef = round((des / P1.altura) / 100, 3)
meta = objetivo.loc[objetivo['Coeficiente'] == coef]
print("O coeficiente desejado é: ", coef)

print(med_atual)
plt.title("Comparativo de medidas")
plt.plot(meta,df)
plt.xlabel('Coeficiente desejado')
plt.ylabel('Coeficiente atual')
plt.show()

#print(coef_des)
#print("\n\033[32m",type(coef_atual-x))

