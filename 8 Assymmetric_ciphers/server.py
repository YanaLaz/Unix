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
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()

p, g, b = 7, 5, 3
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