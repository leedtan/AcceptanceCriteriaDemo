"""Example test to verify pytest setup works."""


def test_basic_assertion():
    """Basic test to verify pytest is working."""
    assert 1 + 1 == 2


def test_import_main():
    """Test that we can import from the main package."""
    from acceptance_criteria_demo import main

    assert callable(main)
