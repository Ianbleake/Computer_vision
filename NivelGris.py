#escala de gris
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

imagen = cv.imread("Grises\chicles.jpeg")
resultante = cv.resize(imagen, (1024, 720))
[M, N, L] = resultante.shape

escalaGrises = np.zeros([M, N])
cv.imshow("Imagen original", resultante)
resultante = np.array(resultante, dtype=(float))
escalaGrises = np.array(escalaGrises, dtype=(float))
resultante = pow(resultante.astype(np.float64) / 255, 1) * 255

for x in range(M):
    for y in range(N):
        for z in range(L):
            escalaGrises[x, y] = resultante[x, y, 0] * 0.299 + resultante[x, y, 1] * 0.587 + resultante[x, y, 2] * 0.114

escalaGrises = np.array(escalaGrises, dtype=(np.uint8))
cv.imshow("Escala de grises", escalaGrises)
cv.waitKey(0)
cv.destroyAllWindows()

# Obtener valores de intensidad y comparar
intensidades = escalaGrises.flatten()  # Aplanar la matriz de intensidades
print("Valores de intensidad:", intensidades)

# Comparar los valores de intensidad (puedes utilizar cualquier métrica de comparación)
# Por ejemplo, imprimir el valor máximo y mínimo
print("Valor máximo de intensidad:", np.max(intensidades))
print("Valor mínimo de intensidad:", np.min(intensidades))

# También puedes calcular la media, la desviación estándar, etc.
print("Valor medio de intensidad:", np.mean(intensidades))
print("Desviación estándar de intensidad:", np.std(intensidades))

# Histograma de los valores de intensidad
plt.hist(intensidades, bins=256, range=(0, 256), density=True, color='gray', alpha=0.7)
plt.title('Histograma de Intensidades')
plt.xlabel('Intensidad')
plt.ylabel('Frecuencia')
plt.show()