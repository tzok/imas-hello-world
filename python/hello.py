#! /usr/bin/env python
import os
import pwd
import imas

if __name__ == '__main__':
    uid = os.getuid()
    pw = pwd.getpwuid(uid)

    pulsefile = imas.ids(1, 1)
    pulsefile.create_env(pw.pw_name, 'test', '3')

    summary = pulsefile.summary
    summary.ids_properties.comment = 'Hello World from Python'
    summary.ids_properties.homogeneous_time = 1
    summary.time.resize(1)
    summary.time[0] = 0.1
    summary.put()

    pulsefile.close()
