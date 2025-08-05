import tkinter as tk

class AppGUI:
    def __init__(self, api_client):
        self.api_client = api_client
        self.root = tk.Tk()
        self.root.title("Aplicação Desktop")

        self.label = tk.Label(self.root, text="Bem-vindo!")
        self.label.pack(padx=20, pady=20)

    def run(self):
        self.root.mainloop()

# Removed duplicate main block to avoid errors and conflicts