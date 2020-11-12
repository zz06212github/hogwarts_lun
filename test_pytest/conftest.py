# -*- coding: utf-8 -*-
# @Author : lun
from typing import List
import pytest

from test_pytest.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

@pytest.fixture(scope="module")
def begin_calc():
    calc = Calculator()
    print("开始计算")
    yield calc
    print("结束计算")