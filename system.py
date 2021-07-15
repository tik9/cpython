# https://stackoverflow.com/a/30990617/1705829

import socket
from os.path import isdir, join
import os
import shutil


def main():
    # copy_packages()
    # print(1)
    ip_add = get_ip_address()
    print(ip_add)


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    return s.getsockname()


def copy_packages():
    dist = 'dist-packages'
    dist_dirs = [join('/usr/local/lib/python3.8/', dist),
                 join('/usr/lib/python3', dist)]
    site_dir = '/home/tk/.local/lib/python3.8/site-packages'
    # print (site_dir)

    for dist_dir in dist_dirs:
        if isdir(dist_dir):
            file_names = os.listdir(dist_dir)

            for file_name in file_names:
                # print(file_name)
                shutil.move(join(dist_dir, file_name),
                            join(site_dir, file_name))
            shutil.rmtree(dist_dir)
        os.symlink(site_dir, dist_dir)


if __name__ == '__main__':
    main()
