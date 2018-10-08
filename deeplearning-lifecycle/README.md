## Dev Setup

These instructions are for Mac but should mostly work as is on Linux OS as well
- Install Miniconda for Mac from https://conda.io/miniconda.html
- `conda create -name=env python=3.6` creates an sandboxed environment so that any libraries installed will not conflict with the ones needed for other projects using globally / system-wide installed libraries
- `conda install psutil` is needed for ray and does not install properly on a Mac using `pip`. May work with `pip` on a linux machine
- `pip install requirements.txt`
- `jupyter notebook`
