#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))
            metodos = ["INVITE", "ACK", "BYE"]
            metodo = line.decode('utf-8').split(' ')[0]
            if len(line) >=2:
                if metodo == "INVITE":
                    enviar = b"SIP/2.0 100 Trying\r\n\r\n"
                    enviar += b"SIP/2.0 180 Ring\r\n\r\n"
                    enviar += b"SIP/2.0 200 OK\r\n\r\n"
                    self.wfile.write(enviar)
                elif metodo == "ACK":
                    aEjecutar = './mp32rtp -i ' + IP + ' -p 23032 <' + FICHERO
                    os.system(aEjecutar)

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break

if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = socketserver.UDPServer(('', 6001), EchoHandler)
    print("Lanzando servidor UDP de eco...")
    serv.serve_forever()
