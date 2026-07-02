# 🕹️ Taller Nube — Clientes de Control por Socket.IO

Repositorio del taller de **Computación en la Nube**: tres clientes
progresivos, todos ejecutables desde **Google Colab** (sin instalar nada
en la computadora del alumno), que se conectan por **Socket.IO** a un
servidor que controla motores.

Cada cliente construye sobre el anterior y termina con un reto de
personalización para que cada alumno lo haga suyo.

```
taller-nube-clientes/
├── README.md
├── LICENSE
├── requirements_desktop.txt
├── reference/
│   └── control_tkinter_original.py   # cliente original de escritorio (referencia)
└── colab/
    ├── cliente_1_botones.ipynb        # Nivel básico
    ├── cliente_2_sliders.ipynb        # Nivel intermedio
    └── cliente_3_gestos_manos.ipynb   # Nivel avanzado
```

## Los 3 clientes del taller

| # | Cliente | Qué controla | Tecnología nueva que introduce |
|---|---|---|---|
| 1 | **Botones** | Incrementos `+`/`-` por motor | Gradio como interfaz web en Colab |
| 2 | **Sliders** | Posición absoluta (0°–180°) por motor | Límites de seguridad, estado en Python |
| 3 | **Gestos de mano** | Igual que el 1, pero con la mano frente a la cámara | MediaPipe + acceso a la webcam del navegador desde Colab |

El **Cliente 3** es la versión en Colab del script original de OpenCV +
MediaPipe: como Colab no puede abrir la cámara directamente
(`cv2.VideoCapture` no funciona ahí), el notebook usa un pequeño puente
de JavaScript que captura cuadros del video del navegador y se los pasa
a Python para procesarlos con MediaPipe — cuadro por cuadro.

## Cómo abrir los notebooks en Colab

Sube este repositorio a GitHub y abre cada notebook con:

```
https://colab.research.google.com/github/TU-USUARIO/taller-nube-clientes/blob/main/colab/cliente_1_botones.ipynb
```

(reemplaza el nombre del archivo para los clientes 2 y 3), o desde Colab:
**Archivo → Abrir notebook → GitHub** y pega la URL del repositorio.

## Requisitos del servidor

Los tres clientes emiten al mismo evento de Socket.IO:

```json
{"motor": "1", "command": "+"}
```

- `motor`: identificador del motor (`"1"` a `"5"` en los ejemplos).
- `command`: `"+"` / `"-"` (clientes 1 y 3) o `"set"` con un campo extra
  `"valor"` (cliente 2, posición absoluta 0–180).

Tu servidor debe escuchar el evento `ctrl_from_python` en el puerto que
configures (por defecto `5001` en los notebooks).

> ⚠️ **Nota de compatibilidad:** los notebooks usan el paquete
> `socketIO-client`, que habla el protocolo **Socket.IO 1.x**. Si tu
> servidor usa una versión moderna de Socket.IO (2.x en adelante) y la
> conexión falla o se queda colgada, prueba con la librería
> `python-socketio` en su lugar (`pip install python-socketio`), que sí
> soporta las versiones recientes del protocolo.

## Para el instructor: cómo correr el taller

1. Antes de la sesión, levanta el servidor de Socket.IO en tu VM y
   comparte la IP pública con el grupo (como en la guía de "Pasos
   Críticos" de la presentación del curso).
2. Cada alumno abre `cliente_1_botones.ipynb`, cambia `SERVER_IP` y
   ejecuta las celdas en orden.
3. Al final de cada notebook hay un bloque **"🧪 Personaliza tu
   cliente"** con 3–4 ideas de reto. Pide a cada alumno que resuelva
   al menos una antes de pasar al siguiente cliente.
4. El Cliente 3 requiere cámara y permisos del navegador — recomienda
   Chrome o Edge, y probarlo con tiempo antes de la sesión en vivo.

## Licencia

MIT — úsalo y adáptalo libremente para tus talleres.
