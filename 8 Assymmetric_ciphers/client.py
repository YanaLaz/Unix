import socket
import pickle

#симметричный шифр
def encrypt(k, m):
    return ''.join(map(chr, [x + k for x in map(ord, m)]))

def decrypt(k, c):
    return ''.join(map(chr, [x - k for x in map(ord, c)]))

HOST = '127.0.0.1'
PORT = 8080

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = 7, 5, 3
A = g ** a % p
sock.send(pickle.dumps((p, g, A))) # открытый ключ клиента

#получаем открытый ключ сервера
msgK = sock.recv(1024)
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