#
#
#

import sys

import GEMx

def help():
    print("""
    mkmod [src dir] [dest]

    other options:

    -template:
        core
        lib
        app

        [dest]
    """

def main():
    if len(sys.argv) < 3:
        help()
        exit(1)

    if sys.argv[1] == "-template":
        if len(sys.argv) < 4):
            help()
            exit(1)

        template = sys.argv[2]
        if template not in GEMx.list_templates():
            print("{template} is not installed as a template".format(template=template))
            exit(1)

        tar_ = GEMx.get_template(template)

        dest_dir = sys.argv[3]
        tar_.extractall(dest_dir)

