#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

# Dirección IP del servidor.
if len(sys.argv) != 3:
    sys.exit("Usage: python client.py method receiver@IP:SIPport")
    
METODO = sys.argv[1].upper()
LOGIN = sys.argv[2].split("@")[0] + "@"
IP = sys.argv[2].split("@")[1].split(":")[0]
PUERTO = int(sys.argv[2].split('@')[1].split(":")[1])

# Contenido que vamos a enviar
LINE = METODO + " sip:"+ LOGIN + IP + " SIP/2.0\r\n"


# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.connect((IP, PUERTO))

    print("Enviando: " + LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)

    print('Recibido -- ', data.decode('utf-8'))
    print("Terminando socket...")

print("Fin.")
