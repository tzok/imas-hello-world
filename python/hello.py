#! /usr/bin/env python
import imas

if __name__ == '__main__':
    pulsefile = imas.ids(1, 1)
    pulsefile.create_env('imas', 'test', '3')

    summary = pulsefile.summary
    summary.ids_properties.comment = 'Hello World from Python!'
    summary.ids_properties.homogeneous_time = 1
    summary.time.resize(1)
    summary.time[0] = 0.1
    summary.put()

    pulsefile.close()
