from __future__ import annotations

from typing import Any
from typing import Callable

import pandas as pd
import pytest

from tests.utils import convert_dataframe_to_pandas_numpy
from tests.utils import integer_dataframe_5
from tests.utils import interchange_to_pandas


@pytest.mark.parametrize("keys", [["a", "b"], []])
@pytest.mark.parametrize("relax", [lambda x: x, lambda x: x.collect()])
def test_sort(library: str, keys: list[str], relax: Callable[[Any], Any]) -> None:
    df = relax(integer_dataframe_5(library, api_version="2023.09-beta"))
    result = df.sort(*keys)
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"a": [1, 1], "b": [3, 4]})
    pd.testing.assert_frame_equal(result_pd, expected)


@pytest.mark.parametrize("keys", [["a", "b"], []])
@pytest.mark.parametrize("relax", [lambda x: x, lambda x: x.collect()])
def test_sort_descending(
    library: str, keys: list[str], relax: Callable[[Any], Any]
) -> None:
    df = relax(integer_dataframe_5(library, api_version="2023.09-beta"))
    result = df.sort(*keys, ascending=False)
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"a": [1, 1], "b": [4, 3]})
    pd.testing.assert_frame_equal(result_pd, expected)
