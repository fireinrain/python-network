#!/usr/bin/env python
# encoding: utf-8
"""
@desc:
@software: pycharm
@file: test_tls.py
@time: 2018/10/19 23:17
@author: liuzy
@contact: lzycoder.vip@gmail.com
@license: (C) Copyright 2015-2018, Node Supply Chain Manager Corporation Limited.
"""

import socket
import ssl
import sys, textwrap
import ctypes
from pprint import pprint


def open_tls(context, address, server=False):
    raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if server:
        raw_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        raw_sock.bind(address)
        raw_sock.listen(1)
        say("server is listen at ", address)
        raw_client_sock, addr = raw_sock.accept()
        say("get a connetction from ", addr)
        return context.wrap_socket(raw_client_sock, server_side=True)
    else:
        say("address we want to talk to ", address)
        raw_sock.connect(address)
        return context.wrap_socket(raw_sock)


def describe(ssl_sock, hostname, server=False, debug=False):
    cert = ssl_sock.getpeercert()
    if cert is None:
        say("Peer certificate", 'None')
    else:
        say("peer certificate", "provided")
        subjects = cert.get('subject', [])
        names = [name for names in subjects for (key, name) in names if key == 'conmonName']
        if 'subjectAltName' in cert:
            names.extend(name for (key, name) in cert['subjectAltName'] if key == 'DNS')
        say('Names on peer certificate', *names or ['none'])
        if (not server) and names:
            try:
                ssl.match_hostname(cert, hostname)
            except ssl.CertificateError as e:
                message = str(e)
            else:
                message = 'Yes'
            say('Whether the names match the hostname', message)
        for category, count in sorted(context.cert_store_stats().items()):
            say('Certificates ;oaded of type {}'.format(category), count)

    try:
        protocol_version = SSL_get_version(ssl_sock)
    except Exception as e:
        if debug:
            raise
    else:
        say('Protocol version is nigotiated', protocol_version)

    cipher, version, bits = ssl_sock.cipher()
    compression = ssl_sock.compression()

    say('cipher chosen for this connection ', cipher)
    say('cipher defined in TLS', version)
    say('cipher key has this many bits', bits)
    say('compresion algorithm in use', compression or 'none')


class PySSLSocket(ctypes.Structure):
    _fields = [('ob_refcnt', ctypes.c_ulong), ('ob_type', ctypes.c_void_p),
               ('Socket', ctypes.c_void_p), ('ssl', ctypes.c_void_p)]


def SSL_get_version(ssl_sock):
    lib = ctypes.CDLL(ssl.ssl.__file__)
    lib.SSL_get_version.restype = ctypes.c_char_p
    address = id(ssl_sock.sslobj)
    struct = ctypes.cast(address, ctypes.POINTER(PySSLSocket)).contents
    version_bytestring = lib.SSL_get_version(struct.ssl)
    return version_bytestring.decode('ascii')


def look_up(prefix, name):
    if not name.startswith(prefix):
        name = prefix + name
    try:
        return getattr(ssl, name)
    except AttributeError as e:
        mathing_names = (s for s in dir(ssl) if s.startswith(prefix))
        message = f"Error: {' '.join(sorted(mathing_names))} is not one of the available names"
        print(fill(message), file=sys.stderr)
        sys.exit(2)


def say(title, *words):
    print(fill(title.ljust(36, '.')) + ' ' + ' '.join(str(w) for w in words))


def fill(text):
    return textwrap.fill(text, subsequent_indent='   ', break_long_words=False, break_on_hyphens=False)


if __name__ == '__main__':
    address = ('127.0.0.1', 8000)
    protocol = look_up('PROTOCOL', 'SSLv23')
    context = ssl.SSLContext(protocol)
    context.set_ciphers('ALL')
    context.check_hostname = False
    context.verify_mode = ssl.CERT_REQUIRED
    purpose = ssl.Purpose.SERVER_AUTH
    context.load_default_certs(purpose)
    print()

    ssl_sock = open_tls(context, address, None)
    cert = describe(ssl_sock, '127.0.0.1', None, False)
    print()
