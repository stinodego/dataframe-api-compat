from __future__ import annotations

import pandas as pd

from tests.utils import convert_dataframe_to_pandas_numpy
from tests.utils import integer_dataframe_1
from tests.utils import interchange_to_pandas


def test_get_column(library: str) -> None:
    df = integer_dataframe_1(library)
    df.__dataframe_namespace__()
    col = df.col
    result = col("a").rename("_tmp")
    result = df.assign(result).drop_columns("a").rename_columns({"_tmp": "a"})
    df.__dataframe_namespace__()
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})[["b", "a"]]
    pd.testing.assert_frame_equal(result_pd, expected)
