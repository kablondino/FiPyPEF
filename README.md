# FiPyPEF: FiPy Plasma Edge Fluxes

## Requirements and Installation
* Python3
* [FiPy](https://www.ctcms.nist.gov/fipy/ "FiPy Homepage")

It is recommended to use the [Anaconda](https://www.anaconda.com/download/ "Download Anaconda") package management system included in Anaconda.
It handles the additional required packages needed by FiPy, such as numpy and scipy.
For a more-minimal approach, use only the package manager [conda](https://conda.io/miniconda.html "Download Miniconda").
Make sure you download the Python3 version.

Upon completing the installation of conda, follow the instructions from FiPy to install the software:
[Installation Instructions](https://www.ctcms.nist.gov/fipy/INSTALLATION.html "Instructions")
Currently, the command to install the environment is this:
```
conda install --name NAME --channel conda-forge python=3.6 fipy
```

Please use git to manage any updates.
In order to get this code, simply execute the following command in the location of your choice.
```
git clone https://github.com/kablondino/FiPyPEF.git
```
Don't forget to activate your conda environment!
Substitute the name that you gave it.
```
conda activate NAME
```

It has not been tested in the [Jupyter notebook](http://jupyter.org/ "Jupyter").

## Use
The main routine of solving the system is in the `solving_taylor.py` and `solving_flux.py` files.
On the command line, run `python solving_taylor.py CONFIG_FILE.py` with the appropriate configuration file.
Read through the example configuration file `taylor_config.py` to see all of the options available.

Currently, there are 6 total nonambipolar fluxes implemented.
Read `Model_Notes.html` in a browser to see the forms of all the plasma parameters and fluxes without needing to sift through code.

