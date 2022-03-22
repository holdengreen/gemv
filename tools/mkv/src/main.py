#
#
#

import sys
import os

#import colorful as cf

valid_targets = [
    "browser",
    "virt"
]

print("# valid targets: " + str(valid_targets))
target = input("which target?: ")

if target not in valid_targets:
    print("{0} is not a valid target".format(target))
    exit(1)


def build_image():
    pass

