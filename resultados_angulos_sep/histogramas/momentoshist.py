import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("70-90deg_086400_100m.csv", delimiter="\s+")

# Crear una figura con tres subplots para los histogramas
fig, axs = plt.subplots(3, 1, figsize=(8, 10))

# Histograma de la variable "px"
counts_px, bins_px, _ = axs[0].hist(data["px"], bins=25, color='blue', alpha=0.7)
axs[0].hist(data["px"], bins=25, color='blue', alpha=0.7)
axs[0].set_xlabel("px")
axs[0].set_ylabel("Frecuencia")
axs[0].set_title("Histograma de px")
axs[0].set_yscale("log")  # Utilizar escala logarítmica para el eje y
# Calcular las barras de error
errors_px = np.sqrt(counts_px)

# Mostrar las barras de error
axs[0].errorbar(
    x=(bins_px[:-1] + bins_px[1:]) / 2,
    y=counts_px,
    yerr=errors_px,
    fmt='none',
    color='black'
)

# Histograma de la variable "py"
counts_py, bins_py, _ = axs[1].hist(data["py"], bins=25, color='green', alpha=0.7)
axs[1].hist(data["py"], bins=25, color='green', alpha=0.7)
axs[1].set_xlabel("py")
axs[1].set_ylabel("Frecuencia")
axs[1].set_title("Histograma de py")
axs[1].set_yscale("log")  # Utilizar escala logarítmica para el eje y
# Calcular las barras de error
errors_py = np.sqrt(counts_py)

# Mostrar las barras de error
axs[1].errorbar(
    x=(bins_py[:-1] + bins_py[1:]) / 2,
    y=counts_py,
    yerr=errors_py,
    fmt='none',
    color='black'
)
# Histograma de la variable "pz"
counts_pz, bins_pz, _ = axs[2].hist(data["pz"], bins=25, color='orange', alpha=0.7)
axs[2].hist(data["pz"], bins=25, color='orange', alpha=0.7)
axs[2].set_xlabel("pz")
axs[2].set_ylabel("Frecuencia")
axs[2].set_title("Histograma de pz")
axs[2].set_yscale("log")  # Utilizar escala logarítmica para el eje y
# Calcular las barras de error
errors_pz = np.sqrt(counts_pz)

# Mostrar las barras de error
axs[2].errorbar(
    x=(bins_pz[:-1] + bins_pz[1:]) / 2,
    y=counts_pz,
    yerr=errors_pz,
    fmt='none',
    color='black'
)
# Ajustar los espacios entre subplots
plt.tight_layout()

# Obtener el nombre del archivo sin la extensión
nombre_archivo = "histogramas_px_py_pz_region_70-90_100m"

# Guardar la figura en una imagen PNG con el nuevo nombre
plt.savefig(nombre_archivo + ".png")

# Mostrar la figura en pantalla
plt.show()
