import cv2

def mostrar_interfaz(frame, gris, bordes):
    """Muestra las diferentes ventanas del proyecto."""
    cv2.imshow("Original - Proyecto Grupal", frame)
    cv2.imshow("Preprocesamiento (Gris)", gris)
    cv2.imshow("Preprocesamiento (Bordes - Canny)", bordes)

def reconocer_patrones(datos):
    """Simula el reconocimiento de patrones o clasificación."""
    print("Realizando reconocimiento de patrones...")
    # Aquí iría el código real de reconocimiento (ej. modelo de ML, detección de objetos)
    if datos:
        return "Patrón detectado: Cara humana"
    return "No se detectaron patrones significativos"

def main():
    # Activar la cámara
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: No se puede abrir la cámara.")
        return

    print("Cámara activada. Presiona 'q' en la ventana para salir.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("No se pudo recibir el fotograma. Saliendo...")
            break

        # --- INICIO DE LA TAREA 'PREPROCESAMIENTO' ---
        # Convertir el frame a escala de grises
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Aplicar filtro Canny para detección de bordes
        bordes = cv2.Canny(gris, 100, 200)
        # --- FIN DE LA TAREA 'PREPROCESAMIENTO' ---

        # Mostrar la interfaz con todas las ventanas
        mostrar_interfaz(frame, gris, bordes)

        # Manejo de teclado: salir con 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Liberar recursos al finalizar
    print("Cerrando la aplicación...")
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
