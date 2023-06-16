import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
# Generar valores aleatorios para n y m
n = 0
m = 70

# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("0-70deg_001800.csv", delimiter="\s+")

# Crear una figura con tres subplots para los histogramas
fig, axs = plt.subplots(3, 1, figsize=(8, 10))

# Histograma de la variable "z"
axs[0].hist(data["z"], bins=15, color='blue', alpha=0.7)
axs[0].set_xlabel("z")
axs[0].set_ylabel("Frecuencia")
axs[0].set_title("Histograma de z")
axs[0].set_yscale("log")  # Utilizar escala logarítmica para el eje y

#Letras Griegas
phi = "\u03C6"
theta = "\u03B8"

# Histograma de la variable "prm_theta"
axs[1].hist(data["prm_theta"], bins=20, color='green', alpha=0.7)
axs[1].set_xlabel(f"Ángulo azimutal {theta}")
axs[1].set_ylabel("Frecuencia")
axs[1].set_title(f"Histograma de {theta}")

# Histograma de la variable "prm_phi"
axs[2].hist(data["prm_phi"], bins=20, color='orange', alpha=0.7)
axs[2].set_xlabel(f"Ángulo polar {phi}")
axs[2].set_ylabel("Frecuencia")
axs[2].set_title(f"Histograma de {phi}")

# Ajustar los espacios entre subplots
plt.tight_layout()

# Obtener el nombre del archivo sin la extensión
nombre_archivo = f"{n}-{m}deg"

# Guardar la figura en una imagen PNG con el nuevo nombre
plt.savefig(nombre_archivo + "_ánguloshistogramas.png")

# Crear tablas distintas según CorsikaId
tablas_por_corsika_id = data.groupby("CorsikaId")

# Guardar las tablas resultantes en archivos de texto separados
for corsika_id, tabla in tablas_por_corsika_id:
    nombre_archivo_tabla = f"tabla_CorsikaId_{corsika_id}_0-70deg.txt"
    with open(nombre_archivo_tabla, "w") as file:
        file.write(f"Tabla para CorsikaId {corsika_id}:\n")
        file.write(tabla.to_string())
        file.write("\n\n")
