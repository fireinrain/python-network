#!/usr/bin/env python
# encoding: utf-8
"""
@desc: 打包脚本 os.system, os.popen
@software: pycharm
@file: lsme.py
@time: 2018/11/6 22:36
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""
import os
import sys
import shutil
import time

import paramiko

# 传入源码路径
# source_path = sys.argv[1]

# 基础依赖
base_source_path = ""

source_path = "F:/IdeaProjects/mydevops-play".replace("/", "\\")

# 传入服务器目录
# server_path = sys.argv[2]

# 服务器ip
server_ip = '192.168.11.119'

# 服务器用户
server_user = "root"

# 服务器密码
server_pass = "sunriseme1994"

# 打包出来的所有jar包放在一起
jar_output_dir = source_path + os.sep + "jar_temp"

# jar 包名列表
target_jars_names = []

# 远程服务端 jar包地址
remote_server_dir = "/home/"

if not os.path.exists(jar_output_dir):
    print(f"不存在jar_temp目录")
    print(f"尝试创建：{jar_output_dir}")
    os.mkdir(jar_output_dir)
    print(f"创建：{jar_output_dir}成功")

if not os.path.exists(source_path):
    print(f"源码路径不存在：{source_path}")
    raise IOError
source_path_list = os.listdir(source_path)

# print(f"{source_path_list}")
# 排除jar_output
source_path_list = [i for i in source_path_list if i != "jar_temp"]
# print(f"{source_path_list}")
print(f"-----------------------------------------------")


def compile_java_code():
    for source in source_path_list:
        source_dir = source_path + os.sep + source
        os.chdir(source_dir)
        print(f"切换到：{source_dir}工作目录！")
        print(f"即将进行打包<<<-------")
        # os.system("mvn package")
        print(f"{source_dir}:打包完成!!!")
        files_list = os.listdir(source_dir + os.sep + "target")

        jar_files = [source_dir + os.sep + "target" + os.sep + i for i in files_list if i.endswith(".jar")]
        # 判断最大的jar
        jar_files = sorted(jar_files, key=lambda x: os.path.getsize(x), reverse=True)
        print(jar_files)
        target_jars_names.append(jar_files[0].split("\\")[-1])
        # 尝试复制jar包到外层临时目录
        shutil.copy(jar_files[0], jar_output_dir)
        print(f"复制jar包到外层临时目录成功")
        print(f"------------------------------------------")


def ssh_server_scp_run():
    # 连接主机 进行scp 拷贝，并尝试启动

    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='192.168.11.118', port=22, username="root", password="sunriseme1994")

        # jar包全路径
        local_jar_paths = [jar_output_dir + os.sep + i for i in target_jars_names]
        print(f"local_jar_paths: {local_jar_paths}")
        # 上传文件
        sftp = ssh.open_sftp()
        # sftp.put(local_jar_paths[0], "/home/"+target_jars_names[0])
        for index, jar in enumerate(local_jar_paths):
            sftp.put(jar, remote_server_dir + target_jars_names[index])

        command = ["cd /home", "bash", 'nohup java -jar boot2-0.0.1-SNAPSHOT.jar &']

        # # conn.write(command)
        chan = ssh.invoke_shell()  # 新函数

        for c in command:
            chan.send(c + '\n')
            # \n是执行命令的意思，没有\n不会执行
            time.sleep(2)  # 等待执行，这种方式比较慢
            # 这个时候就可以在chroot目录下执行命令了
            res = chan.recv(7000)
            print(res.decode('utf-8'))

        chan.close()
        ssh.close()
    except Exception as e:
        print(f"exception:{repr(e)}")


def run_steps():
    compile_java_code()
    ssh_server_scp_run()


if __name__ == '__main__':
    run_steps()

    # os.system("ls -a")
