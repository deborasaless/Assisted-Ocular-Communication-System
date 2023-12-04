# import the necessary packages
from imutils import face_utils
import dlib
import cv2


#################
# Esse código aplica os landmarkings na face e corta a região do olho esquerdo
#################

# Vamos inicializar um detector de faces (HOG) para então
# fazer a predição dos pontos da nossa face.
# p é o diretório do nosso modelo já treinado, neste caso, ele está no mesmo diretório
# que este script
p = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(p)

# Obtendo nossa imagem através da webcam e transformando-a preto e branco.
image = cv2.imread("dataset/foto-perfil.jpeg")
image_landmarking = cv2.imread("dataset/foto-perfil.jpeg")

gray = cv2.cvtColor(image_landmarking, cv2.COLOR_BGR2GRAY)

# Detectando as faces em preto e branco.
rects = detector(gray, 0)

# para cada face encontrada, encontre os pontos de interesse.
for (i, rect) in enumerate(rects):
    # faça a predição e então transforme isso em um array do numpy.
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)

    print(shape)

    shape_x = shape[:, 0]
    shape_y = shape[:, 1]

    print(shape_x)
    print(shape_y)

    # desenhe na imagem cada coordenada (x, y) que foi encontrado.
    for (x, y) in shape:
        cv2.circle(image_landmarking, (x, y), 2, (0, 255, 0), -1)

    print("DESENHOU\n")

    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

    print(image.shape)

    # Verifique se os índices estão dentro dos limites da imagem
    x_inicio = max(0, int(shape_x[36]))
    x_fim = min(image_landmarking.shape[1], int(shape_x[39]))
    y_inicio = max(0, int(shape_y[37]))
    y_fim = min(image_landmarking.shape[0], int(shape_y[41]))

    left_eye = image[y_inicio:y_fim, x_inicio:x_fim]

    print("CORTOU\n")

    # Exibir as regiões dos olhos com o centro da pupila
    cv2.imshow("Output", image_landmarking)
    cv2.imshow("left eye", left_eye)
    cv2.imwrite("left_eye.jpg", left_eye)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("output")

cv2.destroyAllWindows()
