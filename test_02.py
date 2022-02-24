import pytest


@pytest.mark.xfail(reason="unable to execute test")
def test_02_xfail():
    assert 1 == 2
