
import numpy as np


def test_mask_multiply_1(func) -> None:
    """
    Test # 1
    N = 4
    M = 9
    B = 13

    test_array = np.random.randint(50, size=(N, M))
    test_mask = np.random.randint(2, size=(B, N))
    """
    # make numpy arrays
    test_values = [[14, 22, 10, 1, 26, 36, 30, 9, 31],
                  [11, 39, 32, 41, 19, 19, 39, 42, 5],
                  [35, 33, 6, 1, 0, 27, 38, 20, 10],
                  [35, 45, 1, 2, 44, 26, 44, 26, 31]]

    mask_values = [[1, 0, 0, 1],
                  [1, 1, 1, 1],
                  [1, 0, 1, 0],
                  [1, 0, 1, 1],
                  [0, 1, 1, 1],
                  [1, 1, 0, 1],
                  [1, 0, 0, 0],
                  [1, 0, 0, 1],
                  [0, 0, 0, 0],
                  [1, 0, 1, 1],
                  [0, 1, 1, 1],
                  [0, 0, 0, 1],
                  [1, 1, 1, 0]]

    test_array = np.array(test_values)
    test_mask = np.array(mask_values)

    # expected 
    expected = [[126, 198, 90, 9, 234, 324, 270, 81, 279],
                [55, 195, 160, 205, 95, 95, 195, 210, 25],
                [245, 231, 42, 7, 0, 189, 266, 140, 70],
                [315, 405, 9, 18, 396, 234, 396, 234, 279]]
    expected = np.array(expected)
    
    # give appropriate function input
    if func == "mask_multiply_py":
        result = func(test_values, mask_values)
    else:
        result = func(test_array, test_mask)
    
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 1")
        print("Testing your code with the following array:")
        print(test_array)
        print("Testing your code with the following mark:")
        print(test_mask)
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 1 pass.\n")
        
    # enforce test
    assert is_correct

    
def test_mask_multiply_2(func) -> None:
    """
    Test # 2
    N = 9
    M = 4
    B = 13

    test_array = np.random.randint(50, size=(N, M))
    test_mask = np.random.randint(-1, 2, size=(B, N))
    """
    # make numpy arrays
    test_values = [[31, 41, 45, 17],
                   [20, 35, 20, 21],
                   [23, 31, 30, 45],
                   [12, 49,  1, 49],
                   [3,  21, 45, 27],
                   [4,  29, 24, 28],
                   [28, 44,  8, 32],
                   [14, 40, 25, 20],
                   [17,  4, 41, 49]]

    mask_values = [[ 1, -1,  1,  1, -1,  1, -1, -1, -1],
                   [ 1, -1,  0, -1, -1,  1,  0,  1, -1],
                   [-1, -1,  0, -1,  0,  0,  0,  1, -1],
                   [-1, -1,  1,  0, -1,  0,  0,  1, -1],
                   [-1, -1,  0,  0,  0,  0, -1, -1,  1],
                   [-1,  0, -1,  1,  1,  0, -1,  0,  1],
                   [ 1, -1,  0,  1, -1,  1, -1,  1,  1],
                   [ 0,  0,  0,  1,  0, -1, -1,  0,  1],
                   [ 1,  1, -1, -1, -1, -1, -1, -1,  0],
                   [-1,  0,  0,  1, -1, -1,  0,  1, -1],
                   [-1,  0,  1,  1,  0,  1,  1,  0,  0],
                   [-1,  0,  0, -1,  0,  1,  0,  1,  0],
                   [-1, -1,  0,  0, -1,  1,  0, -1, -1]]

    test_array = np.array(test_values)
    test_mask = np.array(mask_values)

    # expected 
    expected = [[-124, -164, -180,  -68],
                [-120, -210, -120, -126],
                [  23,   31,   30,   45],
                [  24,   98,    2,   98],
                [ -18, -126, -270, -162],
                [  12,   87,   72,   84],
                [-140, -220,  -40, -160],
                [  28,   80,   50,   40],
                [ -34,   -8,  -82,  -98]]
    expected = np.array(expected)
    
    # give appropriate function input
    if func == "mask_multiply_py":
        result = func(test_values, mask_values)
    else:
        result = func(test_array, test_mask)
        
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 2")
        print("Testing your code with the following array:")
        print(test_array)
        print("Testing your code with the following mark:")
        print(test_mask)
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 2 pass.\n")
        
    # enforce test
    assert is_correct

def test_mask_multiply_3(func) -> None:
    """
    Test # 3
    N = 5
    M = 5
    B = 5

    test_array = np.random.randint(50, size=(N, M))
    test_mask = np.random.randint(2, size=(B, N))
    """
    # make numpy arrays
    test_values = [[18,  2, 30, 24, 37],
                   [25,  2, 30, 17, 27],
                   [33, 42, 38, 39, 38],
                   [19, 36, 23,  9,  1],
                   [ 2, 23, 26, 36,  1]]

    mask_values = [[1, 0, 0, 0, 1],
                   [0, 0, 0, 0, 1],
                   [1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0],
                   [0, 1, 1, 1, 0]]

    test_array = np.array(test_values)
    test_mask = np.array(mask_values)

    # expected 
    expected = [[ 54,   6,  90,  72, 111],
                [ 50,   4,  60,  34,  54],
                [ 66,  84,  76,  78,  76],
                [ 19,  36,  23,   9,   1],
                [  4,  46,  52,  72,   2]]
    expected = np.array(expected)
    
    # give appropriate function input
    if func == "mask_multiply_py":
        result = func(test_values, mask_values)
    else:
        result = func(test_array, test_mask)
        
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 3")
        print("Testing your code with the following array:")
        print(test_array)
        print("Testing your code with the following mark:")
        print(test_mask)
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 3 pass.\n")
        
    # enforce test
    assert is_correct
    
def test_mask_multiply_4(func) -> None:
    """
    Test # 4
    N = 5
    M = 5
    B = 5

    test_array = np.random.randint(50, size=(N, M))
    test_mask = np.random.randint(-1, 2, size=(B, N))
    """
    # make numpy arrays
    test_values = [[ 2, 12,  3,  4, 43],
                   [ 8, 40,  2, 41,  4],
                   [10, 34, 26, 44,  1],
                   [12,  1, 39, 17, 35],
                   [39, 43,  7, 14, 17]]

    mask_values = [[-1, -1,  0, -1, -1],
                   [ 1, -1, -1,  0,  1],
                   [ 0, -1,  1,  0,  1],
                   [ 0, -1,  0,  0,  0],
                   [ 0, -1,  0,  0, -1]]

    test_array = np.array(test_values)
    test_mask = np.array(mask_values)

    # expected 
    expected = [[   0,    0,    0,    0,    0],
                [ -40, -200,  -10, -205,  -20],
                [   0,    0,    0,    0,    0],
                [ -12,   -1,  -39,  -17,  -35],
                [   0,    0,    0,    0,    0]]
    expected = np.array(expected)
    
    # give appropriate function input
    if func == "mask_multiply_py":
        result = func(test_values, mask_values)
    else:
        result = func(test_array, test_mask)
        
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 4")
        print("Testing your code with the following array:")
        print(test_array)
        print("Testing your code with the following mark:")
        print(test_mask)
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 4 pass.\n")
        
    # enforce test
    assert is_correct
    
def test_mask_multiply_5(func) -> None:
    """
    Test # 5
    N = 1
    M = 1
    B = 1

    test_array = np.random.randint(50, size=(N, M))
    test_mask = np.random.randint(2, size=(B, N))
    """
    # make numpy arrays
    test_values = [[20]]
    mask_values = [[1]]
    test_array = np.array(test_values)
    test_mask = np.array(mask_values)

    # expected 
    expected = [[20]]
    expected = np.array(expected)
    
    # give appropriate function input
    if func == "mask_multiply_py":
        result = func(test_values, mask_values)
    else:
        result = func(test_array, test_mask)
        
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 5")
        print("Testing your code with the following array:")
        print(test_array)
        print("Testing your code with the following mark:")
        print(test_mask)
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 5 pass.\n")
        
    # enforce test
    assert is_correct
    
def test_mask_multiply_6(func) -> None:
    """
    Test # 6
    N = 1
    M = 1
    B = 1

    test_array = np.random.randint(50, size=(N, M))
    test_mask = np.random.randint(1, size=(B, N))
    """
    # make numpy arrays
    test_values = [[43]]
    mask_values = [[0]]
    test_array = np.array(test_values)
    test_mask = np.array(mask_values)

    # expected 
    expected = [[0]]
    expected = np.array(expected)
    
    # give appropriate function input
    if func == "mask_multiply_py":
        result = func(test_values, mask_values)
    else:
        result = func(test_array, test_mask)
        
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 6")
        print("Testing your code with the following array:")
        print(test_array)
        print("Testing your code with the following mark:")
        print(test_mask)
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 6 pass.\n")
        
    # enforce test
    assert is_correct
    
def test_mask_multiply_7(func) -> None:
    """
    Test # 7
    N = 6
    M = 3
    B = 3

    test_array = np.random.randint(50, size=(N, M))
    test_mask = np.random.randint(2, size=(B, N))
    """
    # make numpy arrays
    test_values = [[20, 19,  5],
                   [30, 42,  5],
                   [49, 15, 37],
                   [41, 34, 46],
                   [ 1,  9, 17],
                   [25, 43, 48]]

    mask_values = [[0, 0, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 1, 1]]

    test_array = np.array(test_values)
    test_mask = np.array(mask_values)

    # expected 
    expected = [[ 0,  0,  0],
                [ 0,  0,  0],
                [98, 30, 74],
                [82, 68, 92],
                [ 1,  9, 17],
                [25, 43, 48]]
    expected = np.array(expected)
    
    # give appropriate function input
    if func == "mask_multiply_py":
        result = func(test_values, mask_values)
    else:
        result = func(test_array, test_mask)
        
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 7")
        print("Testing your code with the following array:")
        print(test_array)
        print("Testing your code with the following mark:")
        print(test_mask)
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 7 pass.\n")
        
    # enforce test
    assert is_correct
    
def test_mask_multiply_8(func) -> None:
    """
    Test # 8
    N = 6
    M = 3
    B = 3

    test_array = np.random.randint(50, size=(N, M))
    test_mask = np.random.randint(-1, 2, size=(B, N))
    """
    # make numpy arrays
    test_values = [[40, 10, 32],
                   [48, 43, 43],
                   [37, 37,  4],
                   [45, 18,  6],
                   [49,  9, 41],
                   [17, 30, 17]]

    mask_values = [[ 1,  0,  1,  0, -1,  0],
                   [ 0,  0,  1,  1, -1, -1],
                   [ 0, -1,  1,  1, -1,  1]]

    test_array = np.array(test_values)
    test_mask = np.array(mask_values)

    # expected 
    expected = [[  40,   10,   32],
                [ -48,  -43,  -43],
                [ 111,  111,   12],
                [  90,   36,   12],
                [-147,  -27, -123],
                [   0,    0,    0]]
    expected = np.array(expected)
    
    # give appropriate function input
    if func == "mask_multiply_py":
        result = func(test_values, mask_values)
    else:
        result = func(test_array, test_mask)
        
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 8")
        print("Testing your code with the following array:")
        print(test_array)
        print("Testing your code with the following mark:")
        print(test_mask)
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 8 pass.\n")
        
    # enforce test
    assert is_correct