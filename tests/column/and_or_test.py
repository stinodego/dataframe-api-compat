from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd

from tests.utils import bool_dataframe_1
from tests.utils import interchange_to_pandas

if TYPE_CHECKING:
    import pytest


def test_column_and(library: str) -> None:
    df = bool_dataframe_1(library, api_version="2023.09-beta")
    ser = df.col("a")
    other = df.col("b")
    result = df.assign((ser & other).rename("result"))
    result_pd = interchange_to_pandas(result, library)["result"]
    expected = pd.Series([True, True, False], name="result")
    pd.testing.assert_series_equal(result_pd, expected)


def test_expression_and(library: str) -> None:
    df = bool_dataframe_1(library, api_version="2023.09-beta")
    df.__dataframe_namespace__()
    ser = df.col("a")
    other = df.col("b")
    result = df.assign((ser & other).rename("result"))
    result_pd = interchange_to_pandas(result, library)["result"]
    expected = pd.Series([True, True, False], name="result")
    pd.testing.assert_series_equal(result_pd, expected)


def test_column_or(library: str) -> None:
    df = bool_dataframe_1(library).collect()
    ser = df.col("a")
    other = df.col("b")
    result = df.assign((ser | other).rename("result"))
    result_pd = interchange_to_pandas(result, library)["result"]
    expected = pd.Series([True, True, True], name="result")
    pd.testing.assert_series_equal(result_pd, expected)


def test_column_and_with_scalar(library: str, request: pytest.FixtureRequest) -> None:
    df = bool_dataframe_1(library).collect()
    ser = df.col("a")
    other = True
    result = df.assign((ser & other).rename("result"))
    result_pd = interchange_to_pandas(result, library)["result"]
    expected = pd.Series([True, True, False], name="result")
    pd.testing.assert_series_equal(result_pd, expected)


def test_column_or_with_scalar(library: str, request: pytest.FixtureRequest) -> None:
    df = bool_dataframe_1(library).collect()
    ser = df.col("a")
    other = True
    result = df.assign((ser | other).rename("result"))
    result_pd = interchange_to_pandas(result, library)["result"]
    expected = pd.Series([True, True, True], name="result")
    pd.testing.assert_series_equal(result_pd, expected)
