import time
import pytest
from pytest import mark


@pytest.mark.usefixtures("setup")
class NavigationTests:

    def test_something(self):
        assert True
