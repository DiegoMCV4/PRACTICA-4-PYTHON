import tkinter as tk
from tkinter import messagebox

def limpiar_campos():
    entryNombre.delete(0, tk.END)
    entryApellidos.delete(0, tk.END)
    entryEdad.delete(0, tk.END)
    entryEstatura.delete(0, tk.END)
    entryTelefono.delete(0, tk.END)
    varGenero.set(0)

def borrar_campos():
    limpiar_campos()

def guardar_datos():
    nombre = entryNombre.get()
    apellidos = entryApellidos.get()
    edad = entryEdad.get()
    estatura = entryEstatura.get()
    telefono = entryTelefono.get()
    
    genero = ""
    if varGenero.get() == 1:
        genero = "Hombre"
    elif varGenero.get() == 2:
        genero = "Mujer"
    
    datos = f"Nombre: {nombre}\nApellidos: {apellidos}\nEdad: {edad} a\u00f1os\nEstatura: {estatura}\nTel\u00e9fono: {telefono}\nG\u00e9nero: {genero}\n"
    
    with open("DatosFormulario.txt", "a") as archivo:
        archivo.write(datos + "\n\n")
    
    messagebox.showinfo("Informacion", f"Datos guardados con exito:\n\n{datos}")

    limpiar_campos()

ventana = tk.Tk()
ventana.geometry("800x600") 
ventana.title("Formulario Version 01")

varGenero = tk.IntVar(value=0)

labelNombre = tk.Label(ventana, text="Nombre(s):")
labelNombre.pack()
entryNombre = tk.Entry(ventana)
entryNombre.pack()

labelApellidos = tk.Label(ventana, text="Apellidos:")
labelApellidos.pack()
entryApellidos = tk.Entry(ventana)
entryApellidos.pack()

labelTelefono = tk.Label(ventana, text="Telefono:")
labelTelefono.pack()
entryTelefono = tk.Entry(ventana)
entryTelefono.pack()

labelEdad = tk.Label(ventana, text="Edad:")
labelEdad.pack()
entryEdad = tk.Entry(ventana)
entryEdad.pack()

labelEstatura = tk.Label(ventana, text="Estatura:")
labelEstatura.pack()
entryEstatura = tk.Entry(ventana)
entryEstatura.pack()

labelGenero = tk.Label(ventana, text="Genero:")
labelGenero.pack()
radioHombre = tk.Radiobutton(ventana, text="Hombre", variable=varGenero, value=1)
radioHombre.pack()
radioMujer = tk.Radiobutton(ventana, text="Mujer", variable=varGenero, value=2)
radioMujer.pack()

botonGuardar = tk.Button(ventana, text="Guardar", command=guardar_datos)
botonGuardar.pack(padx=20, pady=5)

botonBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_campos)
botonBorrar.pack(padx=10, pady=5)

ventana.mainloop()
