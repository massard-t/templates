#!/usr/bin/env python
# coding: utf-8
import sys
import logging
import sh


def prepare_logger():
    global logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s >> %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def manage_opts(args):
    try:
        if len(args) > 3:
            logger.error("Too much arguments. Exiting")
            sys.exit(1)
        logger.info("From: {}".format(args[0]))
        logger.info("To: {}".format(args[1]))
        logger.info("Branch: {}".format(2))
        logger.info("{} are the args".format(' '.join(args)))
        logger.info("Somestuff")
    except IndexError:
        logger.error("Missing informations.", exc_info=True)
        sys.exit(1)


def get_stdin_content():
    stdin_content = sys.stdin.readlines()
    args = stdin_content[0].split(" ")
    return args


def main():
    prepare_logger()
    message = get_stdin_content()
    manage_opts(message)


if __name__ == '__main__':
    main()
