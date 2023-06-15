import pandas as pd
import matplotlib.pyplot as plt
import random

# Generar valores aleatorios para n y m
n = 70
m = 90

# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("70-90deg-rpol-izq_001800.csv", delimiter="\s+")

# Filtrar los datos con "x" y "y" menores o iguales a 1000
filtered_data = data[(data["x"].abs() <= 500) & (data["y"].abs() <= 500)]

# Realizar un plot de dispersión entre las columnas "x" y "y"
plt.scatter(filtered_data["x"], filtered_data["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Distancia al detector, ángulos entre 70° a 90°")

# Obtener el nombre del archivo sin la extensión
nombre_archivo = f"{n}-{m}deg_0001800"

# Guardar el gráfico en una imagen PNG con el nuevo nombre
#plt.savefig(nombre_archivo + ".png")
plt.savefig("filter-" + nombre_archivo + "_500m_rest_pol_izq.png")

# Hacer la preselección de datos según CorsikaId y prm_theta
preseleccion = filtered_data[filtered_data["prm_theta"] >= 0]

# Crear tablas distintas según CorsikaId
tablas_por_corsika_id = preseleccion.groupby("CorsikaId")

# Guardar las tablas resultantes1 en un archivo de texto
with open("filter_head_70-90deg_001800_500m_rest_pol_izq.txt", "w") as file:
    for corsika_id, tabla in tablas_por_corsika_id:
        file.write(f"Tabla para CorsikaId {corsika_id}:\n")
        file.write(tabla.to_string())
        file.write("\n\n")
