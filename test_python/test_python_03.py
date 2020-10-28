
class TongLao:
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def see_people(self,name):
        if name == "WYZ":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            raise ValueError("传入名字错误")


