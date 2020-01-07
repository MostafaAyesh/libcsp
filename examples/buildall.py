#!/usr/bin/env python
# encoding: utf-8

import subprocess
import sys

os = 'posix'  ## default OS
options = sys.argv[1:]

if (len(options) > 0) and not options[0].startswith('--'):
    os = options[0]
    options = options[1:]

options += [
    '--with-os=' + os,
    '--enable-rdp',
    '--enable-qos',
    '--enable-promisc',
    '--enable-crc32',
    '--enable-hmac',
    '--enable-xtea',
    '--enable-dedup',
    # '--enable-if-i2c',
    # '--enable-if-kiss',
    # '--enable-if-can',
]

if os in ['posix']:
    options += [
        # '--enable-bindings',
        '--enable-python3-bindings',
        # '--enable-can-socketcan',
        # '--with-driver-usart=linux',
        # '--enable-if-zmqhub'
    ]
    waf = ['./waf']

if os in ['macosx']:
    waf = ['./waf']

if os in ['windows']:
    waf = ['python', '-x', 'waf']

waf += ['distclean', 'configure', 'build']
print("Waf build command:", waf)

# Build
subprocess.check_call(waf + options +
                      ['--enable-init-shutdown', '--with-rtable=cidr', '--disable-stlib', '--disable-output'])
subprocess.check_call(waf + options +
                      ['--enable-examples'])
