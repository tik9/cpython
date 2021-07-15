import unittest
from os import path,scandir

def main():
    unittest.main()

def sort_files(folder):
    # entries = sorted((e for e in os.scandir(folder)),
    #  key=lambda f: f.name)
    entries = sorted((e for e in scandir(folder)
                      if e.is_file()), key=lambda e: e.stat().st_mtime)
    return [e.path for e in entries]

class TestHelper(unittest.TestCase):
    
    def test_sortfiles(self):
        dir = path.join('', '')
        self.assertEqual(sort_files(dir), ['C:\\Users\\User\\pictures\\bd\\unbenannt17.PNG',
                                          'C:\\Users\\User\\pictures\\bd\\unbenannt22.PNG'], 'Sort Dir')


if __name__ == "__main__":
    main()