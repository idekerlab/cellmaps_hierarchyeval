#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `cellmaps_hierarchyeval` package."""


import unittest
from cellmaps_hierarchyeval.runner import CellmapshierarchyevalRunner


class TestCellmapshierarchyevalrunner(unittest.TestCase):
    """Tests for `cellmaps_hierarchyeval` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_constructor(self):
        """Tests constructor"""
        myobj = CellmapshierarchyevalRunner(0)

        self.assertIsNotNone(myobj)

    def test_run(self):
        """ Tests run()"""
        myobj = CellmapshierarchyevalRunner(4)
        self.assertEqual(4, myobj.run())
