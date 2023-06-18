import cv2
import numpy as np

# Cargar la imagen
image = cv2.imread("img.bmp")

# Dividir la imagen en canales RGB
blue, green, red = cv2.split(image)

# Segmentación por color
blue_mask = cv2.inRange(blue, 200, 255)
green_mask = cv2.inRange(green, 200, 255)
red_mask = cv2.inRange(red, 200, 255)

# Encontrar contornos de los objetos
blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extraer ROIs y visualizarlos
for contour in red_contours:
    x, y, w, h = cv2.boundingRect(contour)
    roi = image[y:y+h, x:x+w]
    cv2.imshow("ROI Red", roi)
    cv2.moveWindow("ROI Red",300,300)
    
    
for contour in blue_contours:
    x, y, w, h = cv2.boundingRect(contour)
    roi = image[y:y+h, x:x+w]
    cv2.imshow("ROI Blue", roi)
    cv2.moveWindow("ROI Blue",500,300)
    

for contour in green_contours:
    x, y, w, h = cv2.boundingRect(contour)
    roi = image[y:y+h, x:x+w]
    cv2.imshow("ROI Green", roi)
    cv2.moveWindow("ROI Green",700,300)
    cv2.waitKey(0)



cv2.destroyAllWindows()
