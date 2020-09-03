#! /usr/bin/env python
import os
import pwd
import imas

if __name__ == '__main__':
    uid = os.getuid()
    pw = pwd.getpwuid(uid)

    pulsefile = imas.ids(1, 1)
    pulsefile.open_env(pw.pw_name, 'test', '3')

    summary = pulsefile.summary
    summary.get()
    print(summary.ids_properties.comment)

    pulsefile.close()
