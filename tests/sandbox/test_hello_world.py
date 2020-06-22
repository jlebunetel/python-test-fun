#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
Hello World tests
"""

import unittest


from sandbox.hello_world import additionner


class AdditionnerTestCase(unittest.TestCase):
    def test_additionner_un_plus_un(self):
        self.assertEqual(additionner(1, 1), 2)

    def test_additionner_un_plus_un_egal_trois(self):
        self.assertEqual(additionner(1, 1), 3)


if __name__ == "__main__":
    unittest.main()
