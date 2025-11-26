import pytest
from conftest import load_func

transpose_matrix = load_func(8, "transpose_matrix")


def test_transpose_square_matrix_spec():
    matrix = [[1, 2], [3, 4]]
    assert transpose_matrix(matrix) == [[1, 3], [2, 4]]


def test_transpose_rectangular_2x3_spec():
    matrix = [[1, 2, 3], [4, 5, 6]]
    assert transpose_matrix(matrix) == [[1, 4], [2, 5], [3, 6]]


def test_transpose_rectangular_3x2_spec():
    matrix = [[1, 2], [3, 4], [5, 6]]
    assert transpose_matrix(matrix) == [[1, 3, 5], [2, 4, 6]]


def test_transpose_single_row_1xN_spec():
    matrix = [[1, 2, 3, 4]]
    assert transpose_matrix(matrix) == [[1], [2], [3], [4]]


def test_transpose_single_column_Nx1_spec():
    matrix = [[1], [2], [3], [4]]
    assert transpose_matrix(matrix) == [[1, 2, 3, 4]]


def test_transpose_empty_matrix_spec():
    assert transpose_matrix([]) == []


def test_transpose_single_empty_row_spec():
    assert transpose_matrix([[]]) == []


def test_transpose_does_not_modify_input_spec():
    matrix = [[1, 2, 3], [4, 5, 6]]
    original = [row[:] for row in matrix]
    result = transpose_matrix(matrix)
    assert matrix == original
    assert result is not matrix
