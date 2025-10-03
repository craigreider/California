import sys
import os
from datetime import datetime
import site
"""
python -c "import os; help(os)"
"""
def os_clear():
    os.system("cls" if os.name == "nt" else "clear")
    
def info():
    os.system("cls")
    time_info()
    dashdash=['help','version','help-env','help-all','help-all','help-xoptions','']
    help_info(dashdash[0])
    os_info()
    sys_info()

def help_info(help_type):
    make_label('help_info')
    print(f'os.system: {os.system(f'python --{help_type}')}')

def time_info():
    make_label('time_info')
    print(f'datetime.now: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')   

def os_info():
    make_label('os_info')
    print(f'os.name: {os.name}')
    print(f'os.getpid: {os.getpid()}')

def sys_info():
    make_label('sys_info')
    print(f'sys.executable: {sys.executable}')
    print(f'sys.version: {sys.version}')
    print(f'sys.api_version: {sys.api_version}')
    print(f'sys.implementation: {sys.implementation}')
    print(f'sys.int_info: {sys.int_info}')
    print(f'sys.float_info: {sys.float_info}')
    print(f'sys.hash_info: {sys.hash_info}')
    print(f'sys.version_info: {sys.version_info}')
    print(f'sys.maxsize: {sys.maxsize}')
    print(f'sys.maxunicode: {sys.maxunicode}')

def show_path():
    make_label('show_path')
    for path in sys.path:
        print(f'path: {path}')

def show_cur_dir():
    make_label('show_cur_dir')
    print(f'cwd: {os.getcwd()}')

def show_exec_path():
    make_label('show_exec_path')
    for exec_path in os.get_exec_path():
        print(f'exec path: {exec_path}')

def show_site_packages():
    make_label('show_site_packages')
    for package in site.getsitepackages():
        print(f'sit getsitpackages: {package}')

def show_env(starts=('',)):
    make_label('show_env')
    for k,v in os.environ.items():
        if k.upper().startswith(tuple(start.upper() for start in starts)):
            print(f'env: {k}={v}')

def show_pth():
    make_label('show_pth')   
    site_packages_dirs = site.getsitepackages() # list of site directories

    print("Searching for .pth files in the following site dir:")
    for site_dir in site_packages_dirs:
        print(f"- {site_dir}")
        if os.path.exists(site_dir):
            for filename in os.listdir(site_dir):
                if filename.endswith(".pth"):
                    pth_file_path = os.path.join(site_dir, filename)
                    print(f"  Found: {pth_file_path}")
                    try:
                        with open(pth_file_path, 'r') as f:
                            print("    Contents:")
                            for line in f:
                                print(f"      {line.strip()}")
                    except Exception as e:
                        print(f"    Error reading {pth_file_path}: {e}")

def make_label(label,pre=40,post=40):
    print(f'{pre*'_'}{label}{post*'_'}')

def show_main():
    print(f'____________________________________MAIN Info______________________________')
    print(f'__name__: {__name__}')