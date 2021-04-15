import socket
import argparse
import math
import time
import sys
import shutil
import logging

RAZAO = 1000 / 8
RAZAO_INVERSA = 8 / 1000000

def ClienteUDP(argv):
    tamHeader = 42
    tamBuffer = 800000
    

    colunas, linhas = shutil.get_terminal_size(fallback=(80, 24)) # é só para desenhar o texto

    #logFile
    logging.basicConfig(filename="logfileclient3.log", level=logging.INFO)
    
    parser = argparse.ArgumentParser(
        description='Simulador de trafego TCP cliente.')

    parser.add_argument('-i', type=str, help='Endereço IP alvo')
    parser.add_argument('-p', type=int, help='Porta alvo')
    # parser.add_argument('-r', type=int, help='Tamanho da rajada')
    count = 0
    packetSent = 0
    argumentos = parser.parse_args()
    ip = argumentos.i
    porta = argumentos.p
    tamRajada = 1000
    print('=' * colunas)
    print('Cliente TCP'.center(colunas))
    print('-' * colunas)
    print('Ip: ', argumentos.i)
    print('Porta: ', argumentos.p)
    print('=' * colunas)

    pacotesEnviados = 0
    pacoteParaEnviar = bytearray(1448)

    # Create TCP socket and connect
    TCPsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (ip, porta)
    TCPsocket.connect(dest)
    
    start_time = time.time()   
    while True:
       TCPsocket.send(pacoteParaEnviar)
       packetSent +=  1514
       times = time.time()

       if times - start_time >= count:
          count +=1
          bitsPerSecond = packetSent * 8

          print(bitsPerSecond, 'Contador: ', count, 'Real time:', times - start_time, end = "\r",)
          
          logging.info(',' + str(bitsPerSecond) + ',' + str(times - start_time))

          packetSent = 0

if __name__ == '__main__':
    ClienteUDP(sys.argv)
