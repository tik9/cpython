import unittest
from os import path, scandir


def main():
    unittest.main()


def sort_files(folder):
    # entries = sorted((e for e in os.scandir(folder)),
    #  key=lambda f: f.name)
    entries = sorted((e for e in scandir(folder) if e.is_file()),
                     key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]


class TestHelper(unittest.TestCase):

    def test_sortfiles(self):
        dir = path.join('c', 'test')
        print(dir)
        self.assertEqual(sort_files(dir), [path.join(
            'c', 'test', 'test1.txt'), path.join('c', 'test', 'test2.txt')], 'sorting..')


if __name__ == "__main__":
    main()
