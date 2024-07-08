#!/usr/bin/env python3
import argparse
import subprocess
import sys
import os

def parse_args():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--notebook', type=str, help='The notebook to execute.', required=True)
    parser.add_argument('--offline', type=bool, help='Set environment variables so that huggingface will not access the internet.', required=True)

    return parser.parse_args()


def main(args):
    if args.offline:
        print("I set environment variables HF_HUB_OFFLINE and OFFLINE.")
        os.environ["HF_HUB_OFFLINE"] = "1"
        os.environ["OFFLINE"] = "True"

    command = f'runnb --allow-not-trusted {args.notebook}'
    subprocess.check_call(command, shell=True, stdout=sys.stdout, stderr=subprocess.STDOUT)


if __name__ == '__main__':
    main(parse_args())
