import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo original
data = pd.read_csv("filter_70-90deg_086400_100m.csv", delimiter="\s+")

# Filtrar los valores de la variable "z" que sean menores a 2000 en valor absoluto
filtered_data = data[data["z"].abs() < 2000]

# Guardar los datos filtrados en un nuevo archivo CSV
filtered_data.to_csv("datos_filtrados.csv", index=False)

# Crear una figura con tres subplots para los histogramas
fig, axs = plt.subplots(3, 1, figsize=(8, 10))

# Histograma de la variable "px"
axs[0].hist(filtered_data["px"], bins=25, color='blue', alpha=0.7)
axs[0].set_xlabel("px")
axs[0].set_ylabel("Frecuencia")
axs[0].set_title("Histograma de px")
#axs[0].set_yscale("log")  # Utilizar escala logarítmica para el eje y

# Histograma de la variable "py"
axs[1].hist(filtered_data["py"], bins=25, color='green', alpha=0.7)
axs[1].set_xlabel("py")
axs[1].set_ylabel("Frecuencia")
axs[1].set_title("Histograma de py")
#axs[1].set_yscale("log")  # Utilizar escala logarítmica para el eje y

# Histograma de la variable "pz"
axs[2].hist(filtered_data["pz"], bins=25, color='orange', alpha=0.7)
axs[2].set_xlabel("pz")
axs[2].set_ylabel("Frecuencia")
axs[2].set_title("Histograma de pz")
#axs[2].set_yscale("log")  # Utilizar escala logarítmica para el eje y

# Ajustar los espacios entre subplots
plt.tight_layout()

# Mostrar la figura en pantalla
plt.show()

# Crear un histograma de los CorsikaId
plt.hist(filtered_data["CorsikaId"], bins=20, color='purple', alpha=0.7)
plt.xlabel("CorsikaId")
plt.ylabel("Frecuencia")
plt.title("Histograma de CorsikaId")

# Mostrar el histograma en pantalla
plt.show()
