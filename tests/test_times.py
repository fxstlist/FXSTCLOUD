from datetime import datetime, timedelta

import pytest

import fxstcloud
from fxstcloud import ConvertTimeError


def test_convert_time():
    dt = fxstcloud.set_utc(datetime.utcnow())

    assert isinstance(fxstcloud.convert_dt(dt), str)
    assert isinstance(fxstcloud.convert_dt(timedelta(seconds=5)), str)
    assert isinstance(fxstcloud.convert_time(5), str)


def test_dc_timestamp():
    result = fxstcloud.dc_timestamp(0)
    assert result.startswith("<t:") and result.endswith(":R>")


def test_convert_so_seconds():
    assert fxstcloud.convert_to_seconds("1m 9s") == 69
    assert fxstcloud.convert_to_seconds("1.5m") == 90
    assert fxstcloud.convert_to_seconds("1,5 min") == 90
    assert fxstcloud.convert_to_seconds("1h 5m 10s") == 3910

    # month tests
    assert fxstcloud.convert_to_seconds("1mo 9s") == fxstcloud.convert_to_seconds("30t 9s")
    assert fxstcloud.convert_to_seconds("1mo 1min") == 2592060
    assert fxstcloud.convert_to_seconds("1m 1mo") == 2592060

    # tests with no units
    assert fxstcloud.convert_to_seconds("1 2m 3") == 120
    assert fxstcloud.convert_to_seconds("2") == 120
    assert fxstcloud.convert_to_seconds("2", default_unit="s", error=True) == 2
    assert fxstcloud.convert_to_seconds("2", default_unit=None) == 0

    with pytest.raises(ConvertTimeError):
        fxstcloud.convert_to_seconds("1 2 3", default_unit=None, error=True)

    # tests with invalid units
    assert fxstcloud.convert_to_seconds("") == 0
    assert fxstcloud.convert_to_seconds("z") == 0

    with pytest.raises(ConvertTimeError):
        assert fxstcloud.convert_to_seconds("", error=True)

    with pytest.raises(ConvertTimeError):
        assert fxstcloud.convert_to_seconds("z", error=True)