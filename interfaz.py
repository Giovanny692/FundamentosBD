import tkinter as tk

class Interfaz():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Interfaz") 
        self.root.config(width=1000,height=500)
        self.root.resizable(0,0)
        frame = Frame(self.root)
        frame.poner_labels()
        frame.poner_textos()
        frame.poner_botones()
        frame.mainloop()

class Frame(tk.Frame):
    def __init__(self,root):
        super().__init__(root,width=1000,height=500)
        self.root = root
        self.pack()
        
    def poner_labels(self):
        self.label_id = tk.Label(self,text='ID: ')
        self.label_id.config(font=('Arial',12,''),width=10)
        self.label_id.grid(row=0,column=0,padx=10,pady=10)
        
        self.label_nombre = tk.Label(self,text='Nombre: ')
        self.label_nombre.config(font=('Arial',12,''),width=10)
        self.label_nombre.grid(row=1,column=0,padx=10,pady=10)
        
        self.label_telefono = tk.Label(self,text='Telefono: ')
        self.label_telefono.config(font=('Arial',12,''),width=10)
        self.label_telefono.grid(row=2,column=0,padx=10,pady=10)
    
    def poner_textos(self):
        self.texto_id = tk.Entry(self)
        self.texto_id.config(width=30, font=('Arial',12))
        self.texto_id.grid(row=0,column=1,padx=10,pady=10) 
        
        self.texto_nombre = tk.Entry(self)
        self.texto_nombre.config(width=30, font=('Arial',12))
        self.texto_nombre.grid(row=1,column=1,padx=10,pady=10)    
        
        self.texto_telefono = tk.Entry(self)
        self.texto_telefono.config(width=30, font=('Arial',12))
        self.texto_telefono.grid(row=2,column=1,padx=10,pady=10) 
        
        self.texto_nombre_busc = tk.Entry(self)
        self.texto_nombre_busc.config(width=30, font=('Arial',12),state='disabled')
        self.texto_nombre_busc.grid(row=1,column=2,padx=10,pady=10) 
        
        self.texto_nombre_busc = tk.Entry(self)
        self.texto_nombre_busc.config(width=30, font=('Arial',12),state='disabled')
        self.texto_nombre_busc.grid(row=2,column=2,padx=10,pady=10)  
        
    def poner_botones(self):
        self.boton_entrada = tk.Button(self,text='Entrada')   
        self.boton_entrada.config(width=20,font=('Arial',12,'bold'),fg='red')
        self.boton_entrada.grid(row=3,column=0) 
        
        self.boton_busqueda = tk.Button(self,text='Busqueda')   
        self.boton_busqueda.config(width=20,font=('Arial',12,'bold'),fg='green')
        self.boton_busqueda.grid(row=3,column=1) 
        
        
        
        
        
            
                


            
    
        
def main():
    interfaz = Interfaz() 
    print("e")

if __name__ == '__main__':
    main()        
    
      
            
        