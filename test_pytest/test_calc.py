# -*- coding: utf-8 -*-
# @Author : lun
import pytest

from test_pytest.calculator import Calculator
from test_pytest.YamlUtil import Yaml

MyYml = Yaml("calc_data.yml")
data = MyYml.read_data()["data"]
data_ids = data["myids"]


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("测试类开始")

    def teardown_class(self):
        print("测试类结束")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a, b, expect', data["add"], ids=data_ids)
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert expect == result

    @pytest.mark.parametrize('a,b,expect', data["div"], ids=data_ids)
    def test_div(self, a, b, expect):
        result = round(self.calc.div(a,b),2)
        assert expect == result
