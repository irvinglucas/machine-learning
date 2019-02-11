import os
import pandas as pd
import time as t

diretorio_dataset = os.getcwd()
diretorio_dataset +=r"\black-friday.xlsx"
print(diretorio_dataset)
inicio = t.time()
data_frame = pd.read_excel(diretorio_dataset)
fim = t.time()
tempo = fim-inicio
print("dataset carregado em: %.2f" %(tempo))
inicio = t.time()
print(data_frame.head())
fim = t.time()
tempo = fim-inicio
print("dataset impresso em: %.2f" %(tempo))