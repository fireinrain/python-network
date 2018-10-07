#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: proxy_server.py
@time: 2018/10/7 11:52
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import socket
import threading
import re


def proxy(ser):  # 接收线程传递过来的socket对象
    conn, addr = ser.accept()  # 接收一个connection然后返回新的connection和address
    data = conn.recv(1024)  # 接收从conn收到的数据
    # print(data)                                          #查看接收到的内容，收到的数据是byte类型
    path_num = data.decode().find('\r\n')  # 解码byte类型数据为字符串，然后查找第一行的末尾数
    first_line = data.decode()[:path_num]  # 获取第一行数据（后续要用来判断请求的方法《method》和相对路径）
    remain_line = data.decode()[path_num:]  # 获取http head及data，即除第一行以外的数据（需要了解http协议就知道为什么这样处理）
    method, path_url, protocol = first_line.split()  # http第一行数据中包含三个内容，用空格分割之后就得到三个（后面需要用）
    # print(method)                                        #查看method
    print(path_url)  # 查看path_url（即全url）（后续需要用这个url分割相对路径）
    # print(protocol)                                      #查看protocol（即http的请求协议，一般就是“http/1.1”）
    host = re.findall(r'(?<=://).*?(?=/)', path_url)[0]  # 从全url中分割出host（这个host是用来作为proxy转发到web服务器时的目标地址用）
    main_url = re.findall(r'.*?://', path_url)[0] + host  # 从全url中分割出主url（即http://加host）
    # print(main_url)                                      #查看主url
    path = path_url[len(main_url):]  # 相对路径/shopxx-mobile/goods/list/243.jhtml
    s_data = method + ' ' + path + ' ' + protocol + remain_line  # 将抓到的包进行处理，然后合并**作为**后续转发到web服务器的数据
    print(s_data)  # 打印要发送的数据

    print(host)  # 打印host
    try:  # 判断从抓取到的数据中的host是ip地址类型的，还是域名类型的，然后有不同处理
        r_host = socket.gethostbyname(host)  # 尝试使用域名解析ip地址，如果解析成功就将port赋值80（这里不严谨，没有考虑https）
        port = '80'
    except:
        if ':' in host:  # 如果host中有“:”说明host就是ip地址，并分割出ip址和port
            r_host, port = host.split(':')
        else:
            port = '80'
    s_s = socket.socket()  # 再创建一个sockte对象，用于前面分离出的ip与端口进行转发浏览器接收到的数据
    print(r_host, port)
    s_s.connect((r_host, int(port)))  # 连接从浏览器接收到的数据中的目标ip与端口
    print("############################")
    print(s_data)  # 打印要转发的数据
    s_s.send(s_data.encode())  # 转发要发送的数据
    d = s_s.recv(1024)  # 接收转发到web服务器的返回数据
    print(d)  # 打印从web服务器返回的数据
    conn.send(d)  # 将接收的数据使用最上面socket对象中的conn进行发送
    # ser.close()
    # s_s.close()


SER_ADDR = ('', 80)  # 因为socket中的bind需要一个地址与端口的tuple类型
ser = socket.socket()  # 创建一个socket对象
ser.bind(SER_ADDR)  # 对socket对象绑定地址和端口
ser.listen(5)  # 设置socket对象同时监听多少个链接

while True:  # 为开启线程循环
    t = threading.Thread(target=proxy(ser))
    t.start()
