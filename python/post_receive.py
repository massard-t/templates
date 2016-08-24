#!/usr/bin/env python
# coding: utf-8
import sys
import logging
import sh
import os


__author__ = "Theo Massard <theo@reezocar.com>"

DOCKER_KEY = [key for key in os.environ if "docker" in key.lower()][0]
DOCKER_LOCATION = os.environ.get(DOCKER_KEY)


def prepare_my_logger():
    global my_logger
    my_logger = logging.getLogger()
    my_logger.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s >> %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    my_logger.addHandler(stream_handler)


def manage_opts(args):
    try:
        trimmed_args = args[0][:-1]
        my_logger.info("Original Message: {}".format(trimmed_args))
    except IndexError:
        my_logger.error("Missing informations.", exc_info=True)
        sys.exit(1)


def get_commit_message():
    #    my_logger.info(sys.argv[1])
    with open(sys.argv[1], 'r') as f:
        commit_message = f.readlines()
    #    print(commit_message)
    content = commit_message[0].split(" ")
    return content


def makefile_command_inside_container(command, _ret_ouput=False):
    my_logger.info(DOCKER_LOCATION)
    sh.cd(DOCKER_LOCATION)
    my_logger.info("Executing rule {}.".format(command))
    try:
        if _ret_ouput is True:
            return sh.make(command)
        sh.make(command)
    except Exception:
        my_logger.error()
        my_logger.error("Error while processing command. Error: {}".
                        format(Exception))


def get_git_infos():
    config = sh.git.config("-l")
    tmp = [line for line in config.split("\n") if "origin.url" in line]
    str(tmp).split("/")[-1]


def test_func():
    containers = sh.docker("ps")
    c_s = containers.split("\n")
    if len(c_s) == 2:
        my_logger.info("containers aren't running")
        my_logger.info("Containers' location: " + DOCKER_LOCATION)
        try:
            my_logger.warning("Containers aren't running")
            # makefile_command_inside_container("project")
        except Exception:
            my_logger.error("Something really bad happened", exc_info=True)
    else:
        try:
            res = makefile_command_inside_container("test_pytest_spiders")
            print(res)
            
        except Exception:
            my_logger.error("Something really bad happened during the test.")
    # my_logger.info(c_s[0])


def main():
    prepare_my_logger()
    message = get_commit_message()
    manage_opts(message)


if __name__ == '__main__':
    main()
    test_func()
    sys.exit(1)
