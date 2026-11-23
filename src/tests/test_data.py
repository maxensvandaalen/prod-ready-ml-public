import pytest

from animal_shelter import data


def test_convert_camel_case():
    assert data.convert_camel_case("CamelCase") == "camel_case"
    assert data.convert_camel_case("CamelCASE") == "camel_case"
    assert data.convert_camel_case("camel-case") != "camel_case"
    assert data.convert_camel_case("snake_case") == "snake_case"
    assert data.convert_camel_case(" trim_snake_case   ") == "trim_snake_case"


def test_convert_camel_cases_raises_for_int():
    with pytest.raises(TypeError) as exception:
        data.convert_camel_case(123)
    assert "expected string or bytes-like object, got 'int'" in str(exception.value)
