#!/usr/bin/env python
# coding: utf-8

from unittest import TestCase

from supreme_broccoli.cli_test import main

class TestConsole(TestCase):
    def test_basic(self):
        main()
