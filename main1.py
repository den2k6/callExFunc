#! /usr/bin/env python3

import subprocess

def main():
    print('Hello from main1')
    # subprocess.run(['python3', 'sub1.py'])
    subprocess.run(['./sub1.py'])

if __name__ == '__main__':
    main()

