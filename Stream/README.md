# Compartir camara web por medio del buscador y un access point

Este script en python crea una API en flask y con ayuda de Gstreamer transmite la imagen de la camara web. 

EL punto de acceso wifi se creó por medio de la interfaz gráfica con la que cuenta la tarjeta Jetson Nano.

Para configurar el host es necesario acceder a *ifconfig* por medio de la terminal, buscar nuestra tarjeta de red y copiar la IP, posteriormente la colocamos en la siguiente linea de código:

        app.run(host="Insertar IP")

## Referencias

Cambio de longitudes de imagen:
https://www.codingforentrepreneurs.com/blog/open-cv-python-change-video-resolution-or-scale/

¿Como saber la resolucipon de la camara?
v4l2-ctl -d /dev/video0 --list-formats-ext

