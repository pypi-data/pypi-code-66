from unittest import TestCase

import yautil
import matplotlib.pyplot as plt


class TestPlot:
    plot: callable

    def test_basic(self):
        data = [0, 1, 2, 2, 3, 4]
        self.plot(data, block=False)
        plt.pause(1)
        plt.close()

    def test_xlabel(self):
        data = ['test values', 0, 1, 2, 2, 3, 4]
        self.plot(data, block=False)
        plt.pause(1)
        plt.close()

    def test_subfigures(self):
        data = [0, 1, 2, 2, 3, 4]
        self.plot(data, data, block=False)
        plt.pause(1)
        plt.close()

    def test_multi_lines(self):
        data1 = ['test values 1', 0, 1, 2, 2, 3, 4]
        data2 = ['test values 2', 1, 2, 2, 3, 4]
        self.plot((data1, data2), block=False)
        plt.pause(1)
        plt.close()


class TestPlotCdf(TestPlot, TestCase):

    def __init__(self):
        self.plot = yautil.plot_cdf
        super().__init__()


class TestPlotLinear(TestPlot, TestCase):

    def __init__(self):
        self.plot = yautil.plot_linear
        super().__init__()

