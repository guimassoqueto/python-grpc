from unittest import TestCase


class TestAny(TestCase):
    def test_any(self):
        a = True
        b = True

        self.assertEqual(a, b)
