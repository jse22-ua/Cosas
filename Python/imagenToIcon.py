from PIL import Image

def convertir_a_icono(ruta_imagen, ruta_icono, tamaño=(32, 32)):
    # Abrir la imagen con Pillow
    imagen = Image.open(ruta_imagen)

    # Redimensionar la imagen al tamaño del icono
    imagen = imagen.resize(tamaño)

    # Guardar la imagen como un archivo de icono (.ico)
    imagen.save(ruta_icono, format="ICO")

if __name__ == "__main__":
    # Rutas de la imagen de entrada y el icono de salida
    ruta_imagen_entrada = "logo.jpg"
    ruta_icono_salida = "logo.ico"

    # Tamaño del icono (ancho, alto)
    tamaño_icono = (64, 64)

    # Convertir la imagen a un icono
    convertir_a_icono(ruta_imagen_entrada, ruta_icono_salida, tamaño_icono)

    print(f"La imagen se ha convertido a un icono y se ha guardado en {ruta_icono_salida}.")
