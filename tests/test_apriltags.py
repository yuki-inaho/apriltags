#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `apriltags` package."""

import pytest


import apriltags3


@pytest.fixture
def detector():
    return apriltags3.Detector()


def test_detector_init(detector):
    print(detector)
