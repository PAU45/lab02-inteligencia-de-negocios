import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Iris-1.csv')
df['Species'].value_counts().plot(kind='bar')
plt.xlabel('Species')
plt.ylabel('Count')
plt.title('Distribución de Species en Iris')
plt.show()