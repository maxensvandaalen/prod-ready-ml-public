import pandas as pd
import pytest
from pandas.testing import assert_series_equal

from animal_shelter import features


@pytest.fixture(scope="function")
def sex_upon_outcome():
    return pd.Series(
        [
            "neutered Female",
            "NEutered male",
            "123Spayed234123Female",
            " intact  Male",
            "abc",
        ]
    )


def test_check_has_name():
    s = pd.Series(["Ivo", "Henk", "unknown"])
    result = features.check_has_name(s)
    expected = pd.Series([True, True, False])
    assert_series_equal(result, expected)


def test_is_dog():
    s = pd.Series(["cat", "DOG", "dog", "CaT"])
    result = features.check_is_dog(s)
    expected = pd.Series([False, True, True, False])
    assert_series_equal(result, expected)


def test_get_sex(sex_upon_outcome):
    result = features.get_sex(sex_upon_outcome)
    expected = pd.Series(["female", "unknown", "female", "male", "unknown"])
    assert_series_equal(result, expected)


def test_get_neutered(sex_upon_outcome):
    result = features.get_neutered(sex_upon_outcome)
    expected = pd.Series(["fixed", "fixed", "fixed", "intact", "unknown"])
    assert_series_equal(result, expected)


def test_get_hair_type():
    s = pd.Series(["abc ShortHair", "123 Medium Hair", "Hair", "LongHair"])
    result = features.get_hair_type(s)
    expected = pd.Series(["shorthair", "medium hair", "unknown", "longhair"])
    assert_series_equal(result, expected)


def test_compute_days_upon_outcome():
    s = pd.Series(["45 years", "1 day", "0 days", "12 weeks"])
    result = features.compute_days_upon_outcome(s)
    expected = pd.Series([16425.0, 1.0, 0.0, 84.0])
    assert_series_equal(result, expected)


def test_is_dog_raises_for_other_animal():
    with pytest.raises(RuntimeError) as exception:
        s = pd.Series(["Horse", "DOG", "dog", "CaT"])
        features.check_is_dog(s)
    assert "Found pets that are not dogs or cats." in str(exception.value)
