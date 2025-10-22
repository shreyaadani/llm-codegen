from conftest import load_func
transpose_matrix = load_func(8, "transpose_matrix")

def test_square():
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    assert transpose_matrix(mat) == [[1,4,7],[2,5,8],[3,6,9]]

def test_rectangular():
    mat = [[1,2,3],[4,5,6]]
    assert transpose_matrix(mat) == [[1,4],[2,5],[3,6]]
