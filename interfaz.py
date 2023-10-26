import tkinter as tk

class interfaz():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("interfaz")
        barra_menu(root)
    
    def cambiar_menu():
        print("a")    
    
    def barra_menu(root):
        menu = tk.Menu(root)
        root.config(menu=menu,width=100,lenght=100)
        menu.add_cascade(label="escritura",command=cambiar_menu)
        
def main():
    interfaz = interfaz()      
    
      
            
        