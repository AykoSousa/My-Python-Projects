import customtkinter as ctk

window = ctk.CTk() # Criar a janela

# Configurando a janela principal
window.title("App Teste") # Define o título da aplicação
window.geometry("700x400") # Define largura e altura da janela
window.maxsize(width=900, height=550) # Define largura máxima
window.minsize(width=500, height=300) # Define altura mínima
window.resizable(width=False, height=False) # Define largura e altura sem alteração

# Tema
window._set_appearance_mode("light") # -> ["light", "dark", "system"]

# Criando nova janela
def new_display():
    new_window = ctk.CTkToplevel(window, fg_color="teal") # fg_color = backgorund-color
    new_window.geometry("400x400")

btn_new_display = ctk.CTkButton(master=window,
                                text="Abrir nova janela",
                                command=new_display).place(x=300, y=100)

# Frames
frame1 = ctk.CTkFrame(window, width=200, height=330, fg_color="teal", border_width=10).place(x=10, y=60)
frame2 = ctk.CTkFrame(window, width=200, height=330, fg_color="blue", border_color="red", border_width=10).place(x=230, y=60)
frame3 = ctk.CTkFrame(window, width=200, height=330, fg_color="green", corner_radius=5).place(x=450, y=60)

window.mainloop()