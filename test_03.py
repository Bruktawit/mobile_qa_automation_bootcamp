import pytest


@pytest.mark.skip(reason="Unable to execute test")
def test_03_skip():
    assert 1 == 2
