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
    
    def close_program():
        root.destroy()
        cap.release()
        cv.destroyAllWindows()

    # Configurando a janela para ocupar toda a tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")  # Define a largura e altura da janela e posição inicial (0, 0)

    root.title("Direção do Olhar")

    label_direction = tk.Label(root, text="Direção do Olhar: Aguardando Dados")
    label_direction.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
    
    close_button = tk.Button(bottom_frame, text="Fechar", command=close_program, width=20, height=2)
    close_button.grid(row=0, column=1, padx=(0, 10), pady=5, sticky="ew")

    bottom_frame.columnconfigure(0, weight=5)
    bottom_frame.columnconfigure(1, weight=0)

    # Adiciona os botões iniciais
    buttons = ['A', 'B', 'C', 'D', 'E', '->']
    button_frame = tk.Frame(root)
    button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    for i, button_text in enumerate(buttons):
        button = tk.Button(button_frame, text=button_text, command=lambda text=button_text: on_button_click(text),
                           width=26, height=10)
        button['font'] = ('Helvetica', 34)
        button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)

    entry_field = tk.Entry(bottom_frame, width=30)
    entry_field.grid(row=0, column=0, padx=(10, 10), pady=5, sticky="ew")
    entry_field.config(font=('Helvetica', 22))
    
    current_screen = 1
    shared_text = ""

    def on_button_click(button_text):
        global current_screen, shared_text
        current_entry_field = get_current_entry_field(current_screen)
        if button_text == '->':
            print("passar")
            show_next_screen(current_screen)
        else:
            shared_text += button_text
            current_entry_field.insert(tk.END, button_text)
            entry_field.delete(0, tk.END)
            entry_field.insert(tk.END, shared_text)
            
    def get_current_entry_field(current_screen):
        if current_screen == 1:
            return entry_field
        elif current_screen == 2:
            return entry_field_screen2
        elif current_screen == 3:
            return entry_field_screen3
        elif current_screen == 4:
            return entry_field_screen4
        elif current_screen == 5:
            return entry_field_screen5
        elif current_screen == 6:
            return entry_field_screen6
        else:
            return entry_field
            
    def close_other_screens(current_screen):
        for win in root.winfo_children():
            if isinstance(win, tk.Toplevel) and win != current_screen:
                win.destroy()   

    def show_second_screen():
        global current_screen
        current_screen = 2
        root.withdraw()
        close_other_screens(current_screen)
        second_screen = tk.Toplevel(root)
        second_screen.title("Segunda Tela")
        
        second_screen.attributes("-fullscreen", True)
        
        global entry_field_screen2
        entry_field_screen2 = tk.Entry(second_screen, width=30)
        entry_field_screen2.grid_rowconfigure(0, weight=1)
        entry_field_screen2.grid_columnconfigure(0, weight=1)
        entry_field_screen2.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        entry_field_screen2.config(font=('Helvetica', 22))
        entry_field_screen2.insert(tk.END, shared_text)

        new_buttons = ['F', 'G', 'H', 'I', 'J', '->']
        new_button_frame = tk.Frame(second_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=10, height=10) 
            button['font'] = ('Helvetica', 34)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
        for i in range(3):  # Number of columns
            new_button_frame.grid_columnconfigure(i, weight=1)

        for i in range((len(new_buttons) + 2) // 3):  # Number of rows
            new_button_frame.grid_rowconfigure(i, weight=1)
            
    def show_third_screen():
        global current_screen
        current_screen = 3
        close_other_screens(current_screen)
        third_screen = tk.Toplevel(root)
        third_screen.title("Terceira Tela")
        
        third_screen.attributes("-fullscreen", True)
        
        global entry_field_screen3
        entry_field_screen3 = tk.Entry(third_screen, width=30)
        entry_field_screen3.grid_rowconfigure(0, weight=1)
        entry_field_screen3.grid_columnconfigure(0, weight=1)
        entry_field_screen3.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        entry_field_screen3.config(font=('Helvetica', 22))
        entry_field_screen3.insert(tk.END, shared_text)

        new_buttons = ['K', 'L', 'M', 'N', 'O', '->']
        new_button_frame = tk.Frame(third_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=10, height=10)  
            button['font'] = ('Helvetica', 34)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
        for i in range(3):  # Number of columns
            new_button_frame.grid_columnconfigure(i, weight=1)

        for i in range((len(new_buttons) + 2) // 3):  # Number of rows
            new_button_frame.grid_rowconfigure(i, weight=1)
            
    def show_fourth_screen():
        global current_screen
        current_screen = 4
        close_other_screens(current_screen)
        fourth_screen = tk.Toplevel(root)
        fourth_screen.title("Quarta Tela")
        
        fourth_screen.attributes("-fullscreen", True)
        
        global entry_field_screen4
        entry_field_screen4 = tk.Entry(fourth_screen, width=30)
        entry_field_screen4.grid_rowconfigure(0, weight=1)
        entry_field_screen4.grid_columnconfigure(0, weight=1)
        entry_field_screen4.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        entry_field_screen4.config(font=('Helvetica', 22))
        entry_field_screen4.insert(tk.END, shared_text)

        new_buttons = ['P', 'Q', 'R', 'S', 'T', '->']
        new_button_frame = tk.Frame(fourth_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=70, height=25)  
            button['font'] = ('Helvetica', 34)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
        for i in range(3):  # Number of columns
            new_button_frame.grid_columnconfigure(i, weight=1)

        for i in range((len(new_buttons) + 2) // 3):  # Number of rows
            new_button_frame.grid_rowconfigure(i, weight=1)
            
    def show_5_screen():
        global current_screen
        current_screen = 5
        close_other_screens(current_screen)
        fifth_screen = tk.Toplevel(root)
        fifth_screen.title("Quinta Tela")
        
        fifth_screen.attributes("-fullscreen", True)
        
        global entry_field_screen5
        entry_field_screen5 = tk.Entry(fifth_screen, width=30)
        entry_field_screen5.grid_rowconfigure(0, weight=1)
        entry_field_screen5.grid_columnconfigure(0, weight=1)
        entry_field_screen5.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        entry_field_screen5.config(font=('Helvetica', 22))
        entry_field_screen5.insert(tk.END, shared_text)

        new_buttons = ['U', 'V', 'W', 'X', 'Y', '->']
        new_button_frame = tk.Frame(fifth_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=70, height=25)  
            button['font'] = ('Helvetica', 34)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
        for i in range(3):  # Number of columns
            new_button_frame.grid_columnconfigure(i, weight=1)

        for i in range((len(new_buttons) + 2) // 3):  # Number of rows
            new_button_frame.grid_rowconfigure(i, weight=1)
            
    def show_6_screen():
        global current_screen
        current_screen = 6
        close_other_screens(current_screen)
        sixth_screen = tk.Toplevel(root)
        sixth_screen.title("Sexta Tela")
        
        sixth_screen.attributes("-fullscreen", True)
        
        global entry_field_screen6
        entry_field_screen6 = tk.Entry(sixth_screen, width=30)
        entry_field_screen6.grid_rowconfigure(0, weight=1)
        entry_field_screen6.grid_columnconfigure(0, weight=1)
        entry_field_screen6.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
        entry_field_screen6.config(font=('Helvetica', 22))
        entry_field_screen6.insert(tk.END, shared_text)

        new_buttons = ['Z', 'Z', 'Z', 'Z', 'Z', '->']
        new_button_frame = tk.Frame(sixth_screen)
        new_button_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for i, button_text in enumerate(new_buttons):
            button = tk.Button(new_button_frame, text=button_text,
                               command=lambda text=button_text: on_button_click(text),
                               width=70, height=25)  
            button['font'] = ('Helvetica', 34)
            button.grid(row=i // 3, column=i % 3, sticky=tk.NSEW)
            
        for i in range(3):  # Number of columns
            new_button_frame.grid_columnconfigure(i, weight=1)

        for i in range((len(new_buttons) + 2) // 3):  # Number of rows
            new_button_frame.grid_rowconfigure(i, weight=1)

    def show_first_screen():
        global current_screen
        current_screen = 1
        close_other_screens(current_screen)
        root.deiconify()
        pass

    def on_button_text(button_text):
        start_time = time.time()
        
        if button_text == '1' and current_screen==1:
            while button_text == '1' and current_screen == 1:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('A')
                    break
                
        elif button_text == '2' and current_screen==1:
            while button_text == '2' and current_screen == 1:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('B')
                    break

        elif button_text == '3' and current_screen==1:
            while button_text == '3' and current_screen == 1:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('C')
                    break
                
        elif button_text == '4' and current_screen==1:
            while button_text == '4' and current_screen == 1:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('D')
                    break
                
        elif button_text == '5' and current_screen==1:
            while button_text == '5' and current_screen == 1:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('E')
                    break
            
            
        if button_text == '6':
            while button_text == '6':
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    show_next_screen(current_screen)
                    break
                
                
        elif button_text == '1' and current_screen==2:
            while button_text == '1' and current_screen == 2:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('F')
                    break
                
        elif button_text == '2' and current_screen==2:
            while button_text == '2' and current_screen == 2:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('G')
                    break

        elif button_text == '3' and current_screen==2:
            while button_text == '3' and current_screen == 2:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('H')
                    break
                
        elif button_text == '4' and current_screen==2:
            while button_text == '4' and current_screen == 2:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('I')
                    break
                
        elif button_text == '5' and current_screen==2:
            while button_text == '5' and current_screen == 2:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('J')
                    break
                
                
        elif button_text == '1' and current_screen==3:
            while button_text == '1' and current_screen == 3:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('K')
                    break
                
        elif button_text == '2' and current_screen==3:
            while button_text == '2' and current_screen == 3:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('L')
                    break

        elif button_text == '3' and current_screen==3:
            while button_text == '3' and current_screen == 3:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('M')
                    break
                
        elif button_text == '4' and current_screen==3:
            while button_text == '4' and current_screen == 3:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('N')
                    break
                
        elif button_text == '5' and current_screen==3:
            while button_text == '5' and current_screen == 3:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('O')
                    break
                
                
        elif button_text == '1' and current_screen==4:
            while button_text == '1' and current_screen == 4:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('P')
                    break
                
        elif button_text == '2' and current_screen==4:
            while button_text == '2' and current_screen == 4:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('Q')
                    break

        elif button_text == '3' and current_screen==4:
            while button_text == '3' and current_screen == 4:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('R')
                    break
                
        elif button_text == '4' and current_screen==4:
            while button_text == '4' and current_screen == 4:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('S')
                    break
                
        elif button_text == '5' and current_screen==4:
            while button_text == '5' and current_screen == 4:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('T')
                    break
                
                
        elif button_text == '1' and current_screen== 5:
            while button_text == '1' and current_screen == 5:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('U')
                    break
                
        elif button_text == '2' and current_screen==5:
            while button_text == '2' and current_screen == 5:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('V')
                    break

        elif button_text == '3' and current_screen==5:
            while button_text == '3' and current_screen == 5:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('W')
                    break
                
        elif button_text == '4' and current_screen==5:
            while button_text == '4' and current_screen == 5:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('X')
                    break
                
        elif button_text == '5' and current_screen==5:
            while button_text == '5' and current_screen == 5:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('Y')
                    break
                
                
                
        elif button_text == '1' and current_screen==6:
            while button_text == '1' and current_screen == 6:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('Z')
                    break
                
        elif button_text == '2' and current_screen==6:
            while button_text == '2' and current_screen == 6:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('Z')
                    break

        elif button_text == '3' and current_screen==6:
            while button_text == '3' and current_screen == 6:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('Z')
                    break
                
        elif button_text == '4' and current_screen==6:
            while button_text == '4' and current_screen == 6:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('Z')
                    break
                
        elif button_text == '5' and current_screen==6:
            while button_text == '5' and current_screen == 6:
                elapsed_time = time.time() - start_time
                if elapsed_time >= 3:
                    on_button_click('Z')
                    break
                

        
            
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
    
    root.attributes("-fullscreen", True)

    update_direction()
    root.mainloop()

cap.release()
cv.destroyAllWindows()