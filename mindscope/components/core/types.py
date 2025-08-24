from typing import Hashable, Callable, Dict

import polars as pl

# types
LoaderDict = Dict[Hashable, Callable[[], pl.DataFrame]]
EMPTY_DF = pl.DataFrame()
