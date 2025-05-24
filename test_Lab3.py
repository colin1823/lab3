import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_morethan_10():

    input_arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)



    
    assert result == 1 


    
def test_bubble_sort_empty():
    
    input_arr = []
    
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)
    
def test_bubble_float():
    result = []
    input_arr = [64.5, 34.2, 25.1, 12.3, 22.4, 11.6, 90.7]
    test_arr = []
    result = Lab3.bubble_float(input_arr, Lab3.SORT_ASCENDING)
    test_arr = 1    
    assert (result == test_arr)

    