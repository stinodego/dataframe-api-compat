from __future__ import annotations

import pandas as pd

from tests.utils import interchange_to_pandas
from tests.utils import nan_dataframe_1


def test_column_fill_nan(library: str) -> None:
    # todo: test with nullable pandas, check null isn't filled
    df = nan_dataframe_1(library).collect()
    ser = df.col("a")
    result = df.assign(ser.fill_nan(-1.0).rename("result"))
    result_pd = interchange_to_pandas(result, library)["result"]
    expected = pd.Series([1.0, 2.0, -1.0], name="result")
    pd.testing.assert_series_equal(result_pd, expected)
