# Configuration file for jupyter-notebook.

def scrub_output_pre_save(model, **kwargs):
    """scrub output before saving notebooks"""
    # only run on notebooks
    if model['type'] != 'notebook':
        return
    # only run on nbformat v4
    if model['content']['nbformat'] != 4:
        return

    for cell in model['content']['cells']:
        if cell['cell_type'] != 'code':
            continue
        cell['outputs'] = []
        cell['execution_count'] = None

# c.ContentsManager.pre_save_hook = scrub_output_pre_save # Nitin commented this as he wanted to save the output as well

c = get_config()
### Auto-saves .html and .py versions of your notebook:
import os
from subprocess import check_call

def post_save(model, os_path, contents_manager):
    """post-save hook for converting notebooks to .py scripts"""
    if model['type'] != 'notebook':
        return # only do this for notebooks
    d, fname = os.path.split(os_path)
    destination_dir = os.path.join(d, "auto-generated")
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
    try:
        check_call(['jupyter', 'nbconvert', '--to', 'script', fname], cwd=d)
        check_call(['jupyter', 'nbconvert', '--to', 'html', fname], cwd=d)
    except:
        # for anaconda distributions
        check_call(['jupyter-nbconvert', '--to', 'script', fname], cwd=d)
        check_call(['jupyter-nbconvert', '--to', 'html', fname], cwd=d)


c.FileContentsManager.post_save_hook = post_save
