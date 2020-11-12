# -*- coding: utf-8 -*-
# @Author : lun
import pytest

from test_pytest.calculator import Calculator
from test_pytest.YamlUtil import Yaml

MyYml = Yaml("calc_data.yml")
data = MyYml.read_data()["data"]
data_ids = data["myids"]


class TestCalc:
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a, b, expect', data["add"], ids=data_ids)
    def test_add(self, begin_calc, a, b, expect):
        result = begin_calc.add(a, b)
        assert expect == result

    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect', data["div"], ids=data_ids)
    def test_div(self, begin_calc, a, b, expect):
        result = round(begin_calc.div(a,b),2)
        assert expect == result

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a, b, expect', data["sub"], ids=data_ids)
    def test_sub(self, begin_calc, a, b, expect):
        result = round(begin_calc.sub(a, b),2)
        assert expect == result

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expect', data["mul"], ids=data_ids)
    def test_mul(self, begin_calc, a, b, expect):
        result = round(begin_calc.mul(a, b),2)
        assert expect == result
