import sys
import assignment_001.py

import pytest

from skimage import data, color
import matplotlib.pyplot as plt
import numpy as np
from numpy.testing import assert_array_equal

@pytest.fixture
def task1_input():
    np.random.seed(10)
    task1_input = np.random.rand(30, 40)
    return task1_input


@pytest.fixture
def kernel():
    kernel = (1 / 9) * np.ones((3, 3))
    return kernel


def test_GaussFilter(task1_input, kernel):
    image_pad, image_filtered = assignment_001.GaussFilter(task1_input, kernel)
    task1_pad = np.load('task1_pad.npy')
    task1_output = np.load('task1_output.npy')
    assert_array_equal(image_pad, task1_pad)
    assert_array_equal(image_filtered, task1_output)


@pytest.fixture
def task2_input():
    np.random.seed(10)
    task2_input = np.random.rand(30, 40)
    return task2_input


@pytest.fixture
def task2_mask():
    kernel = (1 / 9) * np.ones((3, 3))
    return task2_mask


@pytest.fixture
def task2_output():
    kernel = (1 / 9) * np.ones((3, 3))
    return task2_output


@pytest.fixture
def threshold():
    threshold = 0.8
    return threshold


def test_thresholding(task2_input, threshold):
    mask, threshold_image = assignment_001.thresholding(task2_input, threshold)
    task2_mask = np.load('task2_mask.npy')
    task2_output = np.load('task2_output.npy')
    assert_array_equal(mask, task2_mask)
    assert_array_equal(threshold_image, task2_output)
