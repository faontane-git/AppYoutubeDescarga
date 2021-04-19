import tkinter as tk
import pytube
#Autor:
#Fabrizzio Ontaneda
master=tk.Tk()
master.title("Youtube Video Descarga")
tk.Label(master,text="Convertidor de video youtube",fg="red",font=("calibri,15")).grid(sticky=tk.N,padx=100,row=0)
tk.Label(master,text="Profavor ingrese el enlace: del video a continuación",fg="red",font=("calibri,12")).grid(sticky=tk.N,padx=1,row=15)
notif=tk.Label(master,font=("Calibri",12))
notif.grid(sticky=tk.N,pady=1,row=4)

def descarga():
    try:
        youtube=pytube.YouTube(Url.get())
        video=youtube.streams.first()
        video.download("C:/Users/fabri/Desktop/decargavideos") #Colocar la dirección a donde quieres que se guarden los videos
        notif.config(fg="red",text="Descarga Completa")
    except Exception as e:
        print(e)
        notif.config(fg="red",text="No se pudo descargar el video")

Url=tk.StringVar()
tk.Button(master,width=20,text="Descargar",font=("Calibri",12),command=descarga).grid(sticky=tk.N,row=3,pady=15)
tk.Entry(master,width=50,textvariable=Url).grid(sticky=tk.N,row=2)
master.mainloop()

