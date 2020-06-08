Introduction
============

This guide describes how to use custom codes with IMAS Docker image.

Requirements
============

-   Install [Docker](https://www.docker.com/) on your local computer:
    follow the official
    [documentation](https://docs.docker.com/get-docker/)

-   Or [uDocker](https://github.com/indigo-dc/udocker) on an HPC
    machine:

        mkdir -p $HOME/.local/opt
        wget https://github.com/indigo-dc/udocker/releases/download/devel3_1.2.4/udocker-1.2.4.tar.gz
        tar xf udocker-1.2.4.tar.gz -C $HOME/.local/opt
        export PATH=$PATH:$HOME/.local/opt/udocker

        # to make the change permanent on current machine
        echo 'export PATH=$PATH:$HOME/.local/opt/udocker' >> ~/.bashrc

Steps
=====

1.  Get the IMAS Docker image:

        scp login.eufus.eu:~g2tomz/public/imas-fc2k-latest.tar.xz ./
        # or alternatively
        scp hpc-login02.iter.org:~zokt/public/imas-fc2k-latest.tar.xz ./

2.  Load the image:

        xzcat imas-fc2k-latest.tar.xz | docker load

    Or for uDocker on HPC:

        xzcat imas-fc2k-latest.tar.xz | udocker load

3.  Start an interactive session within the IMAS environment:

        docker run -it --rm imas/fc2k

    Or for uDocker on HPC:

        udocker create --name=imas imas/fc2k:3.28.1-4.7.3-2.5p5-3.1.1-4.10.1
        udocker run imas

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
