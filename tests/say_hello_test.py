import pytest
from my_python_package_scaffold import my_functions


# pytest discover tests if function names have "test" in the beginning.
# c.f. https://docs.pytest.org/en/latest/explanation/goodpractices.html#test-discovery
def test_say_hello():
    assert my_functions.say_hello() == 'hello from my package!'
