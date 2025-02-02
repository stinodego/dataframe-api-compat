from __future__ import annotations

import pandas as pd
import pytest

from tests.utils import integer_dataframe_1


def test_name(library: str) -> None:
    df = integer_dataframe_1(library).collect()
    name = df.col("a").name
    assert name == "a"


def test_invalid_name_pandas() -> None:
    with pytest.raises(ValueError):
        pd.Series([1, 2, 3], name=0).__column_consortium_standard__()
