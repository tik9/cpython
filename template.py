from pathlib import Path
import sys

home = str(Path.home())

# print(home)


def main():
    content_ = content()
    print(content_)


def content():
    pass


def version():
    python_ver = sys.version_info
    major = sys.version_info.major
    minor = sys.version_info.minor


if __name__ == "__main__":
    main()
