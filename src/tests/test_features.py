import pandas as pd
import pytest
from pandas.testing import assert_series_equal

from animal_shelter import features


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


def test_get_sex():
    s = pd.Series(["Female", "male", "123Female", "   Male"])
    result = features.get_sex(s)
    expected = pd.Series(["female", "unknown", "female", "male"])
    assert_series_equal(result, expected)


def test_get_neutered():
    s = pd.Series(["neutered", "NEutered", "123Spayed234", "   intact  ", "abc"])
    result = features.get_neutered(s)
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
