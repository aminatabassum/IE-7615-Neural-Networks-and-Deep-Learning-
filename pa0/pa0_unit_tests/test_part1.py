#!/usr/bin/python3
import numpy as np


def print_indexing_results(result):
    """
    Helper function to visualize the output of
    get_rows_and_elements_py or get_rows_and_elements_np

    Args:
        result: Tuple containing the first, middle & last rows & elements
            of the given array.

    Returns: Nothing.
    """
    message = (
        f"first row      : {result[0]}\n"
        f"middle row     : {result[1]}\n"
        f"last row       : {result[2]}\n"
        f"first element  : {result[3]}\n"
        f"middle element : {result[4]}\n"
        f"last element   : {result[5]}\n"
    )
    print(message)

def test_get_rows_and_elements_1(result) -> None:
    """
    Test # 1
    """
    # Testing array
    array_1x3 = np.array([[0, 1, 2]])
    expected_result = [np.array([0, 1, 2]),
                       np.array([0, 1, 2]),
                       np.array([0, 1, 2]),
                       0,
                       1,
                       2]

    is_correct = [np.array_equal(result[i], expected_result[i])
                  for i in range(len(expected_result))]
    is_passing = np.all(is_correct)

    if not is_passing:
        print("Testing your code with the following array:")
        print(array_1x3)
        print("\n")
        print("Output:")
        print_indexing_results(result)
        print("Expected Output:")
        print_indexing_results(expected_result)
    else:
        print("Test 1 pass.")

    assert is_passing


def test_get_rows_and_elements_2(result) -> None:
    """
    Test # 2
    """
    # Testing array
    array_3x3 = np.arange(9).reshape(3, 3)
    expected_result = [np.array([0, 1, 2]),
                       np.array([3, 4, 5]),
                       np.array([6, 7, 8]),
                       0,
                       4,
                       8]

    is_correct = [np.array_equal(result[i], expected_result[i])
                  for i in range(len(expected_result))]
    is_passing = np.all(is_correct)

    if not is_passing:
        print("Testing your code with the following array:")
        print(array_3x3)
        print("\n")
        print("Output:")
        print_indexing_results(result)
        print("Expected Output:")
        print_indexing_results(expected_result)
    else:
        print("Test 2 pass.")

    assert is_passing


def test_get_rows_and_elements_3(result) -> None:
    """
    Test # 3
    """
    # Testing array
    array_5x5 = np.arange(25).reshape(5, 5)
    expected_result = [np.array([0, 1, 2, 3, 4]),
                       np.array([10, 11, 12, 13, 14]),
                       np.array([20, 21, 22, 23, 24]),
                       0,
                       12,
                       24]

    is_correct = [np.array_equal(result[i], expected_result[i])
                  for i in range(len(expected_result))]
    is_passing = np.all(is_correct)

    if not is_passing:
        print("Testing your code with the following array:")
        print(array_5x5)
        print("\n")
        print("Output:")
        print_indexing_results(result)
        print("Expected Output:")
        print_indexing_results(expected_result)
    else:
        print("Test 3 pass.")

    assert is_passing


def test_get_rows_and_elements_4(result) -> None:
    """
    Test # 4
    """
    # Testing array
    array_7x1 = np.array([[72], [64], [36], [8], [78], [29], [49]])
    expected_result = [np.array([72]),
                       np.array([8]),
                       np.array([49]),
                       72,
                       8,
                       49]

    is_correct = [np.array_equal(result[i], expected_result[i])
                  for i in range(len(expected_result))]
    is_passing = np.all(is_correct)

    if not is_passing:
        print("Testing your code with the following array:")
        print(array_7x1)
        print("\n")
        print("Output:")
        print_indexing_results(result)
        print("Expected Output:")
        print_indexing_results(expected_result)
    else:
        print("Test 4 pass.")

    assert is_passing
    