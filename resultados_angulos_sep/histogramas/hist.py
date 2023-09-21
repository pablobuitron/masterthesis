import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("70-90deg_086400_100m.csv", delimiter="\s+")

# Crear una figura con tres subplots para los histogramas
fig, axs = plt.subplots(3, 1, figsize=(8, 10))

# Histograma de la variable "z"
counts_z, bins_z, _ = axs[0].hist(data["z"], bins=15, color='blue', alpha=0.7)
axs[0].set_xlabel("z")
axs[0].set_ylabel("Frecuencia")
axs[0].set_title("Histograma de z")
axs[0].set_yscale("log")  # Utilizar escala logarítmica para el eje y

# Calcular las barras de error
#errors_z = np.sqrt(counts_z)

# Mostrar las barras de error
#axs[0].errorbar(
#    x=(bins_z[:-1] + bins_z[1:]) / 2,
#    y=counts_z,
#    yerr=errors_z,
#    fmt='none',
#    color='black'
#)

#Letras Griegas
phi = "\u03C6"
theta = "\u03B8"

# Histograma de la variable "prm_theta"
counts_theta, bins_theta, _ = axs[1].hist(data["prm_theta"], bins=20, color='green', alpha=0.7)
axs[1].set_xlabel(f"Ángulo azimutal {theta}")
axs[1].set_ylabel("Frecuencia")
axs[1].set_title(f"Histograma de {theta}")

# Calcular las barras de error
errors_theta = np.sqrt(counts_theta)

# Mostrar las barras de error
axs[1].errorbar(
    x=(bins_theta[:-1] + bins_theta[1:]) / 2,
    y=counts_theta,
    yerr=errors_theta,
    fmt='none',
    color='black'
)

# Histograma de la variable "prm_phi"
counts_phi, bins_phi, _ = axs[2].hist(data["prm_phi"], bins=20, color='orange', alpha=0.7)
axs[2].set_xlabel(f"Ángulo polar {phi}")
axs[2].set_ylabel("Frecuencia")
axs[2].set_title(f"Histograma de {phi}")

# Calcular las barras de error
errors_phi = np.sqrt(counts_phi)

# Mostrar las barras de error
axs[2].errorbar(
    x=(bins_phi[:-1] + bins_phi[1:]) / 2,
    y=counts_phi,
    yerr=errors_phi,
    fmt='none',
    color='black'
)

# Ajustar los espacios entre subplots
plt.tight_layout()

# Obtener el nombre del archivo sin la extensión
nombre_archivo = "7-90deg"

# Guardar la figura en una imagen PNG con el nuevo nombre
plt.savefig(nombre_archivo + "_ánguloshistogramas.png")

