#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from enum import Enum
from ipaddress import ip_address

from mylog import mylogging

IS_WIN = 'win' in sys.platform

INFO_FMT = "{:-^50}"

logger = mylogging.get_blank_logger(__name__, stream=True)


class TestType(str, Enum):
    TCP = "tcp"
    PING = "ping"


class ConcurrentType(str, Enum):
    MULTIPROCESSING = "proc"
    THREADING = "thread"


def get_ip(hosts):
    tmp = [i.strip() for i in hosts.split('-') if i and i.strip()]
    if len(tmp) == 1:
        yield from tmp
    else:
        start_ip, end_ip = [ip_address(i) for i in tmp]
        while start_ip <= end_ip:
            yield start_ip.exploded
            start_ip += 1


def get_port(ports):
    delimiter = '-' if '-' in ports else ',' if ',' in ports else None
    tmp = [i.strip() for i in ports.split(delimiter) if i and i.strip()] if delimiter else [ports]
    if not all(i.isdigit() for i in tmp):
        raise ValueError(f"Port must be type of int")
    tmp = [int(i) for i in tmp]
    if delimiter == '-':
        start_port, end_port = tmp
        while start_port <= end_port:
            yield start_port
            start_port += 1
    else:
        yield from tmp
