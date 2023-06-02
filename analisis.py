import pandas as pd
import matplotlib.pyplot as plt
import random

# Generar valores aleatorios para n y m
n = random.randint(0, 100)
m = random.randint(0, 100)

# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("fluxquito3min0deg.csv", delimiter="\s+")

# Realizar un plot de dispersión entre las columnas "x" y "y"
plt.scatter(data["x"], data["y"])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Distancia al detector")

# Obtener el nombre del archivo sin la extensión
nombre_archivo = f"{n}sec{m}deg"

# Guardar el gráfico en una imagen PNG con el nuevo nombre
plt.savefig(nombre_archivo + ".png")

# Hacer la preselección de datos según CorsikaId y prm_theta
preseleccion = data[data["prm_theta"] >= 70]

# Crear tablas distintas según CorsikaId
tablas_por_corsika_id = preseleccion.groupby("CorsikaId")

# Imprimir las tablas resultantes
for corsika_id, tabla in tablas_por_corsika_id:
    print(f"Tabla para CorsikaId {corsika_id}:")
    print(tabla)
    print("\n")
