
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

    def fight_zms(self, enemy_hp, enemy_power):
        self.hp = self.hp / 2
        self.power = self.power * 10
        self.hp = self.hp - enemy_power
        enemy_hp = enemy_hp - self.power
        if self.hp > enemy_hp:
            print(f"我的血量是{self.hp},敌人的血量是{enemy_hp}")
            print("I win")
        elif self.hp < enemy_hp:
            print(f"我的血量是{self.hp},敌人的血量是{enemy_hp}")
            print("Enemy win")
        else:
            print(f"我的血量是{self.hp},敌人的血量是{enemy_hp}")
            print("两败俱伤")

class XuZhu(TongLao):
    def __init__(self, hp, power):
        super().__init__(hp, power)

    def read(self):
        print("罪过罪过")

T = TongLao(2000,10)
T.see_people("WYZ")
T.fight_zms(1000,200)
X = XuZhu(2000,10)
X.read()