import cv2 as cv
import numpy as np
import mediapipe as mp
import tkinter as tk

mp_face_mesh = mp.solutions.face_mesh

LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

cap = cv.VideoCapture(1)

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
) as face_mesh:

    root = tk.Tk()

    # Configurando a janela para ocupar toda a tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")  # Define a largura e altura da janela e posição inicial (0, 0)

    root.title("Direção do Olhar")

    label_direction = tk.Label(root, text="Direção do Olhar: Aguardando Dados")
    label_direction.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Adiciona os botões iniciais
    buttons = ['A', 'B', 'C', 'D', 'E', '->']
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    for i, button_text in enumerate(buttons):
        button = tk.Button(button_frame, text=button_text, command=lambda text=button_text: on_button_click(text),
                           width=70, height=25)  # Ajusta a largura e altura do botão
        button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)

    entry_field = tk.Entry(root, width=30)
    entry_field.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)  # Use fill=tk.X para preencher horizontalmente
    entry_field.config(font=('Helvetica', 14))  # Ajuste a altura aqui alterando o tamanho da fonte
    
    current_screen = 1

    def on_button_click(button_text):
        global current_screen
        if button_text == '->':
            show_second_screen()
        else:
            entry_field.insert(tk.END, button_text)

    def show_second_screen():
        global current_screen
        current_screen = 2
        # Cria uma nova tela com os botões F, G, H, I, J, ->
        second_screen = tk.Toplevel(root)
        second_screen.title("Segunda Tela")

        new_buttons = ['F', 'G', 'H', 'I', 'J', '->']
        new_button_frame = tk.Frame(second_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text, second_screen),
                               width=70, height=25)  # Ajusta a largura e altura do botão
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
    def show_third_screen():
        global current_screen
        current_screen = 3
        # Cria uma nova tela com os botões F, G, H, I, J, ->
        second_screen = tk.Toplevel(root)
        second_screen.title("Segunda Tela")

        new_buttons = ['K', 'L', 'M', 'N', 'O', '->']
        new_button_frame = tk.Frame(second_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text, second_screen),
                               width=70, height=25)  # Ajusta a largura e altura do botão
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
    def show_fourth_screen():
        global current_screen
        current_screen = 4
        # Cria uma nova tela com os botões F, G, H, I, J, ->
        second_screen = tk.Toplevel(root)
        second_screen.title("Segunda Tela")

        new_buttons = ['P', 'Q', 'R', 'S', 'T', '->']
        new_button_frame = tk.Frame(second_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text, second_screen),
                               width=70, height=25)  # Ajusta a largura e altura do botão
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
    def show_5_screen():
        global current_screen
        current_screen = 5
        # Cria uma nova tela com os botões F, G, H, I, J, ->
        second_screen = tk.Toplevel(root)
        second_screen.title("Segunda Tela")

        new_buttons = ['U', 'V', 'W', 'X', 'Y', '->']
        new_button_frame = tk.Frame(second_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text, second_screen),
                               width=70, height=25)  # Ajusta a largura e altura do botão
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
    def show_6_screen():
        global current_screen
        current_screen = 6
        # Cria uma nova tela com os botões F, G, H, I, J, ->
        second_screen = tk.Toplevel(root)
        second_screen.title("Segunda Tela")

        new_buttons = ['Z', 'Z', 'Z', 'Z', 'Z', '->']
        new_button_frame = tk.Frame(second_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text, second_screen),
                               width=70, height=25)  # Ajusta a largura e altura do botão
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)

    def show_first_screen():
        global current_screen
        current_screen = 1
        # Lógica para a primeira tela
        pass

    def on_button_text(button_text):
        if button_text == '1' and current_screen==1:
            on_button_click('A')
        elif button_text == '2' and current_screen==1:
            on_button_click('B')
        elif button_text == '3' and current_screen==1:
            on_button_click('C')
        elif button_text == '4' and current_screen==1:
            on_button_click('D')
        elif button_text == '5' and current_screen==1:
            on_button_click('E')
        elif button_text == '6':
            show_second_screen()
            
        elif button_text == '1' and current_screen==2:
            on_button_click('F')
        elif button_text == '2' and current_screen==2:
            on_button_click('G')
        elif button_text == '3' and current_screen==2:
            on_button_click('H')
        elif button_text == '4' and current_screen==2:
            on_button_click('I')
        elif button_text == '5' and current_screen==2:
            on_button_click('J')
            
    def show_next_screen(current_screen):
        if current_screen=='2':
            show_second_screen()
            
        
    

    def update_direction():
        global current_screen
        print(f"Está na Tela: {current_screen}")
        ret, frame = cap.read()

        if not ret:
            return

        frame = cv.flip(frame, 1)
        rgb_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        img_h, img_w = frame.shape[:2]
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:

            mesh_points = np.array([np.multiply([p.x, p.y], [img_w, img_h]).astype(int) for p in
                                    results.multi_face_landmarks[0].landmark])

            center_left_eye = tuple(np.mean(mesh_points[LEFT_EYE], axis=0, dtype=np.int32))
            center_right_eye = tuple(np.mean(mesh_points[RIGHT_EYE], axis=0, dtype=np.int32))

            (l_cx, l_cy), l_radius = cv.minEnclosingCircle(mesh_points[LEFT_IRIS])
            (r_cx, r_cy), r_radius = cv.minEnclosingCircle(mesh_points[RIGHT_IRIS])

            center_left = np.array([l_cx, l_cy], dtype=np.int32)
            center_right = np.array([r_cx, r_cy], dtype=np.int32)

            cv.circle(frame, center_left_eye, 3, (0, 255, 0), -1, cv.LINE_AA)
            cv.circle(frame, center_right_eye, 3, (0, 255, 0), -1, cv.LINE_AA)
            cv.circle(frame, tuple(center_left), 3, (255, 0, 255), -1, cv.LINE_AA)
            cv.circle(frame, tuple(center_right), 3, (255, 0, 255), -1, cv.LINE_AA)

            vector_left_eye = np.array(center_left_eye) - np.array(tuple(center_left))
            vector_right_eye = np.array(center_right_eye) - np.array(tuple(center_right))

            vetor = ["centro", "centro"]

            if vector_right_eye[0] > 5:
                vetor[0] = 'left'

            elif vector_right_eye[0] < -5:
                vetor[0] = 'right'
            else:
                vetor[0] = 'center'

            if vector_right_eye[1] > 2:
                vetor[1] = 'up'
            else:
                vetor[1] = 'center'

            if vetor[0] == 'left' and vetor[1] == 'up':
                on_button_text('1')
            elif vetor[0] == 'center' and vetor[1] == 'up':
                on_button_text('2')
            elif vetor[0] == 'right' and vetor[1] == 'up':
                on_button_text('3')
            elif vetor[0] == 'left' and vetor[1] == 'center':
                on_button_text('4')
            elif vetor[0] == 'center' and vetor[1] == 'center':
                on_button_text('5')
            elif vetor[0] == 'right' and vetor[1] == 'center':
                show_next_screen(current_screen)

        cv.imshow('img', frame)
        key = cv.waitKey(1)
        if key == ord('q'):
            root.destroy()

        root.after(100, update_direction)

    # Centraliza o frame do botão
    root.update_idletasks()
    button_frame.place(in_=root, anchor="c", relx=.5, rely=.5)
    root.update_idletasks()

    update_direction()
    root.mainloop()

cap.release()
cv.destroyAllWindows()