import pandas as pd

def caracteristicas_data(df, nombre):
    print(f'Visualización del dataset: {nombre} \n')
    print('*'*50)
    print('Dimensión del dataset: ')
    print(df.shape)
    print('*'*50)
    print('Información de la data: ', df.info())

def prueba():
    return 'hola'
