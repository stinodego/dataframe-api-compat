from __future__ import annotations

import pandas as pd
import pytest

from tests.utils import convert_dataframe_to_pandas_numpy
from tests.utils import integer_dataframe_4
from tests.utils import interchange_to_pandas


def test_groupby_size(library: str, request: pytest.FixtureRequest) -> None:
    if library == "polars-lazy":
        request.node.add_marker(pytest.mark.xfail())
    df = integer_dataframe_4(library)
    result = df.groupby(["key"]).size()
    # got to sort
    idx = result.sorted_indices(["key"])
    result = result.get_rows(idx)
    result_pd = interchange_to_pandas(result, library)
    expected = pd.DataFrame({"key": [1, 2], "size": [2, 2]})
    # TODO polars returns uint32. what do we standardise to?
    result_pd["size"] = result_pd["size"].astype("int64")
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    pd.testing.assert_frame_equal(result_pd, expected)
