import numpy as np
import pandas as pd
import random
import math
from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()


data = iris.data[:,0:2]

print(data)

target = iris.target

k = 3

print(target)

def dist(x0, y0, x1, y1):
    a = (x1 - x0)**2 + (y1 - y0)**2
    b = math.sqrt(a)
    return b

porcentagem = 0.4  #Porcentagem pega dos target

Data_treinamento_ind = []

porInd = int(len(target)*porcentagem)

for i in range(porInd):
    i1 = random.randint(0,len(target)-1)
    Data_treinamento_ind.append(i1)     #######
    
    
print(Data_treinamento_ind)
Data_treinamento = np.array(target)[Data_treinamento_ind] #######

Data_Completo_treina = np.array(data)[Data_treinamento_ind]  #######

print(Data_Completo_treina)

grupo_treinamento = {'Elemento':[Data_treinamento_ind],'Data':[Data_Completo_treina],'Classificação':[Data_treinamento]}

#####
 

for i in range(len(data)):
    x0 = data[i][0]   
    y0 = data[i][1]
    Classifica_Distancias = [[],[],[]]
    for j in range(len(grupo_treinamento['Elemento'][0])):
        

















