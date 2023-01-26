import numpy as np


def print_medians(result):
    """
    Helper function to visualize the output of get_medians_np or get_medians_py

    Args:
        result: Tuple containing the median values and indices and the average values
            over the rows and columns of the given array.

    Returns: Nothing.
    """
    message = (
        f"median row values       : {result[0]}\n"
        f"median col values       : {result[1]}\n"
        f"median row value indices: {result[2]}\n"
        f"median col value indices: {result[3]}\n"
        f"average row value       : {result[4]}\n"
        f"average col value       : {result[5]}\n"
    )
    print(message)


def test_get_medians_1(result) -> None:
    """
    Test # 1
    """
    # Testing array
    array_1x3 = np.array([[0, 1, 2]])

    expected_result = [np.array([1]),
                       np.array([0, 1, 2]),
                       np.array([1]),
                       np.array([0, 1, 2]),
                       np.array([1.]),
                       np.array([0.0, 1.0, 2.0])]

    is_correct = [np.array_equal(result[i], expected_result[i])
                  for i in range(len(expected_result))]
    is_passing = np.all(is_correct)

    if not is_passing:
        print("Testing your code with the following array:")
        print(array_1x3)
        print("\n")
        print("Output:")
        print_medians(result)
        print("Expected Output:")
        print_medians(expected_result)
    else:
        print("Test 1 pass.")

    assert is_passing


def test_get_medians_2(result) -> None:
    """
    Test # 2
    """
    # Testing array
    array_3x3 = np.arange(9).reshape(3, 3)

    expected_result = [np.array([1, 4, 7]),
                       np.array([3, 4, 5]),
                       np.array([1, 4, 7]),
                       np.array([3, 4, 5]),
                       np.array([1.0, 4.0, 7.0]),
                       np.array([3.0, 4.0, 5.0])]

    is_correct = [np.array_equal(result[i], expected_result[i])
                  for i in range(len(expected_result))]
    is_passing = np.all(is_correct)

    if not is_passing:
        print("Testing your code with the following array:")
        print(array_3x3)
        print("\n")
        print("Output:")
        print_medians(result)
        print("Expected Output:")
        print_medians(expected_result)
    else:
        print("Test 2 pass.")

    assert is_passing


def test_get_medians_3(result) -> None:
    """
    Test # 3
    """
    # Testing array
    array_5x5 = np.arange(25).reshape(5, 5)

    expected_result = [np.array([2, 7, 12, 17, 22]),
                       np.array([10, 11, 12, 13, 14]),
                       np.array([2, 7, 12, 17, 22]),
                       np.array([10, 11, 12, 13, 14]),
                       np.array([2.0, 7.0, 12.0, 17.0, 22.0]),
                       np.array([10.0, 11.0, 12.0, 13.0, 14.0])]

    is_correct = [np.array_equal(result[i], expected_result[i])
                  for i in range(len(expected_result))]
    is_passing = np.all(is_correct)

    if not is_passing:
        print("Testing your code with the following array:")
        print(array_5x5)
        print("\n")
        print("Output:")
        print_medians(result)
        print("Expected Output:")
        print_medians(expected_result)
    else:
        print("Test 3 pass.")

    assert is_passing


def test_get_medians_4(result) -> None:
    """
    Test # 4
    """
    # Testing array
    array_7x1 = np.array([[72], [64], [36], [8], [78], [29], [49]])

    expected_result = [np.array([72, 64, 36, 8, 78, 29, 49]),
                       np.array([49]),
                       np.array([72, 64, 36, 8, 78, 29, 49]),
                       np.array([49]),
                       np.array([72.0, 64.0, 36.0, 8.0, 78.0, 29.0, 49.0]),
                       np.array([48.0])]

    is_correct = [np.array_equal(result[i], expected_result[i])
                  for i in range(len(expected_result))]
    is_passing = np.all(is_correct)

    if not is_passing:
        print("Testing your code with the following array:")
        print(array_7x1)
        print("\n")
        print("Output:")
        print_medians(result)
        print("Expected Output:")
        print_medians(expected_result)
    else:
        print("Test 4 pass.")

    assert is_passing
