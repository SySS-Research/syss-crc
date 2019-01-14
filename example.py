#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from syss_crc import CRC

# main
if __name__ == "__main__":
    # simple usage example
    crc = CRC()
    crc.set_config_by_name("CRC-32")
    data = b"What's my CRC again?"
    c = crc.compute(data)
    print("[*] CRC-32 of test data '{:s}' is {:X}".format(data.decode("UTF-8"), c))
