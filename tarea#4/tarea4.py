import cv2
import numpy as np

def calcular_tamano_objeto(imagen, tamano_real_objeto_ancho, tamano_real_objeto_alto):
    # Leer la imagen y convertirla a escala de grises
    img = cv2.imread(imagen)
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Aplicar umbralización para obtener una imagen binaria
    _, binaria = cv2.threshold(gris, 127, 255, cv2.THRESH_BINARY)

    # Encontrar contornos en la imagen binaria
    contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Encontrar el contorno más grande (que debería ser el objeto de interés)
    contorno_objeto = max(contornos, key=cv2.contourArea)

    # Calcular los momentos del contorno
    momentos = cv2.moments(contorno_objeto)

    # Calcular el centroide del objeto
    centroide_x = int(momentos["m10"] / momentos["m00"])
    centroide_y = int(momentos["m01"] / momentos["m00"])

    # Calcular el área del objeto
    area = cv2.contourArea(contorno_objeto)

    # Calcular el rectángulo delimitador del objeto
    x, y, ancho, alto = cv2.boundingRect(contorno_objeto)

    # Calcular el tamaño del objeto en la imagen (factor de aumento)
    

    # Dimensiones del objeto real en milimetros
    ##tamano_real_objeto_ancho = 185 #mm
    ##tamano_real_objeto_alto = 125 #mm
    #distancia de camara a objetos en milimetros
    distancia_camara_obj=300
    # Calcular el factor de aumento
    factor_aumento_ancho = tamano_real_objeto_ancho / ancho
    factor_aumento_alto = tamano_real_objeto_alto / alto
    # Calcular la distancia focal
    distancia_focal_ancho=factor_aumento_ancho*distancia_camara_obj
    distancia_focal_alto = factor_aumento_alto*distancia_camara_obj
    # Dibujar el contorno y el centroide en la imagen original
    cv2.drawContours(img, [contorno_objeto], -1, (0, 255, 0), 2)
    cv2.circle(img, (centroide_x, centroide_y), 5, (0, 0, 255), -1)

    # Mostrar los resultados
    cv2.imshow("Imagen con contorno y centroide", img)
    cv2.waitKey(0)

    # Imprimir los resultados
    print("Alto imagen: {}      Alto real (mm):{}" .format(alto,tamano_real_objeto_alto))
    print("Ancho imagen: {}     Ancho real (mm): {}" .format(ancho,tamano_real_objeto_ancho))
    print("Area:", area)
    print("Centroide: ({}, {})".format(centroide_x, centroide_y))
    print("Factor de aumento (alto):", factor_aumento_alto)
    print("Factor de aumento (ancho):", factor_aumento_ancho)
    print("Distancia de camara a objeto (mm): 300")
    print("Distancia focal (alto en mm): ", distancia_focal_alto)
    print("Distancia focal (ancho en mm): ", distancia_focal_ancho)

    # Cerrar las ventanas
    cv2.destroyAllWindows()

# Ejemplo de uso
imagenes = ["img1.jpg","img2.jpg","img3.jpg"]

print("------Imagen 1:------")
calcular_tamano_objeto(imagenes[0],185,125)
print("------Imagen 2:------")
calcular_tamano_objeto(imagenes[1],120,120)
print("------Imagen 3:------")
calcular_tamano_objeto(imagenes[2],195,160)
