#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import concurrent
import json
import multiprocessing
import sys
import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import typer

from common import get_ip, logger, ConcurrentType, TestType, get_port
from mylog import makedirs
from ping import ping
from scan import scan

app = typer.Typer()


@app.command()
def main(
        hosts: str = typer.Option(..., '-ip', help="IP地址(范围), 如: 192.168.0.1-192.168.0.100"),
        ports: str = typer.Option("1-1024", '-p',
                                  help="待扫描端口号, 支持端口号范围, 支持单个端口号, 连续端口号(用'-'连接, 如: '3000-4000'), 不连续端口号(用','连接, 如: '22,3389,3306,27017')"),
        concurrent_num: int = typer.Option(32, '-n', help="并发数量. 默认32"),
        concurrent_type: ConcurrentType = typer.Option(ConcurrentType.THREADING, '-m', case_sensitive=False,
                                                       help=f"并发类型. 默认: {ConcurrentType.THREADING}"),
        test_type: TestType = typer.Option(TestType.TCP, '-f', case_sensitive=False, help=f"测试类型. 默认: {TestType.TCP}"),
        saved_file: str = typer.Option(None, '-w', case_sensitive=False, help="保存文件"),
        verbose: bool = typer.Option(None, '-v', is_eager=True, help="打印扫描器运行耗时"),
):
    """
    基于多进程或多线程模型的端口主机扫描器
    """
    Executor = ThreadPoolExecutor
    if concurrent_type == ConcurrentType.MULTIPROCESSING:
        Executor = ProcessPoolExecutor
        concurrent_num = multiprocessing.cpu_count()

    _is_saved = False
    if saved_file:
        try:
            makedirs(saved_file)
            f = open(saved_file, "w", encoding='utf-8')
            f.write("[")
            _is_saved = True
        except OSError as e:
            logger.error(e)
            sys.exit(1)

    tic = time.perf_counter()
    with Executor(concurrent_num) as exec:
        tasks = {}
        for host in get_ip(hosts):
            if test_type == TestType.PING:
                future = exec.submit(ping, host)
                tasks.update({future: {'host': host, 'type': test_type}})
            else:
                for port in get_port(ports):
                    future = exec.submit(scan, host, port)
                    tasks.update({future: {'host': host, 'type': test_type}})

        for future in concurrent.futures.as_completed(tasks):
            host, test_type = tasks[future]['host'], tasks[future]['type']
            result = future.result()
            if test_type == TestType.PING:
                logger.info('\n'.join(result))

            elif result['open']:
                logger.info(result)

            if _is_saved:
                out = json.dumps({
                    'host': host,
                    "concurrent_num": concurrent_num,
                    "concurrent_type": concurrent_type,
                    "test_type": test_type,
                    "verbose": verbose,
                    "info": result
                }, ensure_ascii=False)
                f.write(out + ',')

    toc = time.perf_counter()

    if _is_saved:
        f.seek(f.tell()-1)
        f.write("]")

    if verbose:
        logger.info(f"\nTime elapse(s): {toc - tic:.6f}")

    if _is_saved:
        f.close()
        logger.info(f"\nThe result saved in file: {saved_file}")


if __name__ == '__main__':
    app()
