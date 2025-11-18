#!/usr/bin/env python3
import socket
import sys
import argparse

host = '192.168.10.1'

def echo_client(port):
    """A simple echo client"""
    # Crear un socket TCP/IP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar el socket al servidor
    server_address = (host, port)
    print(f"Connecting to {server_address[0]} port {server_address[1]}")
    sock.connect(server_address)

    try:
        # Enviar datos
        message = "Test message. This will be echoed"
        print(f"Sending: {message}")
        sock.sendall(message.encode('utf-8'))

        # Esperar la respuesta
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f"Received: {data.decode('utf-8')}")

    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Other exception: {e}")
    finally:
        print("Closing connection to the server")
        sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action="store", dest="port",
                        type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)