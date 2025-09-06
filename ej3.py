import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Iris-1.csv')  # Cargar el archivo CSV

df['SepalWidthCm'].plot(kind='hist', bins=20, edgecolor='black')
plt.xlabel('SepalWidthCm')
plt.title('Histograma de SepalWidthCm')
plt.show()