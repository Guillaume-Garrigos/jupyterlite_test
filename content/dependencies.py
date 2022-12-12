module_list = ['ipywidgets', 'ipympl', 'addict', 'autograd']

import sys
import importlib
if "pyodide" in sys.modules: # we are in a jupyter lite environment
    # code taken from https://github.com/jupyterlite/jupyterlite/issues/816
    import piplite
    install = lambda string: piplite.install(string)
else: # we are in a classic jupyter environment
    import subprocess
    install = lambda string: subprocess.check_call([sys.executable, "-m", "pip", "install", string])

for module in module_list:
    try:
        # https://stackoverflow.com/questions/301134/how-can-i-import-a-module-dynamically-given-its-name-as-string
        importlib.import_module(module) 
    except:
        install(module)