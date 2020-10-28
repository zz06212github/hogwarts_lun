## 定义5个类
# 1、定义树的类
class tree:
    def __init__(self):
        """
        构造函数，定义颜色属性和高度属性
        """
        self.color = "green"
        self.height = "10m"

    def shade(self):
        """
        实例方法，树的方法、遮阴
        :return:
        """
        print("乘凉遮阴")

    def photosynthesis(self):
        """
        实例方法，树的方法、光合作用
        :return:
        """
        print("光合作用")

# 2、定义纸的类
class paper:
    def __init__(self):
        """
        构造函数，定义颜色属性和大小属性
        """
        self.color = "white"
        self.size = "5cm^2"

    def write(self):
        """
        实例方法，纸的方法、写
        :return:
        """
        print("写")

    def fold(self):
        """
        实例方法，纸的方法、折纸
        :return:
        """
        print("折纸")

# 3、定义耳机的类
class headset:
    def __init__(self, price):
        """
        构造函数，定义颜色属性和价格属性
        """
        self.color = "black"
        self.price = price

    def listen(self):
        """
        实例方法，耳机的方法、听
        :return:
        """
        print("听")

    def sold(self):
        """
        实例方法，纸的方法、卖了
        :return:
        """
        print(f"卖了{self.price}块钱")

# 4、定义米的类
class rice:
    def __init__(self, weight):
        """
        构造函数，定义颜色属性和重量属性
        """
        self.color = "white"
        self.weight = weight

    def eat(self):
        """
        实例方法，米的方法、吃
        :return:
        """
        print("吃")

    def sold(self):
        """
        实例方法，米的方法、卖了
        :return:
        """
        print(f"卖了{self.weight}斤米")

# 5、定义小米的类
class millet(rice):
    def __init__(self,weight,color):
        """
        构造函数，定义颜色属性和重量属性
        """
        super().__init__(weight)
        self.color = color

    def cook(self):
        """
        实例方法，小米的方法、煮
        :return:
        """
        print("煮")
        print(f"重量是{self.weight}")
        print(f"颜色是{self.color}")