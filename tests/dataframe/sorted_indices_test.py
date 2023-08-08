from __future__ import annotations

import pandas as pd
import pytest

from tests.utils import convert_dataframe_to_pandas_numpy
from tests.utils import integer_dataframe_5
from tests.utils import interchange_to_pandas


def test_sorted_indices(
    library: str,
    request: pytest.FixtureRequest,
) -> None:
    if library == "polars-lazy":
        # todo: not working yet
        request.node.add_marker(pytest.xfail())
    df = integer_dataframe_5(library)
    sorted_indices = df.sorted_indices(keys=["a", "b"])
    result = df.get_rows(sorted_indices)
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"a": [1, 1], "b": [3, 4]})
    pd.testing.assert_frame_equal(result_pd, expected)


def test_sorted_indices_descending(
    library: str,
    request: pytest.FixtureRequest,
) -> None:
    if library == "polars-lazy":
        # todo: not working yet
        request.node.add_marker(pytest.xfail())
    df = integer_dataframe_5(library)
    sorted_indices = df.sorted_indices(keys=["a", "b"], ascending=False)
    result = df.get_rows(sorted_indices)
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"a": [1, 1], "b": [4, 3]})
    pd.testing.assert_frame_equal(result_pd, expected)
