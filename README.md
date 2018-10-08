# A set of Tutorials on Machine Learning

This repo contains a bunch of tutorials ranging from machine learning intro, best practices to deep learning. Each folder is a tutorial on a different topic. Check the folder's README file to know what the tutorial is about. These are created completely based on my personal hands on experiences and are usually practical in nature. Please raise "issues" on github if you have any suggestions or would like to let me know if you found any of these useful. Thanks a lot :)

## Dev Setup

We extensively use [Jupyter notebooks](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/) for all the tutorials due to their ease of use and community support to run on a cloud machine without the need for any set up to quickly get started. 

However, code reviewing a jupyter notebook can be challenging in an office project, at least as of Sep 2018, as the source file (.ipynb) has a lot of meta information other the code we write. If this is not a requirement for you, safely skip the rest of the section, but it might be a good practice to set it up once and forget it for any jupyter notebook project in the future. A simple solution to the above problem is to auto generate the corresponding python file and get that reviewed instead. HTML file can also be generate to quickly view the visual content of the notebook as well in any browser. To achieve this replace the file at **~/.jupyter/jupyter_notebook_config.py** with the one in this folder. The file adds simple hooks which save the python and HTML files in a sub folder (to the .ipynb file) called "auto-generated" whenever .ipynb file is saved.