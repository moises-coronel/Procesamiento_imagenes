import cv2
import numpy as np

# Cargando las imágenes
img1 = cv2.imread('img1.bmp')
img2 = cv2.imread('img2.bmp')
img3 = cv2.imread('img3.bmp')

# Sumando las imágenes
img_Result = cv2.add(img1, img2)
img_Result = cv2.add(img_Result, img3)

# Mostrar imagen resultante
cv2.imshow('Imagen Sumada', img_Result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Encontrar contornos de las figuras geométricas
gray = cv2.cvtColor(img_Result, cv2.COLOR_BGR2GRAY)
contornos, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterar sobre los contornos y obtener información de cada figura geométrica
for i, contorno in enumerate(contornos):
    # Calcular el área de la figura
    area = cv2.contourArea(contorno)

    # Calcular el perímetro de la figura
    perimetro = cv2.arcLength(contorno, True)

    # Calcular el centroide de la figura
    moments = cv2.moments(contorno)
    centroid_x = int(moments['m10'] / moments['m00'])
    centroid_y = int(moments['m01'] / moments['m00'])

    # Imprimir los resultados
    print(f"Figura {i+1}:")
    print(f"Area: {area} pixeles cuadrados")
    print(f"Perimetro: {perimetro} pixeles")
    print(f"Centroide: ({centroid_x}, {centroid_y})\n")
