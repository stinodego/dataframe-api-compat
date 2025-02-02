from __future__ import annotations

import numpy as np

from tests.utils import integer_dataframe_1


def test_to_array_object(library: str) -> None:
    df = integer_dataframe_1(library).collect()
    result = np.asarray(df.to_array(dtype="int64"))
    expected = np.array([[1, 4], [2, 5], [3, 6]], dtype=np.int64)
    np.testing.assert_array_equal(result, expected)
