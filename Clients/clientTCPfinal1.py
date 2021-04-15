import socket
import argparse
import math
import sys
import shutil
import logging

import time
import matplotlib
matplotlib.use('GTK3Agg')
from matplotlib import pyplot as plt
import numpy as np

RAZAO = 1000 / 8
RAZAO_INVERSA = 8 / 1000000


## rodar isso e mostrar ajuda: python3 Server/serverTCP.py -h
def ClienteUDP(argv):
    tamHeader = 42
    tamBuffer = 800000
    

    colunas, linhas = shutil.get_terminal_size(fallback=(80, 24)) # é só para desenhar o texto
    
    # Desenhando gr'afico inicial ------------------------------------------------------------------
    # fig, ax = plt.subplots(1, 1)
    # ax.set_aspect('equal')
    # ax.set_xlim(0, 255)
    # ax.set_ylim(0, 255)
    # ax.hold(True)
    # nextXpoint = 0
    # x = 0
    # y = 0
    # plt.show(True)
    # plt.draw()

    # background = fig.canvas.copy_from_bbox(ax.bbox)

    # points = ax.plot(x, y, 'o')[0]
    # tic = time.time()
    #logFile ------------------------------------------------------------------------------------------
    logging.basicConfig(filename="Logs/logfileclient1.log", level=logging.INFO)
    
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

    bitsPerSecond = 0


    # Create TCP socket and connect
    TCPsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (ip, porta)
    TCPsocket.connect(dest)

    

    start_time = time.time()   
    while True:
       TCPsocket.send(pacoteParaEnviar)
       packetSent +=  1514
       times = time.time()

       
       #Graph related stuff
       # update the xy data
    #    KbytesPerSecond = bitsPerSecond/8000
    #    x = nextXpoint
    #    y = KbytesPerSecond
    #    points.set_data(x, y)
    #    # restore background
    #    fig.canvas.restore_region(background)
    #    # redraw just the points
    #    ax.draw_artist(points)
    #    # fill in the axes rectangle
    #    fig.canvas.blit(ax.bbox)
    #    # prepara o proximo ponto
    #    nextXpoint+=1

    #    plt.ion() ## Note this correction
    #    fig=plt.figure()
    #    plt.axis([0,10,0,1])

    #    plt.title('Package Flow Graph')
    #    plt.ylabel('Speed in Kbytes/s')
    #    plt.xlabel('Speed in Kbytes/s')
    #    baseGraphX+=1

    #    plt.bar(baseGraphX, KbytesPerSecond)       # Plotar uma barra a cada ponto novo do grafico
    #    plt.draw()                   # Display the plot
    #    plt.pause(0.001) 

       if times - start_time >= count:
          count +=1
          bitsPerSecond = packetSent * 8

          print(bitsPerSecond, 'Contador: ', count, 'Real time:', times - start_time, end = "\r")
          
          logging.info(',' + str(bitsPerSecond) + ',' + str(times - start_time))

          packetSent = 0

if __name__ == '__main__':
    ClienteUDP(sys.argv)
