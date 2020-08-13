import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import os
# -*- coding: utf-8 -*-

"""
Created on Thu Aug 13 2020

@author: Luiz Paulo Nievola
"""
   
#Variaveis

coef=pescoco=biceps=antebraco=peito=cintura=quadris=coxas=panturrilha=des=0
coef_atual = [0.441,41,36,30,109,99,100,59,41]
coef_des = geek.arange(8)

al=float(input("Qual sua altura(0.00cm)? "))
pe=float(input("Qual seu peso(Kg)? "))
print("Seu IMC atual é: {:.2f}".format(pe/(pow(al,2))))

des=float(input("Qual peso deseja chegar(Kg)? "))
coef=round((des/al)/100,3)
print("O coeficiente desejado é: ",coef)
#Ler .csv
df=pd.read_csv('data_med.csv')
x=df.loc[df['Coeficiente']==coef].values




plt.title("Comparativo medidas")
#plt.bar(coef_des,coef_atual)
plt.gray()
plt.xlabel('Coeficiente desejado')
plt.ylabel('Coeficiente atual')
print(coef_des)

#print(coef_des)
#print("\n\033[32m",type(coef_atual-x))

