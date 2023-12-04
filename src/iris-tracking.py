import cv2 as cv
import numpy as np
import mediapipe as mp

# pega a câmera
cap = cv.VideoCapture(0)

# while infinito
while True:
    
    ret, frame = cap.read() # pega os frames
    if not ret: # se nao tiver input de vídeo, sai do loop
        break
    cv.imshow('img', frame) # mostra os frames da câmera
    key = cv.waitKey(1)
    if key == ord('q'): # sai do loop se apertar a tecla q
        break
    
cap.release() # libera a câmera
cv.destroyAllWindows() # destroi todas as telas