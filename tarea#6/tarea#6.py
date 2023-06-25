import cv2

# Función para realizar la detección de movimiento
def detectar_movimiento(video_path):
    # Leer el video
    video = cv2.VideoCapture(video_path)

    # Obtener el primer frame
    ret, frame_anterior = video.read()

    # Convertir a escala de grises
    frame_anterior_gris = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)
    #obteniendo ultimo frame sin movimiento
    while True:
        ret, frame_actual = video.read()
        if not ret:
            break
        frame_anterior = frame_actual
        frame_anterior_gris = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Frame anterior en escala de grises sin movimiento ", frame_anterior_gris)
    cv2.waitKey(0)

    # Liberar los recursos y cerrar las ventanas
    #video.release()
    cv2.destroyAllWindows()
    
    # Volver a cargar el video para comenzar desde el principio
    video = cv2.VideoCapture(video_path)
    while True:
        # Leer el siguiente frame
        ret, frame_actual = video.read()

        if not ret:
            break

        # Convertir a escala de grises
        frame_actual_gris = cv2.cvtColor(frame_actual, cv2.COLOR_BGR2GRAY)

        # Calcular la diferencia absoluta entre los frames
        diferencia = cv2.absdiff(frame_actual_gris, frame_anterior_gris)

        # Aplicar umbral para obtener una imagen binaria
        umbral = 12
        _, imagen_umbral = cv2.threshold(diferencia, umbral, 255, cv2.THRESH_BINARY)

        # Aplicar operaciones morfológicas para eliminar ruido
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        imagen_morfo = cv2.morphologyEx(imagen_umbral, cv2.MORPH_OPEN, kernel)

        # Mostrar la imagen resultante
        cv2.imshow("Deteccion de movimiento", imagen_morfo)

        # Salir del bucle si se presiona la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Actualizar el frame anterior
        frame_anterior_gris = frame_actual_gris

    # Liberar los recursos y cerrar las ventanas
    video.release()
    cv2.destroyAllWindows()

# Ruta del archivo de video
video_path = "./tarea#6/video1.avi"

# Llamar a la función para realizar la detección de movimiento
detectar_movimiento(video_path)
