# -*- coding: utf-8 -*-

from src.red_black_tree import *


def test_rotate_when_target_is_right():
    """
    p              p
    ├─┐            ├─┐
      y              x
      ├───┐  right   ├───┐
      x   c  --->    a   y
      ├─┐    <---        ├─┐
      a b    left        b c
    """
    return


def test_rotate_when_target_is_left():
    """
    p              p
    ├─┐            ├─┐
    y              x
    ├───┐  right   ├───┐
    x   c  --->    a   y
    ├─┐    <---        ├─┐
    a b    left        b c
    """
    return


def test_rotate_when_target_is_root():
    """
    y              x
    ├───┐  right   ├───┐
    x   c  --->    a   y
    ├─┐    <---        ├─┐
    a b    left        b c
    """
    return
