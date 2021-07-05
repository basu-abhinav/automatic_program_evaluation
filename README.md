# Automatic Program Evaluation

This is an illustration for a case study based on two programs each having two candidate solutions. To get started, please ensure the following dependencies are satisfied.


## Dependencies

### Docker:

Check out the following guides for installation instructions on Ubuntu:

Ubuntu: https://docs.docker.com/engine/install/ubuntu/

For other Linux distributions, visit https://hub.docker.com/search?offering=community&operating_system=linux&q=&type=edition


### KLEE:

KLEE can be installed by many ways. For an extensive guide visit https://klee.github.io/getting-started/

We recommend using the KLEE images for Docker. For more info visit https://klee.github.io/docker/

This illustration has been tested on KLEE version 2.1. Hence we recommend using this particular version for best results.


### CBMC

CBMC is available forLinux. This illustration has been tested on CBMC version 5.11 (cbmc-5.11). Hence we recommend using this particular version for best results. For detailed installation instructions, visit https://www.cprover.org/cbmc/


### Python3:

Installing Python3 on your system is easy. For detailed installation instructions visit https://www.python.org/downloads/



## Instructions

There are two programs in this illustration, "triangle_type" and "merge_arrays", each contained in the directory with the same name respectively.




### 1. triangle_type

There is the golden solution in both C and Python, with filenames "golden.c" and "golden.py" respectively. There are two candidate solutions with filenames "triangle_1.py" and "triangle_2.py".

To evaluated these two candidate solutions, the following needs to be done:

1. Start the docker daemon with the following command:

    sudo systemctl start docker

2. Launch a docker container inside the "triangle_type" directory with the following command:

    sudo docker run -v $(pwd):/home/klee/local --rm -ti --ulimit='stack=-1:-1' klee/klee

3. Change directory to $(pwd):/home/klee/local with the following command:

    cd local

4. There is an "execute.sh" script to evaluate the candidate solutions. It takes the filename of the solution as argument. To evaluate the candidate solutions use the following commands respectively for "triangle_1.py" and "triangle_2.py":

    bash execute.sh triangle_1.py

    or

    bash execute.sh triangle_2.py


The score out of 100 will be displayed on the terminal.





### 2. merge_arrays

There is the golden solution in both C and Python, with filenames "golden.c" and "golden.py" respectively. There are two candidate solutions with filenames "merge_1.py" and "merge_2.py".

To evaluated these two candidate solutions, the following needs to be done:

1. There is an "execute.sh" script to evaluate the candidate solutions. It takes the filename of the solution as argument. To evaluate the candidate solutions use the following commands respectively for "merge_1.py" and "merge_2.py":

    bash execute.sh merge_1.py

    or

    bash execute.sh merge_2.py


The score out of 100 will be displayed on the terminal.
