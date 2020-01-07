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
    '--enable-promisc',
    '--enable-crc32',
    '--enable-hmac',
    '--enable-xtea',
    '--enable-dedup',
    '--enable-if-i2c',
    '--enable-if-kiss',
    '--enable-if-can',
    '--with-loglevel=debug',
]

waf = ['./waf']
if os in ['posix']:
    options += [
        '--enable-bindings',
        '--enable-python3-bindings',
        '--enable-can-socketcan',
        '--with-driver-usart=linux',
        '--enable-if-zmqhub'
    ]

if os in ['macosx']:
    options += [
    ]

if os in ['windows']:
    options += [
        # '--with-driver-usart=windows',
    ]
    waf = ['python', '-x', 'waf']

# Build
waf += ['distclean', 'configure', 'build']
print("Waf build command:", waf)
subprocess.check_call(waf + options +
                      ['--enable-qos', '--enable-init-shutdown', '--with-rtable=cidr', '--disable-stlib', '--disable-output'])
subprocess.check_call(waf + options +
                      ['--enable-examples'])
