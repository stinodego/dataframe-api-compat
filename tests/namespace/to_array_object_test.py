import numpy as np

from tests.utils import integer_dataframe_1, integer_series_1


def test_to_array_object(library: str) -> None:
    df = integer_dataframe_1(library)
    result = np.asarray(df.to_array_object(dtype="int64"))
    expected = np.array([[1, 4], [2, 5], [3, 6]], dtype=np.int64)
    np.testing.assert_array_equal(result, expected)


def test_column_to_array_object(library: str) -> None:
    df = integer_series_1(library)
    result = np.asarray(df.to_array_object(dtype="int64"))
    expected = np.array([1, 2, 3], dtype=np.int64)
    np.testing.assert_array_equal(result, expected)
