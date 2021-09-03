#! /usr/bin/env python3

import subprocess

def main():
    print('Hello from main1')
    res = subprocess.run(['python3', 'sub1.py'])
    # res = subprocess.run(['./sub1.py'])
    print(f'return code: {res.returncode}')

if __name__ == '__main__':
    main()
