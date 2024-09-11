import unittest

from hamon.main import count_elements


class TestCountElements(unittest.TestCase):

    def test_string_input(self):
        self.assertEqual(count_elements('apple'), {
                         'a': 1, 'p': 2, 'l': 1, 'e': 1})

    def test_list_input(self):
        self.assertEqual(count_elements([1, 2, 2, 1]), {1: 2, 2: 2})

    def test_empty_input(self):
        self.assertEqual(count_elements(''), {})
        self.assertEqual(count_elements([]), {})

    def test_single_element_input(self):
        self.assertEqual(count_elements('a'), {'a': 1})
        self.assertEqual(count_elements([42]), {42: 1})

    def test_tuple_input(self):
        self.assertEqual(count_elements(
            (1, 2, 2, 3, 3, 3)), {1: 1, 2: 2, 3: 3})

    def test_non_iterable_input(self):
        with self.assertRaises(TypeError):
            count_elements(42)
