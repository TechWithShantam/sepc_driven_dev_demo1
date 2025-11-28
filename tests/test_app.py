import pytest
import pandas as pd
from io import BytesIO

# Basic test for reading Excel

def test_read_excel():
    df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)
    result = pd.read_excel(buffer)
    assert not result.empty
    assert list(result.columns) == ['A', 'B']
