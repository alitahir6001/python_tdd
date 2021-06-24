import unittest
# Notice that we are now importing unittest

def sum_two(a,b):
    return a + b

# Create the MainTest class and pass it unit test

class MainTest(unittest.TestCase):
    # Each test will be a separate def, and the system knows to run any method whose name begins with 'test'
    def test_hello(self):
        return print("Hello from the tests class")

    def test_sum_two(self):
        returned_value = sum_two(5,7) # I created a variable called 'returned_value' and stored the answer of the function sum_two in it.
        self.assertEqual(returned_value, 12) # I took that variable, checked it against the hard-coded answer of 12, and using the assertEqual method, checked if they matched.
        self.assertEqual(sum_two(-5,5), 0)  # this is a 'one-liner' for the above two lines, where i call the def inside assertEqual, and code the answer after the comma.
        return print("Metroid rules")