#!/usr/bin/python3 

import logging


def main(*args, **kwargs):
    logging.basicConfig()
    log = logging.getLogger("portfolio")
    log.setLevel(logging.DEBUG)

    log
    pass
