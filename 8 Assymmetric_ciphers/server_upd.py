import socket
import pickle

#симметричный шифр
def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [x - k for x in map(ord, c)]))

def checker(m):
    sp = [1,3,5,7]
    for i in m:
        if int(i) not in sp:
            print('В ключе неверное значение')
            conn.send(pickle.dumps(('exit')))
            conn.close()
            return False
    return True


HOST = '127.0.0.1'
def_port = 8090

PORT = int(input("Введите порт: "))
if (1023 >= PORT):
    print(f'Порт введён неверно, порт по умолчанию -  {def_port}')
    PORT = int(def_port)

sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()


with open('openKeyB.txt', 'r') as f:
    x = f.readline()
    x = x.replace(' ','').split(',')
    p, g, b = int(x[0]), int(x[1]), int(x[2])

if checker(x):
    #p, g, b = 7, 5, 3
    B = g ** b % p
    conn.send(pickle.dumps((p, g, B)))

    #получаем открытый ключ клиента
    msgK = conn.recv(1024)
    K = pickle.loads(msgK)[2] ** b % p
    print('K =', K)

    #расшифровать сообщение
    msgR = conn.recv(1024)
    msgR = decrypt(b, pickle.loads(msgR))
    msgR = decrypt(K, msgR)
    print("msgR =", msgR)

    #прислать сообщение
    msg = encrypt(b, 'Hello client!')
    msg = encrypt(K, msg)
    conn.send(pickle.dumps((msg)))
    print("msg to send =", msg)

    conn.close()