
import numpy as np


def test_arange_1(result) -> None:
    """
    Test # 1
    N = 10
    M = 1
    """
    N = 10
    M = 1

    # expected 
    expected = [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
    expected = np.array(expected)
    
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 1")
        print("Testing your code with the following inputs:")
        print(f"N = {N}, M = {M}")
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 1 pass.\n")
        
    # enforce test
    assert is_correct

def test_arange_2(result) -> None:
    """
    Test # 2
    N = 1
    M = 10
    """
    N = 1
    M = 10

    # expected 
    expected = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
    expected = np.array(expected)
    
    # check test
    is_correct = np.array_equal(result, expected)

    # give user feedback
    if not is_correct:
        print("Test 2")
        print("Testing your code with the following inputs:")
        print(f"N = {N}, M = {M}")
        print("\n")
        print("Output:")
        print(result)
        print("Expected Output:")
        print(expected)
    else:
        print("Test 2 pass.\n")
        
    # enforce test
    assert is_correct