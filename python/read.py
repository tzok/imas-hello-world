#! /usr/bin/env python
import imas

if __name__ == '__main__':
    pulsefile = imas.ids(1, 1)
    pulsefile.open_env('imas', 'test', '3')

    ids = pulsefile.summary
    ids.get()
    print(ids.ids_properties.comment)

    pulsefile.close()
