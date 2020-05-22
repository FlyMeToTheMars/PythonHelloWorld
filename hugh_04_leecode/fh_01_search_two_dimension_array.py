
"""
        在一个二维数组中（每个一维数组的长度相同），
        每一行都按照从左到右递增的顺序排序，
        每一列都按照从上到下递增的顺序排序。
        请完成一个函数，
        输入这样的一个二维数组和一个整数，
        判断数组中是否含有该整数。
"""


class SearchTwoDimensionalArray:

    def find(self, target, array):
        row = len(array) - 1
        column = 0

        while row >= 0 and len(array[column]) - 1 >= column:
            if array[row][column] > target:
                row -= 1
            elif array[row][column] < target:
                column += 1
            else:
                return True
        return False
