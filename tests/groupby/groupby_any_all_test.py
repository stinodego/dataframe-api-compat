from __future__ import annotations

from typing import Any
from typing import Callable

import pandas as pd
import pytest
from polars.exceptions import SchemaError

from tests.utils import bool_dataframe_2
from tests.utils import convert_dataframe_to_pandas_numpy
from tests.utils import integer_dataframe_4
from tests.utils import interchange_to_pandas


@pytest.mark.parametrize(
    ("aggregation", "expected_b", "expected_c"),
    [
        ("any", [True, True], [True, False]),
        ("all", [False, True], [False, False]),
    ],
)
@pytest.mark.parametrize("maybe_collect", [lambda x: x, lambda x: x.collect()])
def test_groupby_boolean(
    library: str,
    aggregation: str,
    expected_b: list[bool],
    expected_c: list[bool],
    maybe_collect: Callable[[Any], Any],
) -> None:
    df = maybe_collect(bool_dataframe_2(library))
    df.__dataframe_namespace__()
    result = getattr(df.group_by("key"), aggregation)()
    # need to sort
    result = result.sort("key")
    result_pd = interchange_to_pandas(result, library)
    result_pd = convert_dataframe_to_pandas_numpy(result_pd)
    expected = pd.DataFrame({"key": [1, 2], "b": expected_b, "c": expected_c})
    pd.testing.assert_frame_equal(result_pd, expected)


def test_group_by_invalid_any_all(library: str, request: pytest.FixtureRequest) -> None:
    df = integer_dataframe_4(library)
    with pytest.raises((ValueError, SchemaError)):
        df.group_by("key").any()
    with pytest.raises((ValueError, SchemaError)):
        df.group_by("key").all()
