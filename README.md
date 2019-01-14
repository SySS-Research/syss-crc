# SySS CRC

Simple Python CRC implementation for playing around with cyclic redundancy checks, for instance when analyzing undocumented protocols or file formats.

Inspired by
* [Online CRC Calculator](https://crccalc.com/) by Anton Isakov 
* [Sunshine2k's CRC Calculator](http://www.sunshine2k.de/coding/javascript/crc/crc_js.html) by Bastian Molkenthin

## Usage

```
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
```

## Disclaimer

Use at your own risk. Mainly for educational and tinkering purposes.
