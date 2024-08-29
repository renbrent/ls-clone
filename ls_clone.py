import os
import sys
import stat
from datetime import datetime


def ls(filepath='.', show_all=False, show_long=False):
    try:
        entries = os.listdir(filepath)
        if not show_all:
            entries = [entry for entry in entries if not entry.startswith('.')]
        
        entries.sort()

        for entry in entries:
            if show_long:
                full_path = os.path.join(filepath, entry)
                file_stat = os.stat(full_path)

                file_mode = stat.filemode(file_stat.st_mode)

                n_links = file_stat.st_nlink

                owner = get_username(file_stat.st_uid)
                group = get_username(file_stat.st_gid)

                size = file_stat.st_size

                mod_time = datetime.fromtimestamp(file_stat.st_mtime).strftime('%Y-%m-%d %H:%M')

                print(f"{file_mode} {n_links} {owner} {group} {size:>8} {mod_time} {entry}")
            else:
                print(entry)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied for '{path}'.")

def get_username(uid):
    try:
        import pwd
        return pwd.getpwuid(uid).pw_name
    except ImportError:
        return str(uid)


def main():
    filepath = '.'
    show_all = False
    show_long = False

    args = sys.argv[1:]
    if "-a" in args:
        show_all = True
    if "-l" in args:
        show_long = True
    if len(args) > 0 and not args[0].startswith('-'):
        filepath = args[0]

    ls(filepath, show_all, show_long)

if __name__ == "__main__":
    main()
