from helper import *
from settings import answers,example,prodMd

def main():
    unittest.main()


class TestHelper(unittest.TestCase):
    
    def test_answercount(self):
        answersExample =  [2, 1, 2]
        self.assertEqual(countqa(prodMd),[4]*18,'Number of answers')

    # def test_answer(self):
    #     with open(example, 'r') as f:
    #         line = f.readline()
    #         line = f.readline()
    #     answer = '- [] This is the answer 1\n'
    #     answerNumber = 4
    #     acount = 1
    #     self.assertEqual(lineAnswer(line, answerNumber, acount),
    #                      answer, 'Correct answer')

    # def test_sortfiles(self):
        # dir = path.join(pics, '')
        # self.assertEqual(sortfiles(dir), ['C:\\Users\\User\\pictures\\bd\\unbenannt17.PNG',
    #                                       'C:\\Users\\User\\pictures\\bd\\unbenannt22.PNG'], 'Sort Dir')

    # def test_needle(self):
        # str1 = 'COTest'
        # self.assertEqual(needles(str1), 'Test', "Should remove")

    # def test_match(self):
    # file = 'unbenannt.png.png'
    #     self.assertEqual(does_string_match(file), False, 'Be false')

    # def test_code(self):
        # cod = ('', False, 'python')
    #     self.assertEqual(code(*cod), ('\n```python\n', True))

if __name__ == "__main__":
    main()