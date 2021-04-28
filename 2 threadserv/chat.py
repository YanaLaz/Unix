import socket
import threading
import queue
import sys
import random
import os


#Клиент
def ReceiveData(sock):
    while True:
        try:
            data,addr = sock.recvfrom(1024) # socket.recvfrom(bufsize) вернет данные и адрес сокета с которого получены данные.
            print(data.decode('utf-8'))
        except:
            pass

def RunClient(serverIP):
    host = socket.gethostbyname(socket.gethostname()) # получаем имя хоста
    port = random.randint(6000,10000) #рандомный порт
    print('Client IP->'+str(host)+' Port->'+str(port))
    server = (str(serverIP), 5000)
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # создаём сокет, который будет принимать соединения на порту 5000
    s.bind((host,port)) # связываем сокет с адресом и портом

    name = input('Please write your name here: ')
    if name == '':
        name = 'Guest'+str(random.randint(1000,9999))
        print('Your name is:'+name)
    s.sendto(name.encode('utf-8'),server) #отправляем имя серверу
    threading.Thread(target=ReceiveData,args=(s,)).start() # создаём поток и запускаем многопоточное выполнение
    while True:
        data = input() # принимаем сообщение
        if data == 'exit':
            break
        elif data == '':
            continue
        data = '['+name+']' + '->' + data
        s.sendto(data.encode('utf-8'),server) # отправка данных серверу
    s.sendto(data.encode('utf-8'),server)
    s.close()
    os._exit(1)



#Сервер
def RecvData(sock,recvPackets):
    while True:
        data,addr = sock.recvfrom(1024) # socket.recvfrom(bufsize) вернет данные и адрес сокета с которого получены данные.
        recvPackets.put((data, addr))

def RunServer():
    host = socket.gethostbyname(socket.gethostname()) # получаем имя хоста
    port = 5000
    print('Server hosting on IP-> '+str(host))
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # создаём сокет, который будет принимать соединения на порту 5000
    s.bind((host,port)) # связываем сокет с адресом и портом
    clients = set()
    recvPackets = queue.Queue()

    print('Server Running...')

    threading.Thread(target=RecvData,args=(s,recvPackets)).start() # создаём поток и запускаем многопоточное выполнение

    while True:
        while not recvPackets.empty():
            data,addr = recvPackets.get()
            if addr not in clients:
                clients.add(addr)
                continue
            clients.add(addr)
            data = data.decode('utf-8')
            if data.endswith('exit'):
                clients.remove(addr)
                continue
            print(str(addr)+data)
            for c in clients:
                if c!=addr:
                    s.sendto(data.encode('utf-8'),c)
    s.close()


if __name__ == '__main__':
    if len(sys.argv)==1:
        RunServer()
    elif len(sys.argv)==2:
        RunClient(sys.argv[1])
    else:
        print('Run Serevr:-> python Chat.py')
        print('Run Client:-> python Chat.py <ServerIP>')