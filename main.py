import cv2

# Activar la cámara
# El índice 0 corresponde a la cámara web por defecto.
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error: No se puede abrir la cámara.")
    exit()

print("Cámara activada. Presiona 'q' en la ventana para salir.")

# Bucle principal para procesar cada fotograma del video
while True:
    # Leer un fotograma de la cámara
    ret, frame = cam.read()
    if not ret:
        print("No se pudo recibir el fotograma. Saliendo...")
        break

    # --- INICIO DE LA TAREA 'PREPROCESAMIENTO' ---
    # Tarea: Convertir el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # --- FIN DE LA TAREA 'PREPROCESAMIENTO' ---

    # Mostrar el fotograma original en una ventana
    cv2.imshow("Original - Proyecto Grupal", frame)

    # Mostrar el fotograma preprocesado (en gris) en otra ventana
    cv2.imshow("Preprocesamiento (Gris)", gris)

    # Esperar por la tecla 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos al finalizar
print("Cerrando la aplicación...")
cam.release()
cv2.destroyAllWindows()

# Proyecto de IA colaborativo MARIOOO

def reconocer_patrones(datos):
    """Simula el reconocimiento de patrones o clasificación."""
    print("Realizando reconocimiento de patrones...")
    # Aquí iría el código real de reconocimiento (ej. modelo de ML, detección de objetos)
    if datos:
        return "Patrón detectado: Cara humana"
    return "No se detectaron patrones significativos"

def main():
    # Ejemplo de uso de reconocimiento
    # resultado = reconocer_patrones(True) # Simula datos de entrada
    # print(f"Resultado del reconocimiento: {resultado}")
    pass

if __name__ == "__main__":
    main()
