import os
import shutil
import glob

ruta_origen = "D:\\Documentos\\0.-Universidad Ingeniería Informática\\TFG\\proyecto\\src\\resources\\CBIS-DDSM"
rutas_archivos = glob.glob(ruta_origen + "\\*")

def buscar_y_copiar_imagenes(ruta):
    # Lista para almacenar las rutas de las imágenes .dcm encontradas
    imagenes = []

    # Buscamos archivos de imagen (dcm) en la ruta de origen y subdirectorios
    for root, dirs, files in os.walk(ruta):
        for file in files:
            if file.endswith('.dcm'):
                imagenes.append(os.path.join(root, file))

    print("Imágenes encontradas:")
    for imagen in imagenes:
        print(imagen)
        # Copiar la imagen a la ruta destino
        shutil.copy(imagen, ruta)
        print("Imagen copiada a:", ruta)


# Iteramos sobre todas las rutas encontradas
for ruta in rutas_archivos:
    buscar_y_copiar_imagenes(ruta)
