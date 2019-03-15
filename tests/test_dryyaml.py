#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `dryyaml` package."""

import os

import pytest

from dryyaml import render


test_files_dir = os.path.join(os.path.dirname(__file__), 'test_files')
# test pair paths have input.yaml and output.yaml
test_pair_paths = [os.path.join(test_files_dir, f) for f in os.listdir(test_files_dir)]


@pytest.mark.parametrize("test_pair_path", test_pair_paths)
def test_all_pairs(test_pair_path):

    with open(os.path.join(test_pair_path, "input.yaml")) as fil_in:
        with open(os.path.join(test_pair_path, "output.yaml")) as fil_out:
            assert render(fil_in) == fil_out.read()


# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string
