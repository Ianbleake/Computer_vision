import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
#Prewitt
def convolucion(imagen, kernel):
    return cv2.filter2D(imagen, -1, kernel)

imagen = cv2.imread('fotos_9\DSC_0237.JPG', cv2.IMREAD_GRAYSCALE)

kernel_prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])

kernel_prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

# Aplicar el operador Prewitt
prewitt_x = convolucion(imagen, kernel_prewitt_x)
prewitt_y = convolucion(imagen, kernel_prewitt_y)
prewitt_magnitud = np.sqrt(prewitt_x**2 + prewitt_y**2)

# Mostrar imágenes
plt.figure(figsize=(10, 5))

plt.subplot(231), plt.imshow(imagen, cmap='gray'), plt.title('Original')
plt.subplot(232), plt.imshow(prewitt_x, cmap='gray'), plt.title('Prewitt en X')
plt.subplot(233), plt.imshow(prewitt_y, cmap='gray'), plt.title('Prewitt en Y')
plt.subplot(234), plt.imshow(prewitt_magnitud, cmap='gray'), plt.title('Prewitt Magnitud')

plt.show()
"""

"""
#Sobel
def convolucion(imagen, kernel):
    return cv2.filter2D(imagen, -1, kernel)

# Cargar la imagen
imagen = cv2.imread('fotos_9\DSC_0237.JPG', cv2.IMREAD_GRAYSCALE)

# Definir el kernel Sobel en la dirección x
kernel_sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

# Definir el kernel Sobel en la dirección y
kernel_sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# Aplicar el operador Sobel
sobel_x = convolucion(imagen, kernel_sobel_x)
sobel_y = convolucion(imagen, kernel_sobel_y)
sobel_magnitud = np.sqrt(sobel_x**2 + sobel_y**2)

# Mostrar imágenes
plt.figure(figsize=(10, 5))

plt.subplot(231), plt.imshow(imagen, cmap='gray'), plt.title('Original')
plt.subplot(232), plt.imshow(sobel_x, cmap='gray'), plt.title('Sobel en X')
plt.subplot(233), plt.imshow(sobel_y, cmap='gray'), plt.title('Sobel en Y')
plt.subplot(234), plt.imshow(sobel_magnitud, cmap='gray'), plt.title('Sobel Magnitud')

plt.show()
"""
"""
#Isotropico Frei-chen
def convolucion(imagen, kernel):
    return cv2.filter2D(imagen, -1, kernel)

# Cargar la imagen
imagen = cv2.imread('fotos_9\DSC_0237.JPG', cv2.IMREAD_GRAYSCALE)

# Definir el kernel de Frei-Chen para la dirección x
kernel_frei_chen_x = np.array([[1, np.sqrt(2), 1], [0, 0, 0], [-1, -np.sqrt(2), -1]])

# Definir el kernel de Frei-Chen para la dirección y
kernel_frei_chen_y = np.array([[-1, 0, 1], [-np.sqrt(2), 0, np.sqrt(2)], [-1, 0, 1]])

# Aplicar el operador de Frei-Chen
frei_chen_x = convolucion(imagen, kernel_frei_chen_x)
frei_chen_y = convolucion(imagen, kernel_frei_chen_y)
frei_chen_magnitud = np.sqrt(frei_chen_x**2 + frei_chen_y**2)

# Mostrar imágenes
plt.figure(figsize=(10, 5))

plt.subplot(231), plt.imshow(imagen, cmap='gray'), plt.title('Original')
plt.subplot(232), plt.imshow(frei_chen_x, cmap='gray'), plt.title('Frei-Chen en X')
plt.subplot(233), plt.imshow(frei_chen_y, cmap='gray'), plt.title('Frei-Chen en Y')
plt.subplot(234), plt.imshow(frei_chen_magnitud, cmap='gray'), plt.title('Frei-Chen Magnitud')

plt.show()
"""
"""
#Kirch
import cv2
import numpy as np

# Función para aplicar el operador de Kirsch en una dirección específica
def kirsch_operator(imagen, direction):
    kernel = np.array([
        [-3, -3, 5],
        [-3, 0, 5],
        [-3, -3, 5]
    ]) if direction == 1 else np.array([
        [-3, 5, 5],
        [-3, 0, 5],
        [-3, -3, -3]
    ]) if direction == 2 else np.array([
        [5, 5, 5],
        [-3, 0, -3],
        [-3, -3, -3]
    ]) if direction == 3 else np.array([
        [5, 5, -3],
        [5, 0, -3],
        [-3, -3, -3]
    ]) if direction == 4 else np.array([
        [5, -3, -3],
        [5, 0, -3],
        [5, -3, -3]
    ]) if direction == 5 else np.array([
        [-3, -3, -3],
        [5, 0, -3],
        [5, 5, -3]
    ]) if direction == 6 else np.array([
        [-3, -3, -3],
        [-3, 0, -3],
        [5, 5, 5]
    ]) if direction == 7 else np.array([
        [-3, -3, -3],
        [-3, 0, 5],
        [-3, 5, 5]
    ])
    
    return cv2.filter2D(imagen, -1, kernel)

# Cargar la imagen
imagen = cv2.imread('fotos_9\DSC_0237.JPG', cv2.IMREAD_GRAYSCALE)

# Redimensionar la imagen a 500x700px
imagen_redimensionada = cv2.resize(imagen, (700, 500))

# Aplicar el operador de Kirsch en cada dirección
kirsch_respuestas = [kirsch_operator(imagen_redimensionada, i) for i in range(1, 9)]

# Obtener la magnitud máxima entre todas las respuestas
kirsch_magnitud = np.max(kirsch_respuestas, axis=0)

# Mostrar la imagen resultante redimensionada
cv2.imshow('Kirsch Magnitud', kirsch_magnitud)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Guardar imágenes resultantes
for i, respuesta in enumerate(kirsch_respuestas):
    cv2.imwrite(f'kirsch_respuesta_{i+1}.jpg', respuesta)
"""

