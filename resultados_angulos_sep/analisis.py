import pandas as pd
import matplotlib.pyplot as plt
import random

# Generar valores aleatorios para n y m
n = 60
m = 90

# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("merged0-70-90.csv", delimiter="\s+")

# Realizar un plot de dispersión entre las columnas "x" y "y"
plt.scatter(data["x"], data["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Distancia al detector, ángulos entre 0° a 70° a 90° unidos")

# Obtener el nombre del archivo sin la extensión
nombre_archivo = f"{n}sec{m}deg"

# Guardar el gráfico en una imagen PNG con el nuevo nombre
#plt.savefig(nombre_archivo + ".png")
plt.savefig("merged" + ".png")

# Hacer la preselección de datos según CorsikaId y prm_theta
preseleccion = data[data["prm_theta"] >= 0]

# Crear tablas distintas según CorsikaId
tablas_por_corsika_id = preseleccion.groupby("CorsikaId")

# Guardar las tablas resultantes en un archivo de texto
with open("head_merged.txt", "w") as file:
    for corsika_id, tabla in tablas_por_corsika_id:
        file.write(f"Tabla para CorsikaId {corsika_id}:\n")
        file.write(tabla.to_string())
        file.write("\n\n")
