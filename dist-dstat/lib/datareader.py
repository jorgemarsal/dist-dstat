import csv
from constants import *

class DataReader:
    def __init__(self, filename, scale=1.0):
        self.filename = filename
        self.scale = scale

    def get_col(self, col_index):
        """
        :param col_index (int): index of the column
        :return: List of values for the specified col
        """
        col = []
        with open(self.filename, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            index = 0
            for row in reader:
                if index >= Constants.CSV_STARTING_INDEX:
                    col.append(float(row[col_index]) / self.scale)
                index += 1
        return col


    # def get_cols(self, col_index, operator):
    #     """
    #
    #     :param col_index (list):
    #     :param operator (string): valid ops are + *
    #     :return: List of values after applying operator to the columns
    #     """
    #     col = []
    #     with open(self.filename, 'rb') as csvfile:
    #         reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    #         for row in reader:
    #             values = []
    #             for c in col_index:
    #                 values.append(row[c])
    #             if operator == '+': col.append(reduce(lambda x, y: x+y, values))
    #             elif operator == '*': col.append(reduce(lambda x, y: x*y, values))
    #             else: raise Exception("operator %s is not supported" %(operator))
    #     return col
