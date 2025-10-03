import importlib
import sys
import util.show_config as show_config
importlib.reload(show_config)

def main():
    show_config.os_clear()
    print(f'__name__: {__name__}')
    # show_config.info()
    # show_config.show_cur_dir()
    show_config.show_path()
    # show_config.show_exec_path()
    # show_config.show_env(('a','p','t'))
    #show_config.show_main()
    # for item in sys.path:
    #         print(f'California.py path: {item}')

    show_config.show_pth()

if __name__=="__main__":
    main()