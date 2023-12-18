import cv2 as cv
import numpy as np
import mediapipe as mp
import tkinter as tk
import time

mp_face_mesh = mp.solutions.face_mesh

LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
LEFT_IRIS = [474, 475, 476, 477]
RIGHT_IRIS = [469, 470, 471, 472]

cap = cv.VideoCapture(0)

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
) as face_mesh:

    root = tk.Tk()


    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    root.title("Direção do Olhar")

    label_direction = tk.Label(root, text="Direção do Olhar: Aguardando Dados")
    label_direction.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


    buttons = ['A', 'B', 'C', 'D', 'E', '->']
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    for i, button_text in enumerate(buttons):
        button = tk.Button(button_frame, text=button_text, command=lambda text=button_text: on_button_click(text),
                           width=70, height=25)
        button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)

    entry_field = tk.Entry(root, width=30)
    entry_field.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)  
    entry_field.config(font=('Helvetica', 14))
    
    current_screen = 1

    def close_other_screens(current_screen):
        for win in root.winfo_children():
            if isinstance(win, tk.Toplevel) and win != current_screen:
                win.destroy()
            
    def on_button_click(button_text):
        global current_screen
        if button_text == '->':
            show_next_screen(current_screen)
        else:
            entry_field.insert(tk.END, button_text)

    def show_second_screen():
        global current_screen
        current_screen = 2
        close_other_screens(current_screen)

        second_screen = tk.Toplevel(root)
        second_screen.title("Segunda Tela")

        new_buttons = ['F', 'G', 'H', 'I', 'J', '->']
        new_button_frame = tk.Frame(second_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=70, height=25)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
    def show_third_screen():
        global current_screen
        current_screen = 3
        close_other_screens(current_screen)
        third_screen = tk.Toplevel(root)
        third_screen.title("Terceira Tela")

        new_buttons = ['K', 'L', 'M', 'N', 'O', '->']
        new_button_frame = tk.Frame(third_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=70, height=25)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
    def show_fourth_screen():
        global current_screen
        current_screen = 4
        close_other_screens(current_screen)

        fourth_screen = tk.Toplevel(root)
        fourth_screen.title("Quarta Tela")

        new_buttons = ['P', 'Q', 'R', 'S', 'T', '->']
        new_button_frame = tk.Frame(fourth_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=70, height=25)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
    def show_5_screen():
        global current_screen
        current_screen = 5
        close_other_screens(current_screen)

        five_screen = tk.Toplevel(root)
        five_screen.title("Quinta Tela")

        new_buttons = ['U', 'V', 'W', 'X', 'Y', '->']
        new_button_frame = tk.Frame(five_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=70, height=25)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
    def show_6_screen():
        global current_screen
        current_screen = 6
        close_other_screens(current_screen)
        six_screen = tk.Toplevel(root)
        six_screen.title("Sexta Tela")

        new_buttons = ['Z', 'Z', 'Z', 'Z', 'Z', '->']
        new_button_frame = tk.Frame(six_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=70, height=25)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)

    def show_first_screen():
        global current_screen
        current_screen = 1
        close_other_screens(current_screen)
        pass
    
    def timer():
        tempo_inicial = time.time()

        def time_count():
            return time.time() - tempo_inicial
        
        if time_count() > 3:
            return 1
        else:
            return 0

    def on_button_text(button_text):
        if button_text == '1' and current_screen==1:
            while button_text == '1' and current_screen==1:
                time=timer()
                if time == 1:
                    on_button_click('A')
                    
        elif button_text == '2' and current_screen==1:
            while button_text == '2' and current_screen==1:
                time=timer()
                if time == 1:
                    on_button_click('B')
                    
        elif button_text == '3' and current_screen==1:
            while button_text == '3' and current_screen==1:
                time=timer()
                if time == 1:
                    on_button_click('C')
                    
        elif button_text == '4' and current_screen==1:
            while button_text == '4' and current_screen==1:
                time=timer()
                if time == 1:
                    on_button_click('D')

        elif button_text == '5' and current_screen==1:
            while button_text == '5' and current_screen==1:
                time=timer()
                if time == 1:
                    on_button_click('E')
                    
            
        if button_text == '6':
            while button_text == '6':
                time=timer()
                if time == 1:
                    show_next_screen(current_screen)

            
        elif button_text == '1' and current_screen==2:
            while button_text == '1' and current_screen==2:
                time=timer()
                if time == 1:
                    on_button_click('F')
            
        elif button_text == '2' and current_screen==2:
            while button_text == '2' and current_screen==2:
                time=timer()
                if time == 1:
                    on_button_click('G')
            
        elif button_text == '3' and current_screen==2:
            while button_text == '3' and current_screen==2:
                time=timer()
                if time == 1:
                    on_button_click('H')
            
        elif button_text == '4' and current_screen==2:
            while button_text == '4' and current_screen==2:
                time=timer()
                if time == 1:
                    on_button_click('I')
            
        elif button_text == '5' and current_screen==2:
            while button_text == '5' and current_screen==2:
                time=timer()
                if time == 1:
                    on_button_click('J')
            
            
        elif button_text == '1' and current_screen==3:
            while button_text == '1' and current_screen==3:
                time=timer()
                if time == 1:
                    on_button_click('K')
            
        elif button_text == '2' and current_screen==3:
            while button_text == '2' and current_screen==3:
                time=timer()
                if time == 1:
                    on_button_click('L')
            
        elif button_text == '3' and current_screen==3:
            while button_text == '3' and current_screen==3:
                time=timer()
                if time == 1:
                    on_button_click('M')
            
        elif button_text == '4' and current_screen==3:
            while button_text == '4' and current_screen==3:
                time=timer()
                if time == 1:
                    on_button_click('N')
            
        elif button_text == '5' and current_screen==3:
            while button_text == '5' and current_screen==3:
                time=timer()
                if time == 1:
                    on_button_click('O')
            
            
        elif button_text == '1' and current_screen==4:
            while button_text == '1' and current_screen==4:
                time=timer()
                if time == 1:
                    on_button_click('P')
            
        elif button_text == '2' and current_screen==4:
            while button_text == '2' and current_screen==4:
                time=timer()
                if time == 1:
                    on_button_click('Q')
            
        elif button_text == '3' and current_screen==4:
            while button_text == '3' and current_screen==4:
                time=timer()
                if time == 1:
                    on_button_click('R')
            
        elif button_text == '4' and current_screen==4:
            while button_text == '4' and current_screen==4:
                time=timer()
                if time == 1:
                    on_button_click('S')
            
        elif button_text == '5' and current_screen==4:
            while button_text == '5' and current_screen==4:
                time=timer()
                if time == 1:
                    on_button_click('T')
            
            
        elif button_text == '1' and current_screen==5:
            while button_text == '1' and current_screen==5:
                time=timer()
                if time == 1:
                    on_button_click('U')
            
        elif button_text == '2' and current_screen==5:
            while button_text == '2' and current_screen==5:
                time=timer()
                if time == 1:
                    on_button_click('V')
            
        elif button_text == '3' and current_screen==5:
            while button_text == '3' and current_screen==5:
                time=timer()
                if time == 1:
                    on_button_click('W')
            
        elif button_text == '4' and current_screen==5:
            while button_text == '4' and current_screen==5:
                time=timer()
                if time == 1:
                    on_button_click('X')
            
        elif button_text == '5' and current_screen==5:
            while button_text == '5' and current_screen==5:
                time=timer()
                if time == 1:
                    on_button_click('Y')
            
            
        elif button_text == '1' and current_screen==6:
            while button_text == '1' and current_screen==6:
                time=timer()
                if time == 1:
                    on_button_click('Z')
            
        elif button_text == '2' and current_screen==6:
            while button_text == '2' and current_screen==6:
                time=timer()
                if time == 1:
                    on_button_click('Z')
            
        elif button_text == '3' and current_screen==6:
            while button_text == '3' and current_screen==6:
                time=timer()
                if time == 1:
                    on_button_click('Z')
            
        elif button_text == '4' and current_screen==6:
            while button_text == '4' and current_screen==6:
                time=timer()
                if time == 1:
                    on_button_click('Z')
            
        elif button_text == '5' and current_screen==6:
            while button_text == '5' and current_screen==6:
                time=timer()
                if time == 1:
                    on_button_click('Z')
            
            
    def show_next_screen(current_screen):
        if current_screen==1:
            show_second_screen()
        elif current_screen==2:
            show_third_screen()
        elif current_screen==3:
            show_fourth_screen()
        elif current_screen==4:
            show_5_screen()
        elif current_screen==5:
            show_6_screen()
        elif current_screen==6:
            show_first_screen()

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