import pandas as pd

# Cargar los datos desde el archivo con separación por espacios
data = pd.read_csv("fluxquito1min0deg.csv", delimiter="\s+")

# Calcular el valor máximo en valor absoluto de la variable "y"
max_abs_y = data["y"].abs().max()

print("Valor máximo en valor absoluto de 'y':", max_abs_y)
