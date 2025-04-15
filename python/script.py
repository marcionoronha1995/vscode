import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

# Criação da janela principal
root = tk.Tk()
root.title("Tela de Login")

# Widgets da tela de login
label_username = tk.Label(root, text="Usuário:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Senha:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=10)

# Inicia o loop da interface gráfica
root.mainloop()