from suma import sum

def test_suma():
    assert sum(10,5) == 15
    assert sum(1,1) == 2
    assert sum(1,-5) == -4
    assert sum(0,0) == 0