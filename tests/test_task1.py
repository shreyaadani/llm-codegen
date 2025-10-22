# tests/test_task1.py
from conftest import load_func

min_cost_path = load_func(1, "min_cost_path")

def test_small_1():
    cost = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3],
    ]
    assert min_cost_path(cost, 2, 2) == 8  # 1→2→2→3

def test_small_2():
    cost = [
        [3, 4, 1, 2],
        [2, 1, 8, 9],
        [4, 7, 8, 1],
        [1, 2, 3, 4],
    ]
    assert min_cost_path(cost, 3, 3) == 16

def test_row_col_edges():
    cost = [
        [5, 9, 6],
        [11, 5, 2],
        [4, 7, 1],
    ]
    assert min_cost_path(cost, 0, 2) == 20  # 5→9→6
    assert min_cost_path(cost, 2, 0) == 20  # 5→11→4
