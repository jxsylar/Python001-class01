#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket


def scan(host: str, port: int):
    s = socket.socket()
    is_open = False
    try:
        s.settimeout(1)
        res = s.connect_ex((host, port))
        is_open = res == 0
    finally:
        s.close()
        res = {
            'host': host,
            'port': port,
            'open': is_open
        }
        return res
