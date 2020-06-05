IMAS Hello World! Collection
============================

This repository contains a collection of simple `Hello World!` programs
for IMAS. Examples are written in C++, Fortran, Java and Python.

C++
---

```cpp
#include <UALClasses.h>

int main() {
    IdsNs::IDS ids(1, 1, 0, 0);
    ids.createEnv("imas", "test", "3");

    ids._summary.ids_properties.comment = "Hello World from C++";
    ids._summary.ids_properties.homogeneous_time = 1;
    ids._summary.time.resize(1);
    ids._summary.time(0) = 0.1;
    ids._summary.put();

    ids.close();
    return 0;
}
```

Fortran
-------

```fortran
program test
    use ids_routines

    integer :: pulsectx, status;
    type(ids_summary) :: summary;

    call ual_begin_pulse_action(MDSPLUS_BACKEND, 1, 1, 'imas', 'test', '3', pulsectx)
    call ual_open_pulse(pulsectx, FORCE_CREATE_PULSE, '', status);

    allocate(summary%ids_properties%comment(1))
    summary%ids_properties%comment(1) = 'Hello World from Fortran'
    summary%ids_properties%homogeneous_time = 1;
    allocate(summary%time(1))
    summary%time(1) = 0.1

    call ids_put(pulsectx, "summary", summary)
    call ids_deallocate(summary)
    call ual_close_pulse(pulsectx, FORCE_CREATE_PULSE, '', status)
end program test
```

Java
----

```java
package pl.psnc.imas;

import imasjava.imas;
import imasjava.imas.summary;
import imasjava.UALException;
import imasjava.Vect1DDouble;

public class HelloWorld {
    public static void main(String[] args) throws UALException {
        int pulseCtx = imas.createEnv(1, 1, "imas", "test", "3");

        summary s = new summary();
        s.ids_properties.comment = "Hello World from Java!";
        s.ids_properties.homogeneous_time = 1;
        s.time = new Vect1DDouble(new double[] { 0.1 });

        imas.summary.put(pulseCtx, "summary", s);
    }
}
```

Python
------

```python
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
```
