import socket
import pickle

#симметричный шифр
def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [x - k for x in map(ord, c)]))


HOST = '127.0.0.1'
def_port = 8090

PORT = int(input("Введите порт: "))
if (1023 >= PORT):
    print(f'Порт введён неверно, порт по умолчанию -  {def_port}')
    PORT = int(def_port)

sock = socket.socket()
sock.connect((HOST, PORT))

with open('openKeyA.txt', 'r') as f:
    x = f.readline()
    x = x.replace(' ','').split(',')
    p, g, a = int(x[0]), int(x[1]), int(x[2])

#p, g, a = 7, 5, 3
A = g ** a % p
sock.send(pickle.dumps((p, g, A))) # открытый ключ клиента

#получаем открытый ключ сервера
msgK = sock.recv(1024)
if pickle.loads(msgK) == 'exit':
    sock.close()
else:
    K = pickle.loads(msgK)[2] ** a % p
    print('K =', K)

    #прислать сообщение
    msg = encrypt(a, 'Hello server!')
    msg = encrypt(K, msg)
    sock.send(pickle.dumps((msg)))
    print("msg to send =", msg)

    #расшифровать сообщение
    msgR = sock.recv(1024)
    msgR = decrypt(a, pickle.loads(msgR))
    msgR = decrypt(K, msgR)
    print("msgR =", msgR)

    sock.close()