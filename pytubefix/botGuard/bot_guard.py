import os
import subprocess
import shutil

os.environ["PATH"] += os.pathsep + "C:\\Program Files\\nodejs"

NODE_PATH = os.path.abspath(shutil.which("node"))
NODE_PATH = 'node' if NODE_PATH == None else NODE_PATH

if not os.path.isfile(NODE_PATH):
    NODE_PATH = 'node'

VM_PATH = os.path.dirname(os.path.realpath(__file__)) + r'/vm/botGuard.js'

def generate_po_token(visitor_data: str) -> str:
    """
    Run nodejs to generate poToken through botGuard.

    Requires nodejs installed.
    """
    result = subprocess.check_output(
        [NODE_PATH, VM_PATH, visitor_data]
    ).decode()
    return result.replace("\n", "")
    
