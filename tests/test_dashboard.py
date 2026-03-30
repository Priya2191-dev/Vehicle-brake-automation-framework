import os
import pytest
from dashboard import plot


def test_plot_creation():
    speed = [10, 20, 30]
    pressure = [5, 10, 15]

    plot(speed, pressure)

    assert os.path.exists("plot.png")


def test_plot_overwrite():
    speed = [1, 2, 3]
    pressure = [3, 2, 1]

    plot(speed, pressure)

    assert os.path.exists("plot.png")


def test_invalid_input_length():
    speed = [10, 20]
    pressure = [5]

    with pytest.raises(ValueError):
        plot(speed, pressure)


def test_empty_input():
    speed = []
    pressure = []

    plot(speed, pressure)

    assert os.path.exists("plot.png")
