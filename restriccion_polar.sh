#!/bin/bash

# Obtener la ubicación del directorio desde la bandera -d o --directorio
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -d|--directorio) directorio="$2"; shift ;;
        *) echo "Opción inválida: $1"; exit 1 ;;
    esac
    shift
done

# Verificar si se proporcionó la ubicación del directorio
if [ -z "$directorio" ]; then
    echo "Debes proporcionar la ubicación del directorio con la opción -d/--directorio."
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
        # Modificar las líneas 14 y 15 del archivo
        sed -i '14s/.*/-90/' "$archivo"
        sed -i '15s/.*/90/' "$archivo"
        echo "Archivo modificado: $archivo"
    fi
done
