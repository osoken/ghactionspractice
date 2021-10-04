from unittest import TestCase


class DoNothingTestCase(TestCase):
    def test_always_pass(self) -> None:
        self.assertTrue(True)
