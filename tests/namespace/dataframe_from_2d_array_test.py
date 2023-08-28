from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from tests.utils import convert_dataframe_to_pandas_numpy
from tests.utils import integer_dataframe_1
from tests.utils import interchange_to_pandas


def test_dataframe_from_2d_array(library: str, request: pytest.FixtureRequest) -> None:
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    df = integer_dataframe_1(library)
    namespace = df.__dataframe_namespace__()
    arr = np.array([[1, 4], [2, 5], [3, 6]])
    result = namespace.dataframe_from_2d_array(
        arr, names=["a", "b"], dtypes={"a": namespace.Int64(), "b": namespace.Int64()}
    )
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    pd.testing.assert_frame_equal(result_pd, expected)


def test_dataframe_from_2d_array_invalid_version(library: str) -> None:
    df = integer_dataframe_1(library)
    namespace = df.__dataframe_namespace__()
    arr = np.array([[1, 4], [2, 5], [3, 6]])
    with pytest.raises(ValueError):
        namespace.dataframe_from_2d_array(
            arr,
            names=["a", "b"],
            dtypes={"a": namespace.Int64(), "b": namespace.Int64()},
            api_version="123.456",
        )
