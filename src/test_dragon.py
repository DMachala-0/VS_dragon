from dragon import move_left, move_right, generate_dragon


def test_move_left():
    assert move_left([0], [0], 0, 0) == (0, 1)
    assert move_left([0], [0], 0, 1) == (-1, 0)
    assert move_left([0], [0], 0, 2) == (0, -1)
    assert move_left([0], [0], 0, 3) == (1, 0)


def test_move_right():
    assert move_right([0], [0], 0, 0) == (0, -1)
    assert move_right([0], [0], 0, 1) == (-1, 0)
    assert move_right([0], [0], 0, 2) == (0, 1)
    assert move_right([0], [0], 0, 3) == (1, 0)


def test_generate_dragon():
    assert generate_dragon(0) == ('r', 'l', 'r')
    assert generate_dragon(1) == ('r', 'l', 'r')
    assert generate_dragon(2) == ('rrl', 'l', 'r')
    assert generate_dragon(3) == ('rrlrrll', 'l', 'r')
    assert generate_dragon(4) == ('rrlrrllrrrllrll', 'l', 'r')


# def test_