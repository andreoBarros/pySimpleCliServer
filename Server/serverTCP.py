import socket
import argparse
import threading
import sys


def Servidor(argv):
    tamHeader = 42
    tamBuffer = 4000000
    total = 0
    parser = argparse.ArgumentParser(description='Servidor TCP.')

    parser.add_argument('-p', type=int, help='Porta para o servidor escutar')
    
    argumentos = parser.parse_args()
    porta = argumentos.p

    # change this to get self ip by some pyhton lib
    socketInicialUDP = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketInicialUDP.connect(('8.8.8.8', 80))
    ip = socketInicialUDP.getsockname()[0]
    socketInicialUDP.close()
    # nessas linhas de cima ele acha seu próprio ip
    
    socketTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketTCP.bind((ip, porta))
    print('O servidor escuta na porta: ', porta, 'Com o IP: ', ip)
    socketTCP.listen(1)
    
    while True:
        con, cliente = socketTCP.accept()
        print ('Conectado por', cliente)

        while True:
            data = con.recv(tamBuffer)
            total += len(data)
            print("Dados recebidos: ", total, end ="\r")


if __name__ == '__main__':
    Servidor(sys.argv)

# python lab-redes-server.py -p 3332
# ipconfig
# python lab-redes.py -i 192.168.0.55 -p 3332 -r 10
