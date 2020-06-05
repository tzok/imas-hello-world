Introduction
============

This guide describes how to use custom codes with IMAS Docker image.

Steps
=====

Execute all of these steps on your local computer.

1.  Get the IMAS Docker image:

        scp login.eufus.eu:~g2tomz/public/imas-fc2k-latest.tar.xz ./
        # or alternatively
        scp hpc-login02.iter.org:~zokt/public/imas-fc2k-latest.tar.xz ./

2.  Load the image:

        xzcat imas-fc2k-latest.tar.xz | docker load

3.  Start an interactive session within the IMAS environment:

        docker run -it --rm imas/fc2k

    **Note**: The session is ready to use from the start -- all
    necessary environment variables are set

4.  Get your custom code in the container:

        git clone https://github.com/tzok/imas-hello-world.git

    **Note:** This repository has IMAS `Hello World!` examples for IMAS
    in C++, Fortran, Java and Python. All codes create `summary` IDS in
    `shot=1` and `run=1` with a specific value in `comment` field. There
    is also a Python script `read.py` which reads that from the
    pulsefile and prints that out

5.  Try all variants of Hello World! examples:

        cd ~/imas-hello-world/cpp
        make
        ./hello
        ../python/read.py
        # Hello World from C++

        cd ~/imas-hello-world/fortran
        make
        ./hello
        ../python/read.py
        # Hello World from Fortran

        cd ~/imas-hello-world/java
        make
        make run
        ../python/read.py
        # Hello World from Java

        cd ~/imas-hello-world/python
        ./hello.py
        ./read.py
        # Hello World from Python
