import unittest
from plot import *

class TestPlot(unittest.TestCase):
    def test1(self):
        plot1 = Plot('cpu1')
        plot1.ymax = 100
        plot1.addline([1,1,1,1])
        plot1.addline([2,2,2,2])
        plot2 = Plot('cpu2')
        plot2.addline([3,3,3,3])
        plot2.addline([4,4,4,4])
        plot2.ymax = 100

        plot3 = Plot('mem1')
        plot3.addline([1,1,1,1])
        plot3.addline([2,2,2,2])
        plot4 = Plot('mem2')
        plot4.addline([3,3,3,3])
        plot4.addline([4,4,4,4])

        c = Canvas()
        c.add_plot(plot1,'cpu')
        c.add_plot(plot2,'cpu')
        c.add_plot(plot3,'mem')
        c.add_plot(plot4,'mem')
        c.save_fig('/tmp/ex.png')

