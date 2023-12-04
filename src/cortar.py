import cv2

# Carregue a imagem
image = cv2.imread("foto-perfil.jpeg")

# Defina as coordenadas de início e fim para cortar a imagem
x_inicio, x_fim = 74, 95
y_inicio, y_fim = 102, 109  # Corrigido para garantir que y_inicio < y_fim

# Corte a região desejada da imagem
regiao_cortada = image[x_inicio:y_inicio, x_fim:y_fim]

print(regiao_cortada)
print(regiao_cortada.shape)

# Exiba a imagem original e a região cortada
cv2.imshow("Imagem Original", image)
cv2.imshow("Região Cortada", regiao_cortada)
cv2.waitKey(0)
cv2.destroyAllWindows()
