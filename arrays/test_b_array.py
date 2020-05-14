from unittest import TestCase, main

from arrays.b_array import BArray


class TestBArray(TestCase):

    def test_remove_value(self):
        arr = BArray([1, 2, 3, 1, 2, 3])

        expected = [2, 3, 2, 3]
        arr.remove_value(1)
        actual = arr.get_data()
        self.assertEqual(expected, actual)

        arr.remove_value(9)
        self.assertEqual(expected, actual)

        arr.remove_value(3)
        expected = [2, 2]
        actual = arr.get_data()
        self.assertEqual(expected, actual)

        arr.remove_value(2)
        expected = []
        actual = arr.get_data()
        self.assertEqual(expected, actual)

    def test_remove_indices(self):
        arr = BArray([0, 1, 2, 3, 4, 5])

        arr.remove_indices([0, 1, 2])
        expected = [3, 4, 5]
        actual = arr.get_data()
        self.assertEqual(expected, actual)

        arr.remove_indices([0, 1, 2])
        expected = []
        actual = arr.get_data()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
