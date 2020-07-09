#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess

from common import IS_WIN, INFO_FMT, logger


def ping(host):
    logger.info(INFO_FMT.format(f"ping: {host}"))
    opt = "-c 5" if not IS_WIN else ""
    cmd = f"ping {opt} {host}"
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    res = [i.strip() for i in p.stdout.read().decode('gbk').split('\n') if i and i.strip()]
    return res
