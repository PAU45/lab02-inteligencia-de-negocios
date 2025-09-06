import matplotlib.pyplot as plt

# Datos
x = [2012, 2022, 2025, 2028]
y = [42, 43, 45, 47]  # Perú
x2 = [2012, 2022, 2025, 2028]
y2 = [42, 48, 49, 50]  # Colombia

plt.plot(x, y, marker='o', label='Perú')
plt.plot(x2, y2, marker='s', label='Colombia')
plt.xlabel('Año')
plt.ylabel('Población')
plt.title('Población Perú vs Colombia')
plt.legend()
plt.show()