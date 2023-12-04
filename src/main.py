import dlib
import cv2
import numpy as np

#################
# Esse código aplica os landmarkings na face e corta a região do olho esquerdo e identifica a pupila
#################




def detect_and_crop_eyes(image_path):
    # Inicializar o detector de face
    detector = dlib.get_frontal_face_detector()
    
    # Inicializar o preditor de landmarks
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    
    # Carregar a imagem
    img = cv2.imread(image_path)
    
    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Detectar faces na imagem
    faces = detector(gray)
    
    # Para cada face encontrada, extrair landmarks
    for face in faces:
        landmarks = predictor(gray, face)
        
        # Extrair coordenadas dos olhos
        left_eye_start = 36
        left_eye_end = 41
        
        left_eye_pts = np.array([(landmarks.part(i).x, landmarks.part(i).y) for i in range(left_eye_start, left_eye_end + 1)])
        
        # Calcular as coordenadas da caixa delimitadora dos olhos
        left_eye_box = cv2.boundingRect(left_eye_pts)
        
        # Recortar a região dos olhos
        left_eye_region = img[left_eye_box[1]:left_eye_box[1] + left_eye_box[3],
                              left_eye_box[0]:left_eye_box[0] + left_eye_box[2]]
        
        
        # Converter a região dos olhos para escala de cinza
        left_eye_gray = cv2.cvtColor(left_eye_region, cv2.COLOR_BGR2GRAY)
        
        # Aplicar a detecção de bordas e encontrar a pupila
        _, left_eye_thresh = cv2.threshold(left_eye_gray, 30, 255, cv2.THRESH_BINARY_INV)
        
        # Encontrar contornos
        left_contours, _ = cv2.findContours(left_eye_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Encontrar o centro da pupila
        if left_contours:
            left_pupil_center = tuple(np.mean(left_contours[0], axis=0, dtype=int).flatten())
            cv2.circle(left_eye_region, left_pupil_center, 2, (0, 255, 0), -1)
        
        
        # Exibir as regiões dos olhos com o centro da pupila
        cv2.imshow("Left Eye", left_eye_region)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Substitua "aaa.webp" pelo caminho da sua imagem
detect_and_crop_eyes("dataset/foto-perfil.jpeg")
