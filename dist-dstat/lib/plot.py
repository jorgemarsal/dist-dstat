from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

from constants import *
from mylogger import dr_logger

class Plot:
    def __init__(self,host,category,title=None,xlabel='time',ylabel=None,ymax=None):
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.ymax = ymax
        self.host = host
        if title:
            self.title = title
        else:
            self.title = category # default title is category
        self.lines = []

    def addline(self,line, label=''):
        self.lines.append((line,self.host + ' - ' + label))



class Canvas(object):
    def __init__(self):
        self.dict = OrderedDict()

    def add_plot(self,plot,category):
        """

        :param plot (list): one or more plots. If more than one use subplots
        :return:
        """
        if not category in self.dict: self.dict[category] = []
        self.dict[category].append(plot)

    def save_fig(self,filename):
        total = 0
        for category,plots in self.dict.iteritems():
            total += len(plots)

        f, axes = plt.subplots(total, sharex=True, sharey=False)
        f.set_size_inches(Constants.PLOT_WIDTH_INCHES,Constants.PLOT_HEIGHT_INCHES * len(axes))


        i = 0
        for category,plots in self.dict.iteritems():
            for p in plots:
                for line,label in p.lines:
                    axes[i].plot(line, label=label)
                if p.title:
                    axes[i].set_title(p.title,y=Constants.TITLE_Y)
                if p.ymax:
                    axes[i].set_ylim([0,p.ymax])
                if p.ylabel:
                    axes[i].set_ylabel(p.ylabel)
                axes[i].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                                   ncol=2, mode="expand", borderaxespad=0.)

                i += 1

        plt.tight_layout()
        plt.savefig(filename)

class CategoryCanvas(Canvas):
    '''Have only 1 plot per category, different line for every host'''
    def __init__(self):
        super(CategoryCanvas,self).__init__()


    def save_fig(self,filename):

        f, axes = plt.subplots(len(self.dict), sharex=True, sharey=False)
        f.set_size_inches(Constants.PLOT_WIDTH_INCHES,Constants.PLOT_HEIGHT_INCHES * len(axes))


        i = 0
        for category,plots in self.dict.iteritems():
            for p in plots:
                for line,label in p.lines:
                    axes[i].plot(line, label=label)

            if p.title:
                axes[i].set_title(p.title,y=1.20)
            if p.ymax:
                axes[i].set_ylim([0,p.ymax])
            if p.ylabel:
                axes[i].set_ylabel(p.ylabel)

            axes[i].legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                               ncol=2, mode="expand", borderaxespad=0.)
            i += 1

        plt.tight_layout()
        plt.savefig(filename)




