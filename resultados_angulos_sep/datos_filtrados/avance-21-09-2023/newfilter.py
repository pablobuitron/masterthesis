import pandas as pd
import matplotlib.pyplot as plt
import random

# Generar valores aleatorios para n y m
n = 39.81
m = 90

# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("39.81-90deg_000600.csv", delimiter="\s+")

# Filtrar los datos con "x" y "y" menores o iguales a 1000
filtered_data = data[(data["x"] <= -499000) & (data["y"] <= 500000) & (data["y"] >= -500000)]

# Realizar un plot de dispersión entre las columnas "x" y "y"
plt.scatter(filtered_data["x"],filtered_data["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Distancia al detector, ángulos entre 39.81° a 90° que llegarían a 1km del detector real")

# Obtener el nombre del archivo sin la extensión
nombre_archivo = f"{n}-{m}deg_000600"

# Guardar el gráfico en una imagen PNG con el nuevo nombre
#plt.savefig(nombre_archivo + ".png")
plt.savefig("nuevofiltro-" + nombre_archivo + "_1km.png")

# Guardar los datos filtrados en un archivo de texto
filtered_data.to_csv("nuevofiltro_" + nombre_archivo + ".txt", sep=" ", index=False)

