import tkinter as tk
import random

def move_no_button():
    new_x = random.randint(0, window.winfo_width() - no_button.winfo_width())
    new_y = random.randint(0, window.winfo_height() - no_button.winfo_height())
    no_button.place(x=new_x, y=new_y)

def yes_clicked():
    new_window = tk.Toplevel(window)
    new_window.title("¡Respuesta!")
    tk.Label(new_window, text="Sabía que dirías que sí", font=("Arial", 14)).pack()

window = tk.Tk()
window.geometry("300x200")
window.title("Pregunta importante")

question_label = tk.Label(window, text="¿Quieres ser mi novia?", font=("Arial", 14))
question_label.pack(pady=20)

yes_button = tk.Button(window, text="Sí", command=yes_clicked)
yes_button.pack(side=tk.LEFT, padx=50)

no_button = tk.Button(window, text="No")
no_button.place(x=150, y=100)
no_button.bind("<Enter>", lambda event: move_no_button())

window.mainloop()
