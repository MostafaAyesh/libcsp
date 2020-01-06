#!/usr/bin/env python
# encoding: utf-8

import subprocess
import sys

cmd_options = sys.argv[1:]

options = [
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

linux_options = [
    # '--enable-bindings',
    '--enable-python3-bindings',
    # '--enable-can-socketcan',
    # '--with-driver-usart=linux',
    '--with-os=posix',
    # '--enable-if-zmqhub'
]

# Build
subprocess.check_call(['./waf', 'distclean', 'configure', 'build'] + options + linux_options + cmd_options +
                      ['--enable-init-shutdown', '--with-rtable=cidr', '--disable-stlib', '--disable-output'])
subprocess.check_call(['./waf', 'distclean', 'configure', 'build'] + options + linux_options + cmd_options +
                      ['--enable-examples'])
