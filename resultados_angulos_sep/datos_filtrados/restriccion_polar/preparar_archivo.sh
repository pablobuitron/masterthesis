#!/bin/bash

# Parsear argumento de la bandera
while getopts ":f:" flag; do
    case "${flag}" in
        f) file=${OPTARG};;
        *) echo "Uso: $0 -f archivo.shw"; exit 1;;
    esac
done

# Verificar si se proporcionó un archivo
if [ -z "$file" ]; then
    echo "Debe proporcionar un archivo con la bandera -f"
    exit 1
fi

# Verificar si el archivo existe
if [ ! -f "$file" ]; then
    echo "El archivo $file no existe"
    exit 1
fi

# Nombre del archivo CSV resultante
csv_file="${file%.shw}.csv"

# Eliminar las primeras 4 líneas y guardar el resultado en un archivo temporal
tail -n +5 "$file" | cut -c5- > temp_file.txt

# Eliminar la última línea del archivo temporal
sed '$d' temp_file.txt > "$csv_file"

# Eliminar el archivo temporal
rm temp_file.txt

echo "Archivo convertido exitosamente a $csv_file"

# Cambiar extensión del archivo original a .csv
mv "$file" "${file%.shw}.csv"
