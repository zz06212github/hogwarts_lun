# 定义一个函数game
def game():
    # 定义初始变量my_hp、my_power、your_hp、your_power
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199
    # 不限次数的循环，每次循环进行一回合，并判断hp是否≤0，到0退出循环，没到0继续循环
    while True:
        # 我这一轮hp = 我上一轮hp - 敌人power，敌人这一轮hp = 敌人上一轮hp - 我power
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        # 打印我的hp
        print(my_hp)
        # 判断我hp≤0，打印我输了，退出while循环
        if my_hp <= 0:
            print("我输了")
            break
        # 判断敌人hp≤0，打印你输了，退出while循环
        elif your_hp <= 0:
            print("你输了")
            break

# 调用函数game
game()