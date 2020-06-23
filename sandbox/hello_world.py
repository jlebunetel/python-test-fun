#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""
Hello World demo library
"""


def additionner(a, b):
    """Fonction qui renvoie la somme de deux nombres."""

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    return a + b


if __name__ == "__main__":
    print("1 + 1 = ", additionne(1, 1))
