#####Este script corre todos los archicos go generados luego de hacer do_sims.sh, para usarlo se corre el comando: "./rungo.sh proyecto"

#!/bin/bash

# Ruta al directorio donde se encuentran los archivos de script
directorio="/home/pablo/Desktop/mastertesis/lago-corsika/corsika-77402/run/"

# Obtener la palabra como argumento al ejecutar el script
if [ $# -eq 0 ]; then
  echo "Debe proporcionar el nombre del proyecto como argumento."
  exit 1
fi

proyecto="$1"

# Iterar a través de los archivos en el directorio
for archivo in "$directorio"/go-"$proyecto"-*.sh; do
  if [[ -f "$archivo" ]]; then
    echo "Ejecutando $archivo..."
    chmod +x "$archivo"  # Dar permisos de ejecución al archivo si es necesario
    "$archivo"          # Ejecutar el archivo de script
    echo "Finalizado $archivo."
    echo
  fi
done
