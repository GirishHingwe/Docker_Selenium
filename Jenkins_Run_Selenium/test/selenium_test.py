import pytest

@pytest.mark.smoke
def test_google(setup):
    driver = setup
    driver.get("https://www.google.com")

    assert "Google" in driver.title