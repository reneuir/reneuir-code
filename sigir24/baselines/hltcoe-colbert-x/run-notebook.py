#!/usr/bin/env python3
import argparse
import subprocess
import sys
import os

def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--notebook', type=str, help='The notebook to execute.', required=True)

    return parser.parse_args()


def main(args):
    command = f'runnb --allow-not-trusted {args.notebook}'
    subprocess.check_call(command, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)


if __name__ == '__main__':
    main(parse_args())
