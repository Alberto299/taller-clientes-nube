"""
Referencia — Cliente original de escritorio (Tkinter)
------------------------------------------------------
Este es el cliente ORIGINAL con el que arrancó el proyecto: una ventanita
de Tkinter con un menú para elegir el motor y dos botones (+ / -) que
mandan comandos al servidor por Socket.IO.

No es parte del taller como tal (los alumnos trabajan en Colab), pero se
deja aquí como referencia de dónde salió la lógica de los tres clientes
que sí se desarrollan en `colab/`.

Requiere un entorno de escritorio con pantalla (no funciona en Colab):
    pip install socketIO-client
"""

from socketIO_client import SocketIO
from tkinter import *
from functools import partial

SERVER_IP = "TU-IP-SERVIDOR"  # ej: "34.136.249.24"
SERVER_PORT = 5001

print("Comenzando...")
socketIO = SocketIO(SERVER_IP, SERVER_PORT)
print("Conectado al servidor.")


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        value_inside = StringVar(root)
        value_inside.set("1")
        options_list = ["1", "2", "3", "4", "5"]
        question_menu = OptionMenu(root, value_inside, *options_list)
        question_menu.place(x=75, y=10)

        boton_mas = Button(
            self, text="+", width=10, height=8,
            command=partial(self.increase, value_inside),
        )
        boton_mas.place(x=25, y=30)

        boton_menos = Button(
            self, text="-", width=10, height=8,
            command=partial(self.decrease, value_inside),
        )
        boton_menos.place(x=200, y=30)

    def increase(self, value_inside):
        message = {"motor": value_inside.get(), "command": "+"}
        socketIO.emit("ctrl_from_python", message)

    def decrease(self, value_inside):
        message = {"motor": value_inside.get(), "command": "-"}
        socketIO.emit("ctrl_from_python", message)


if __name__ == "__main__":
    root = Tk()
    app = Window(root)
    root.wm_title("CONTROL")
    root.geometry("320x200+700+400")
    root.mainloop()
