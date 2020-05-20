from hugh_04_leecode import fh_01_search_two_dimension_array

if __name__ == '__main__':
    SearchTwoDimensionalArray = fh_01_search_two_dimension_array.SearchTwoDimensionalArray()

    flag = SearchTwoDimensionalArray.find(5, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
    print(flag)
