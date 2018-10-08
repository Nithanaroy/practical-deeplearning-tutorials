#!/usr/bin/env python
# coding: utf-8

# # Tensorflow Keras Model with Dataset API, Tensorboard, Profiling, Testing
# 
# In this short tutorial we will go over some important concepts which can be used in a deep learning project. We'll see why & how to set up a custom input pipeline using tf.dataset API, build a model using tf.keras API, watch the model training using tensorboard, profile the model to check resource utilization numbers and finally validate the model to see what it learned makes sense using 3 important techniques. Lots of exciting stuff, so lets get started!

# ## Development Environment

# Having a good development environment makes the experience smooth and fast to iterate. In this section, we will see some tips on setting up notebooks, environments and versioning your project.

# ### Jupyter Notebooks

# [Jupyter notebooks](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/), such as this document, need not introduction for their ease of use and immense abilities to code, document and visualize in a single place. 
# 
# However, [code reviewing](https://en.wikipedia.org/wiki/Code_review) a jupyter notebook can be challenging in an office project, at least as of Sep 2018, as the source file (.ipynb) has a lot of meta information other the code we write. If this is not a requirement for you, safely skip this section, but it might be a good practice to set it up as it is not that hard. 
# 
# A simple solution to code review problem is to auto generate the corresponding python file and get that reviewed instead. HTML file can also be generate to quickly view the visual contents of the notebook (charts and images) as well in any browser. To achieve this replace the file at **~/.jupyter/jupyter_notebook_config.py** with the one in this folder. The file adds simple hooks which save the python and HTML files in a sub folder (to the .ipynb file) called "auto-generated" whenever .ipynb file is saved.
