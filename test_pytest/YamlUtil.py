# -*- coding: utf-8 -*-
# @Author : lun

import yaml
import os

class Yaml:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._date = None

    def read_data(self):
        if not self._date:
            with open(self.yamlf, "rb") as f:
                self._date = yaml.safe_load(f)
        return self._date

if __name__ == "__main__":
    MyYml = Yaml("calc_data.yml")
    print(MyYml.read_data())
