#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020/1/2 11:36:11


import logging
import os


def makedirs(path):
    """Check if the file exists, if it does not exist,
    then create it, support recursive creation
    """
    folders, _ = os.path.split(path)
    if folders:
        try:
            os.makedirs(folders)
        except:
            pass


# https://docs.python.org/zh-cn/3/library/logging.html#logrecord-attributes
DEFAULT_LOGGING_FORMAT = '%(asctime)s : %(levelname)s : %(message)s'
DEFAULT_LEVEL = logging.DEBUG


class mylogging:
    def __init__(self, log_file='log/default.log',
                 mode='a',
                 fmt=DEFAULT_LOGGING_FORMAT,
                 level=DEFAULT_LEVEL,
                 stream=False,
                 init=True
                 ):
        """
        :param log_file: supports formats like 'log/test.log'
        :param mode:
        :param fmt:
        :param level:
        :param stream: write to stdout if True
        :param init: write 'Init log' to logger if True
        :return:
        """
        self.log_file = log_file
        self.mode = mode
        self.fmt = fmt
        self.level = level
        self.stream = stream
        self.init = init
        self.logger = self._get_logger()

        if self.init:
            self._init()

    def _get_logger(self):
        logger = logging.getLogger(self.log_file)
        logger.setLevel(self.level)
        if self.stream:
            handler = logging.StreamHandler()
        else:
            makedirs(self.log_file)
            handler = logging.FileHandler(self.log_file, mode=self.mode, encoding='utf-8', delay=False)
        handler.setLevel(self.level)
        handler.setFormatter(logging.Formatter(self.fmt))
        logger.addHandler(handler)
        return logger

    def _init(self):
        self.logger.info('Init')

    def finish(self, msg="Finish"):
        self.logger.info(msg)

    def debug(self, msg, *args, **kwargs):
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        self.logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        self.logger.exception(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        self.logger.critical(msg, *args, **kwargs)

    fatal = critical

    @classmethod
    def get_blank_logger(cls, log_file='log/default_blank.log',
                         mode='a',
                         fmt='',
                         level=DEFAULT_LEVEL,
                         stream=False,
                         init=False
                         ):
        return cls(log_file=log_file, mode=mode, fmt=fmt, level=level, stream=stream, init=init)
