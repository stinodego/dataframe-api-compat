from __future__ import annotations

from typing import Any
from typing import Callable

import pandas as pd
import pytest

from tests.utils import bool_dataframe_1
from tests.utils import bool_dataframe_3
from tests.utils import convert_dataframe_to_pandas_numpy
from tests.utils import interchange_to_pandas


@pytest.mark.parametrize(
    ("reduction", "expected_data"),
    [
        ("any", {"a": [True], "b": [True]}),
        ("all", {"a": [False], "b": [True]}),
    ],
)
@pytest.mark.parametrize("relax", [lambda x: x, lambda x: x.collect()])
def test_reductions(
    library: str,
    reduction: str,
    expected_data: dict[str, object],
    relax: Callable[[Any], Any],
) -> None:
    df = relax(bool_dataframe_1(library))
    result = getattr(df, reduction)()
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame(expected_data)
    pd.testing.assert_frame_equal(result_pd, expected)


@pytest.mark.parametrize("relax", [lambda x: x, lambda x: x.collect()])
def test_any(library: str, relax: Callable[[Any], Any]) -> None:
    df = relax(bool_dataframe_3(library))
    result = df.any()
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"a": [False], "b": [True], "c": [True]})
    pd.testing.assert_frame_equal(result_pd, expected)


@pytest.mark.parametrize("relax", [lambda x: x, lambda x: x.collect()])
def test_all(library: str, relax: Callable[[Any], Any]) -> None:
    df = relax(bool_dataframe_3(library))
    result = df.all()
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"a": [False], "b": [False], "c": [True]})
    pd.testing.assert_frame_equal(result_pd, expected)
