# coding=utf-8
from __future__ import print_function, unicode_literals
from nose.tools import assert_equal
import mmm.math as mmath


def setUp():
    print("test math module setup")


def teardown():
    print("test math module teardown")


def test_math_add():
    result = mmath.add(4, 5)
    print("test_math_add")
    assert_equal(9, result)


class test_math3():
    def setUp(self):
        print("test math class setup")

    def teardown(self):
        print("test math class teardown")

    def test_math_square(self):
        print("test_math_square")
        assert_equal(9, mmath.square(3))

    def test_math_sub(self):
        print("test_math_sub")
        assert_equal(1, mmath.sub(3, 2))
