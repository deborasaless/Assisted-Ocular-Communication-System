import cv2 as cv
import numpy as np
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh # pegando o face mesh model do mediapipe

LEFT_EYE=[362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398] # landmarks do olho esquerdo
RIGHT_EYE=[33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246] # landmarks do olho direito

LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

cap = cv.VideoCapture(0) # pega a câmera

with mp_face_mesh.FaceMesh( # passando alguns parâmetros
    max_num_faces=1, 
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as face_mesh:
    
    while True: # while infinito
        ret, frame = cap.read() # pega os frames
        
        if not ret: # se nao tiver input de vídeo, sai do loop
            break
        
        frame = cv.flip(frame, 1) # flipando a imagem (como se eu estivesse me olhando no espelho)
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB) 
        img_h, img_w = frame.shape[:2] # pegando as dimensões
        results = face_mesh.process(rgb_frame)
        
        if results.multi_face_landmarks:
            
            # print(results.multi_face_landmarks[0].landmark)
            
            mesh_points=np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in results.multi_face_landmarks[0].landmark])
            
            # print(mesh_points.shape)
            cv.polylines(frame, [mesh_points[LEFT_EYE]], True, (0,255,0), 1, cv.LINE_AA) # desenha formato do olho esquerdo
            cv.polylines(frame, [mesh_points[RIGHT_EYE]], True, (0,255,0), 1, cv.LINE_AA) # desenha formato do olho direito
            
            (l_cx, l_cy), l_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS]) # calcula a posição da iris esquerda
            (r_cx, r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS]) # calcula a posição da iris direita
            
            center_left = np.array([l_cx, l_cy], dtype=np.int32) # converte
            center_right = np.array([r_cx, r_cy], dtype=np.int32) # converte
            
            cv.circle(frame, center_left, int(l_radius), (255, 0, 255), 1, cv.LINE_AA) # desenha formato da iris esquerda
            cv.circle(frame, center_right, int(r_radius), (255, 0, 255), 1, cv.LINE_AA) # desenha formato da iris direita
            
            # print(center_left)
            # print(center_right)
            
        cv.imshow('img', frame) # mostra os frames da câmera
        key = cv.waitKey(1)
        if key == ord('q'): # sai do loop se apertar a tecla q
            break
    
cap.release() # libera a câmera
cv.destroyAllWindows() # destroi todas as telas