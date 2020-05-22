from hugh_04_leecode import fh_01_search_two_dimension_array
from hugh_04_leecode import fh_02_string_replace

if __name__ == '__main__':
    SearchTwoDimensionalArray = fh_01_search_two_dimension_array.SearchTwoDimensionalArray()

    flag = SearchTwoDimensionalArray.find(5, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]])
    print(flag)

    str = "We Are Happy"
    out = fh_02_string_replace.StringReplace().strreplace(str)
    print(out)

    str1 = "We Are Happy"
    out2 = fh_02_string_replace.StringReplace().strreplace2(str1)
    print(out2)
