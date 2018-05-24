# FiPyPEF: FiPy Plasma Edge Fluxes

## Requirements
* Python2
* [FiPy](https://www.ctcms.nist.gov/fipy/ "FiPy Homepage")

It is recommended to use the [Anaconda](https://www.anaconda.com/download/ "Download Anaconda") package management system included in Anaconda.
It handles the additional required packages needed by FiPy, such as numpy and scipy.
For a more-minimal approach, use only the package manager [conda](https://conda.io/miniconda.html "Download Miniconda").
Make sure you download the Python2 version.

## Use
The main routine of solving the system is in the `solving_taylor.py` and `solving_flux.py` files.
On the command line, run `python solving_taylor.py CONFIG_FILE.py` with the appropriate configuration file.
Read through the example configuration file `taylor_config.py` to see all of the options available.

Currently, there are 6 total nonambipolar fluxes implemented.
Read `Model_Notes.html` in a browser to see the forms of all the plasma parameters and fluxes without needing to sift through code.

