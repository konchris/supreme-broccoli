#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase

from supreme_broccoli.hw import hw

class TestHW(TestCase):
    def test_is_string(self):
        s = hw()
        self.assertTrue(isinstance(s, str))
