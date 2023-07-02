import cv2
import numpy as np

def segmentar_objeto(imagen):
    # Binarización
    umbral = 130
    _, imagen_binaria = cv2.threshold(imagen, umbral, 255, cv2.THRESH_BINARY)

    # Aplicar operaciones morfológicas
    kernel_cerrar = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    imagen_cerrada = cv2.morphologyEx(imagen_binaria, cv2.MORPH_CLOSE, kernel_cerrar, iterations=1)

    kernel_abrir = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    imagen_abierta = cv2.morphologyEx(imagen_cerrada, cv2.MORPH_OPEN, kernel_abrir, iterations=1)

    kernel_erosion = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
    imagen_segmentada = cv2.erode(imagen_abierta, kernel_erosion, iterations=2)

    # Suavizado de bordes
    imagen_suavizada = cv2.GaussianBlur(imagen_segmentada, (5, 5), 0)
    # Realzado de bordes
    #imagen_realzada = cv2.Laplacian(imagen_segmentada, cv2.CV_8U, ksize=3)

    # Mostrar las imágenes resultantes
    cv2.imshow("Imagen binarizada", imagen_binaria)
    cv2.waitKey(0)
    cv2.imshow("Imagen cerrada", imagen_cerrada)
    cv2.waitKey(0)
    cv2.imshow("Imagen abierta", imagen_abierta)
    cv2.waitKey(0)
    cv2.imshow("Imagen segmentada", imagen_segmentada)
    cv2.waitKey(0)
    cv2.imshow("Imagen suavizada", imagen_suavizada)
    cv2.waitKey(0)
    #cv2.imshow("Imagen suavizada", imagen_realzada)
    #cv2.waitKey(0)
   

    return imagen_segmentada

# Cargar la imagen de entrada
imagen_path = "./tarea#7/imagen.jpg"
imagen = cv2.imread(imagen_path)
# Convertir la imagen a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Cargar la imagen de fondo
fondo_path = "./tarea#7/fondo.jpg"
fondo = cv2.imread(fondo_path)

# Asegurarse de que la imagen de fondo y la imagen segmentada tengan las mismas dimensiones
fondo = cv2.resize(fondo, (imagen.shape[1], imagen.shape[0]))

# Segmentar el objeto de interés
imagen_segmentada = segmentar_objeto(imagen_gris)

# Invertir la máscara
mascara = cv2.bitwise_not(imagen_segmentada)

# Aplicar la máscara a la imagen original en color
imagen_color = cv2.bitwise_and(imagen, imagen, mask=mascara)

# Aplicar la máscara invertida a la imagen de fondo en color
fondo_segmentado = cv2.bitwise_and(fondo, fondo, mask=imagen_segmentada)

# Combinar la imagen segmentada en color y el fondo segmentado en color
imagen_final = cv2.add(imagen_color, fondo_segmentado)
# Mostrar la imagen resultante
cv2.imshow("Imagen segmentada con fondo", imagen_final)
cv2.waitKey(0)
cv2.destroyAllWindows()


