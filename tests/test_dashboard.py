import os
from dashboard import plot  

def test_plot_creation():
    speed = [10, 20, 30]
    pressure = [5, 10, 15]

    plot(speed, pressure)

    assert os.path.exists("plot.png")
