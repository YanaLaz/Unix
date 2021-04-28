#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
print('Создание сокета')

port = 9090
sock.bind(('', port))
sock.listen(1)
print(f'Подключение сокета к порту {port}')

conn, addr = sock.accept()

print('connected:', addr)
ok = True
while ok:
	data = conn.recv(1024)
	if not data:
		print(f'Отключение клиента')
		break
	print(f'Полученное сообщение: {data.decode()}')
	if data.decode() == 'exit':
		print('Остановка сервера')
		ok = False
		conn.close()
		break
	print(f'Отправленное сообщение: {data.decode()}')
	conn.send(data)
