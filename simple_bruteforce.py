#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from struct import pack
from syss_crc import CRC

# main
if __name__ == "__main__":
    # find configuration by brute force
    print("[*] Simple CRC configuration brute force test")

    # set custom config
    custom_conf = {'width': 8, 'poly': 0x31, 'init': 0xFF, 'refin': False, 'refout': True, 'xorout': 0x55, 'check': 0x00}
    crc = CRC()
    crc.set_config(custom_conf)

    # create test targets
    target = []
    for i in range(3):
        data = b"Test your might!" + pack("B", i)
        target_crc = crc.compute(data)
        target.append((data, target_crc))

    # try to find the CRC configuration
    config = crc.find_config(8, target)
    if config is None:
        print("[-] Could not find a suitable CRC configuration for the test parameters")
    else:
        print("[+] Found a suitable CRC configuration: {}".format(config))
