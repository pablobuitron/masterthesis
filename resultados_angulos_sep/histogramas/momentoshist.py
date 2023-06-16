import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("70-90deg_086400_50m.txt", delimiter="\s+")

# Crear una figura con tres subplots para los histogramas
fig, axs = plt.subplots(3, 1, figsize=(8, 10))

# Histograma de la variable "px"
axs[0].hist(data["px"], bins=25, color='blue', alpha=0.7)
axs[0].set_xlabel("px")
axs[0].set_ylabel("Frecuencia")
axs[0].set_title("Histograma de px")
axs[0].set_yscale("log")  # Utilizar escala logarítmica para el eje y

# Histograma de la variable "py"
axs[1].hist(data["py"], bins=25, color='green', alpha=0.7)
axs[1].set_xlabel("py")
axs[1].set_ylabel("Frecuencia")
axs[1].set_title("Histograma de py")
axs[1].set_yscale("log")  # Utilizar escala logarítmica para el eje y

# Histograma de la variable "pz"
axs[2].hist(data["pz"], bins=25, color='orange', alpha=0.7)
axs[2].set_xlabel("pz")
axs[2].set_ylabel("Frecuencia")
axs[2].set_title("Histograma de pz")
axs[2].set_yscale("log")  # Utilizar escala logarítmica para el eje y

# Ajustar los espacios entre subplots
plt.tight_layout()

# Obtener el nombre del archivo sin la extensión
nombre_archivo = "histogramas_px_py_pz_region_0-70_50m"

# Guardar la figura en una imagen PNG con el nuevo nombre
plt.savefig(nombre_archivo + ".png")

# Mostrar la figura en pantalla
plt.show()
