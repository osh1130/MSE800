import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        # Checks if 'foo'.upper() returns 'FOO'
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        # Checks if 'FOO' is all uppercase (should be True)
        self.assertTrue('FOO'.isupper())
        # Checks if 'Foo' is all uppercase (should be False)
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        # Checks if 'hello world'.split() returns ['hello', 'world']
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Checks if passing a non-string separator raises TypeError
        with self.assertRaises(TypeError):
            s.split(2)

    def test_isdigit(self):
        # Checks if '123'.isdigit() returns True
        self.assertTrue('123'.isdigit())

if __name__ == '__main__':
    # If any assertion fails, unittest will stop at that point in the test,
    # display which test failed, the line number, and show the expected vs actual result.
    unittest.main()
