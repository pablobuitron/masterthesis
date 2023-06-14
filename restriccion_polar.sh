#!/bin/bash

# Obtener las opciones de las banderas usando getopts
while getopts "d:m:n:" opcion; do
    case $opcion in
        d)
            directorio=$OPTARG
            ;;
        m)
            numero_linea_14=$OPTARG
            ;;
        n)
            numero_linea_15=$OPTARG
            ;;
        \?)
            echo "Opción inválida: -$OPTARG" >&2
            exit 1
            ;;
    esac
done

# Verificar si se proporcionó la ubicación del directorio
if [ -z "$directorio" ]; then
    echo "Debes proporcionar la ubicación del directorio con la opción -d."
    exit 1
fi

# Verificar si el directorio existe
if [ ! -d "$directorio" ]; then
    echo "El directorio especificado no existe."
    exit 1
fi

# Recorrer todos los archivos .run en el directorio objetivo
for archivo in "$directorio"/*.run; do
    # Verificar si el archivo es legible
    if [[ -r "$archivo" ]]; then
        # Modificar las líneas 14 y 15 del archivo con los números de reemplazo proporcionados
        sed -i "14s/.*/$numero_linea_14/" "$archivo"
        sed -i "15s/.*/$numero_linea_15/" "$archivo"
        echo "Archivo modificado: $archivo"
    fi
done
