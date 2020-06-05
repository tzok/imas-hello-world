#! /usr/bin/env python
import imas

if __name__ == '__main__':
    pulsefile = imas.ids(1, 1)
    pulsefile.create_env('imas', 'test', '3')

    ids = pulsefile.summary
    ids.ids_properties.comment = 'Hello World from Python!'
    ids.ids_properties.homogeneous_time = 1
    ids.time.resize(1)
    ids.time[0] = 0.1
    ids.put()

    pulsefile.close()
