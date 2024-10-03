from suma import sum

def test_suma():
    assert sum(3,5) == 8
    assert sum(0,1) == 1
    assert sum(-1,-5) == -6
    assert sum(0,0) == 0