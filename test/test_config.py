import pytest


class RangeCheck(Exception):
    def __init__(self,message="Value is not in range"):
        self.message=message
        super().__init__(self.message)


def test_generic():
    b=4
    with pytest.raises(RangeCheck):
        if b not in range(5,10):
            raise RangeCheck

    