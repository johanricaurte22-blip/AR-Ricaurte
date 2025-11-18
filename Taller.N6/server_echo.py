#!/usr/bin/env python3
# Python Network Programming Cookbook -- Chapter 1
# Adaptado para Python 3

import socket
import argparse

HOST = '0.0.0.0'
DATA_PAYLOAD = 2048
BACKLOG = 5


def echo_server(port):
    """A simple echo server"""
    # Crear un socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permitir reusar la dirección/puerto
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Asociar el socket al puerto
    server_address = (HOST, port)
    print(f"Starting up echo server on {server_address[0]} port {server_address[1]}")
    sock.bind(server_address)

    # Escuchar conexiones entrantes
    sock.listen(BACKLOG)

    while True:
        print("Waiting to receive message from client...")
        client, address = sock.accept()
        print(f"Connection from {address}")

        data = client.recv(DATA_PAYLOAD)
        if data:
            print(f"Data: {data.decode()}")
            client.sendall(data)  # enviar eco al cliente
            print(f"Sent {len(data)} bytes back to {address}")

        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)