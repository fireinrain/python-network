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

if __name__ == '__main__':
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

        # 尝试复制jar包到外层临时目录
        shutil.copy(jar_files[0],jar_output_dir)
        print(f"复制jar包到外层临时目录成功")
        print(f"------------------------------------------")


    print(os.path.getsize("F:/IdeaProjects/mydevops-play/boot2/target/target.jar"))
    # print(server_path)
    # os.system("ls -a")
