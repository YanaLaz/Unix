#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import errno

def free_port(sock, s_port):
    try:
        sock.bind(('', s_port))
        print(f'port: {s_port}')
        return True
    except socket.error as e:
        if e.errno == errno.EADDRINUSE:
            s_port += 1
            return free_port(sock, s_port)

def log_txt(data):
    with open("logServer.txt", "a") as f:
        f.write(f'{data}\n')


#очищаю файл лог сервера
f = open("logServer.txt", 'w+')
f.seek(0)
f.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
log_txt('Создание сокета')

s_port = 9095

if free_port(sock, s_port):
	sock.listen(1)
	log_txt(f'Подключение сокета к порту {s_port}')


	ok = True
	while ok:
		f = open('logServer.txt', 'a')
		conn, addr = sock.accept() # подтверждение пользователя
		log_txt(f'Подключение к клиенту: {addr}')
		work = True
		while work:
			data = conn.recv(1024)
			if not data:
				print(f'Отключение клиента')
				break
			if data.decode() == 'exit':
				log_txt('Отключение клиента от сервера')
				work = False
				break
			log_txt(f'Полученное сообщение: {data.decode()}')
			conn.send(data)


