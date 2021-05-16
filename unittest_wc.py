import unittest
import word_count

class testCaseWordCount(unittest.TestCase):
        def test_normal_case(self):
                self.assertEqual(word_count.wCount("Hi, my name is Emily"), 5)
        def test_empty_string(self):
                self.assertEqual(word_count.wCount(""), 0)
        def test_space(self):
                self.assertEqual(word_count.wCount(" "), 0)

if __name__ == '__main__':
        unittest.main()
