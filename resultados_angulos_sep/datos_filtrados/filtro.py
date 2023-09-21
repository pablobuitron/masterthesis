import pandas as pd
import matplotlib.pyplot as plt
import random

# Generar valores aleatorios para n y m
n = 70
m = 90

# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("70-90deg_000060.csv", delimiter="\s+")

# Filtrar los datos con "x" y "y" menores o iguales a 1000
filtered_data = data[(data["x"].abs() <= 100) & (data["y"].abs() <= 100)]

# Realizar un plot de dispersión entre las columnas "x" y "y"
plt.scatter(filtered_data["x"], filtered_data["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Distancia al detector, ángulos entre 70° a 90°")

# Obtener el nombre del archivo sin la extensión
nombre_archivo = f"{n}-{m}deg_000060"

# Guardar el gráfico en una imagen PNG con el nuevo nombre
#plt.savefig(nombre_archivo + ".png")
plt.savefig("filter-" + nombre_archivo + "_100m.png")

# Guardar los datos filtrados en un archivo de texto
filtered_data.to_csv("filter_" + nombre_archivo + ".txt", sep=" ", index=False)
