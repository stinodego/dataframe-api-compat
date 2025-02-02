from __future__ import annotations

from tests.utils import integer_dataframe_1


def test_get_value(library: str) -> None:
    result = integer_dataframe_1(library).collect().col("a").get_value(0)
    assert int(result) == 1


def test_mean_scalar(library: str) -> None:
    result = integer_dataframe_1(library).collect().col("a").max()
    assert int(result) == 3
