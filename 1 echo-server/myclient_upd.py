#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import socket


def address(def_port, def_ip):
    u_port = input("Введите порт: ")
    if (1023 >= int(port)) & (int(port) >= 65536):
        print(f'Порт введён неверно, порт по умолчанию -  {def_port}')
        u_port = str(def_port)

    u_ip = input("Введите ip сервера: ")
    if check_ip(u_ip) is False:
        print(f'Ip введен неверно, ip сервера по умолчанию -  {def_ip}')
        u_ip = def_ip
    return int(u_port), u_ip

def check_ip(ip):
    try:
        sum = 0
        if ip == 'localhost':
            return True
        parts = ip.split(".", 4)
        if len(parts) == 4:
            for part in parts:
                part = int(part)
                if -1 < part < 256:
                    sum += 1
        else:
            return False
        if sum != 4:
            return False
    except ValueError:
        return False

def log_txt(data):
    with open("logClient.txt", "a") as f:
        f.write(f'{data}\n')


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9095
ip = '127.0.0.1'

u_port, u_ip = address(port, ip)

#очищаю файл лог клиента
f = open("logСlient.txt", 'w+')
f.seek(0)
f.close()

sock.connect((u_ip, u_port))
log_txt(f'Соединение с сервером')

while True:
    mes = input()
    sock.send(mes.encode())
    log_txt(f'Отправка сообщения {mes.encode()}')
    if mes == 'exit':
        log_txt(f'Разрыв соединения с сервером')
        sock.close()
        break
    data = sock.recv(1024)
    log_txt(f'Сообщение доставлено: {data.decode()}')
