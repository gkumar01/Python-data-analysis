#!/usr/bin/python 3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import sys
import logging
import numpy as np
import pandas as pd
from collections import  namedtuple

from utils.data_prep import DataExtractor

__version__ = '1.0.0'

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
# Need to comment below to avoid printing output mltiple times
# as this is called from root/main script.
# logger.addHandler(logging.StreamHandler(sys.stdout))


def setup_parser(args):
    parser = argparse.ArgumentParser(description="Arguments")
    parser.add_argument(
        '--version',
        '-v',
        action = 'version',
        version='%(prog)s {}'.format(__version__),
        help="Display the version and quit"
    )
    parser.add_argument(
        '--input-file',
        '-i',
        help="input data file"
    )
    parser.add_argument(
        '--output-dir',
        '-d',
        help="output directory"
    )
    parser.add_argument(
        '--model-type',
        '-m',
        help="output directory"
    )
    return parser


def process_argv(args):
    """ Parse CLI arguments and return a named tuple object.
    Args: The command line input
    return: A runInfo tupple
    raises: None.
    """

    parser = setup_parser(args)
    args, unknown_argv = parser.parse_known_args(args)
    args_dict = vars(args)
    attr_list = sorted(args_dict.keys())
    SysInfo = namedtuple('SysInfo', attr_list)
    sys_info = SysInfo(**args_dict)
    # logger.info(sys_info)

    return sys_info


def run_main(args=None):
    """ main entry point"""
    ret_code = 0
    msg = '{}'.format("Hello")
    logger.info(msg)
    run_info = process_argv(sys.argv[1:])
    logger.info('run_main: {}'.format(run_info))

    #create director if not exists
    if not os.path.exists(run_info.output_dir):
        os.mkdir(run_info.output_dir)

    data_obj = DataExtractor(run_info.input_file)
    df = data_obj.get_data()
    logger.info('Test:{}'.format(df.head()))
    return ret_code


if __name__ == '__main__':
    """
    usage:
    python3 test.py \
        --input-file ./input_data/diabetes.csv  \
        --output-dir ./output_data/ \
        --model-type 'linearregression' \
        
    """
    
    try:
        return_code = run_main()
    except SystemExit:
        allowed_exit = ['--version', '-h', '--help']
        if not any(x not in sys.argv for x in allowed_exit):
            logger.error('error parsing arguments')
            raise
    except KeyboardInterrupt:
        logger.critical('error parsing arguments')
        sys.exit(1)
    except Exception as e:
        exec_type, _, _ = sys.exc_info()
        msg = '{}: {}'.format(exec_type.__name__, str(e))
        logger.exception(msg)
        sys.exit(1)
    else:
        sys.exit(return_code)
